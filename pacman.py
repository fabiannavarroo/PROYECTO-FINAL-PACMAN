from constantes import *
import pyxel
import time

class Pacman:
    def __init__(self, x, y, bloque):
        self.x = x
        self.y = y
        self.velocidad = 2  # Velocidad de movimiento
        self.bloque = bloque
        self.direccion_actual = PACMAN  # Dirección inicial
        self.direccion_pendiente = None  # Dirección elegida por el jugador
        self.vidas = 3  # Pac-Man empieza con 3 vidas
        self.animacion_frame = 0
        self.en_muerte = False  # Indica si Pac-Man está en animación de muerte
        self.reiniciando = False  # Estado para evitar colisiones durante el reinicio
        self.fantasmas_comido = False
        self.mostrar_puntos = False
        self.texto_tiempo_inicio = 0
        self.posicionx,self.posiciony = 0,0
         



    def draw(self, fantasmas):
        if self.vidas <= 0:  # Si no hay vidas, no se dibuja
            return

        if self.en_muerte:
            self.animar_muerte(fantasmas)
        else:
            if pyxel.frame_count // REFRESH % 2 == 0:
                sprite_x, sprite_y = self.direccion_actual
            else:
                if self.direccion_actual == PACMAN_ARRIBA:
                    sprite_x, sprite_y = PACMAN_ARRIBA_CERRADA
                elif self.direccion_actual == PACMAN_ABAJO:
                    sprite_x, sprite_y = PACMAN_ABAJO_CERRADA
                elif self.direccion_actual == PACMAN_IZQUIERDA:
                    sprite_x, sprite_y = PACMAN_IZQUIERDA_CERRADA
                elif self.direccion_actual == PACMAN_DERECHA:
                    sprite_x, sprite_y = PACMAN_DERECHA_CERRADA
                else:
                    sprite_x, sprite_y = PACMAN
            # Dibujar Pac-Man
            pyxel.blt(self.x, self.y, 0, sprite_x, sprite_y, 16, 16, colkey=0)

            # Dibujar vidas
            self.ver_vidas(10, 10)

            # Mostrar puntos cuando come fantasmas
            if self.mostrar_puntos and time.time() - self.texto_tiempo_inicio < 2:  # Mostrar por 2 segundos
                pyxel.text(self.x, self.y - 10, "+200 puntos", pyxel.COLOR_CYAN)
            else:
                self.mostrar_puntos = False



    def mover(self,):
        if self.vidas <= 0 or self.en_muerte or self.reiniciando:  # Si no hay vidas, está en muerte o reiniciando, no se mueve
            return False

        nueva_x, nueva_y = self.x, self.y

        # Detectar entrada del jugador para cambiar dirección
        if pyxel.btnp(pyxel.KEY_UP):
            self.direccion_pendiente = PACMAN_ARRIBA
        elif pyxel.btnp(pyxel.KEY_DOWN):
            self.direccion_pendiente = PACMAN_ABAJO
        elif pyxel.btnp(pyxel.KEY_LEFT):
            self.direccion_pendiente = PACMAN_IZQUIERDA
        elif pyxel.btnp(pyxel.KEY_RIGHT):
            self.direccion_pendiente = PACMAN_DERECHA

        # Verificar si la dirección pendiente es válida
        if self.direccion_pendiente:
            if self.direccion_pendiente == PACMAN_ARRIBA and not self.bloque.colision(self.x, self.y - self.velocidad):
                self.direccion_actual = self.direccion_pendiente
            elif self.direccion_pendiente == PACMAN_ABAJO and not self.bloque.colision(self.x, self.y + self.velocidad):
                self.direccion_actual = self.direccion_pendiente
            elif self.direccion_pendiente == PACMAN_IZQUIERDA and not self.bloque.colision(self.x - self.velocidad, self.y):
                self.direccion_actual = self.direccion_pendiente
            elif self.direccion_pendiente == PACMAN_DERECHA and not self.bloque.colision(self.x + self.velocidad, self.y):
                self.direccion_actual = self.direccion_pendiente

        # Mover en la dirección actual
        if self.direccion_actual == PACMAN_ARRIBA:
            nueva_y -= self.velocidad
        elif self.direccion_actual == PACMAN_ABAJO:
            nueva_y += self.velocidad
        elif self.direccion_actual == PACMAN_IZQUIERDA:
            nueva_x -= self.velocidad
        elif self.direccion_actual == PACMAN_DERECHA:
            nueva_x += self.velocidad

        # Verificar colisiones
        if not self.bloque.colision(nueva_x, self.y):
            self.x = nueva_x
        if not self.bloque.colision(self.x, nueva_y):
            self.y = nueva_y

        #  Portales
        if (self.x, self.y) in PORTALES:
            self.x, self.y = PORTALES[(self.x, self.y)]

        if self.fantasmas_comido:
            pyxel.text(self.posicionx, self.posiciony, "+200 puntos", pyxel.COLOR_CYAN)
            self.fantasmas_comido = False


        print("Pacman", self.x, self.y)


    def colision_fantasmas(self, fantasmas, puntos):
        if self.en_muerte or self.reiniciando or self.vidas <= 0:  # Si está muerto, reiniciando o sin vidas, no revisa colisiones
            return False

        # Calcular las posiciones centrales de Pac-Man y los fantasmas
        pacman_x = self.x + 8  # Centrar la posición de Pac-Man
        pacman_y = self.y + 8

        for fantasma in fantasmas:
            fantasma_x = fantasma.x + 8  # Centrar la posicion del fantasma
            fantasma_y = fantasma.y + 8

            # Detectar si hay colisión 
            if abs(pacman_x - fantasma_x) < 16 and abs(pacman_y - fantasma_y) < 16:
                if fantasma.asustado:
                    puntos.puntos += 200  # Añade puntos por comer un fantasma
                    self.fantasmas_comido = True
                    self.mostrar_puntos = True  # Poder mostrar puntos
                    self.texto_tiempo_inicio = time.time()  # Guarda el tiempo actual
                    self.posicionx, self.posiciony = self.x, self.y
                    fantasma.volver_a_trampa()  # Enviar fantasma a la trampa
                    return True
                else:
                    self.perder_vida()  # Pac-Man pierde una vida
                    return True

        return False  # No hay colision


    def perder_vida(self):
        self.vidas -= 1
        self.en_muerte = True
        self.animacion_frame = 0
        self.reiniciando = True  # Activar estado de reinicio


    def animar_muerte(self, fantasmas):
        if not self.en_muerte:
            return

        if self.animacion_frame < len(ANIMACION_MUERTE):
            sprite_x, sprite_y = ANIMACION_MUERTE[self.animacion_frame]
            pyxel.blt(self.x, self.y, 0, sprite_x, sprite_y, 16, 16, colkey=0)
            if pyxel.frame_count % 5 == 0:  # Cambiar cada 5 frames
                self.animacion_frame += 1
        else:
            self.en_muerte = False
            self.reiniciar_posiciones(fantasmas)  # Reiniciar tras la animación


    def reiniciar_posiciones(self, fantasmas):
        # Reiniciar posiciones de Pac-Man y fantasmas después de la animación
        self.x, self.y = 192, 304  # Posición inicial de Pac-Man
        for fantasma in fantasmas:
            fantasma.volver_a_posicion_inicial()
        self.reiniciando = False  # Desactivar estado de reinicio


    def ver_vidas(self, x, y):
        # Dibujar las vidas restantes
        sprite_x, sprite_y = PACMAN
        sprite_w, sprite_h = 16, 16
        pos_x = x
        for i in range(self.vidas):
            pyxel.blt(pos_x, y, 0, sprite_x, sprite_y, sprite_w, sprite_h, colkey=0)
            pos_x += sprite_w + 2



from constantes import *
import pyxel
import time

class Pacman:
    def __init__(self, x, y, bloque):
        self.x = x
        self.y = y
        self.velocidad = 2
        self.bloque = bloque
        self.direccion_actual = PACMAN
        self.direccion_pendiente = None
        self.vidas = 3
        self.animacion_frame = 0
        self.en_muerte = False
        self.reiniciando = False
        self.fantasmas_comido = False
        self.mostrar_puntos = False
        self.texto_tiempo_inicio = 0


    def mover(self):
        if self.vidas <= 0 or self.en_muerte or self.reiniciando:
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

        # Mostrar puntos si el tiempo no ha expirado
        if self.mostrar_puntos and time.time() - self.texto_tiempo_inicio < 2:  # Mostrar por 2 segundos
            pyxel.text(self.x, self.y - 10, "200 puntos", pyxel.COLOR_YELLOW)
        else:
            self.mostrar_puntos = False

    def colision_fantasmas(self, fantasmas, puntos):
        if self.en_muerte or self.reiniciando or self.vidas <= 0:
            return False

        pacman_x = self.x + 8
        pacman_y = self.y + 8

        for fantasma in fantasmas:
            fantasma_x = fantasma.x + 8
            fantasma_y = fantasma.y + 8

            if abs(pacman_x - fantasma_x) < 16 and abs(pacman_y - fantasma_y) < 16:
                if fantasma.asustado:
                    puntos.puntos += 200
                    self.fantasmas_comido = True
                    self.mostrar_puntos = True  # Activar la visualización de puntos
                    self.texto_tiempo_inicio = time.time()  # Registrar el tiempo actual
                    fantasma.volver_a_trampa()
                    return True
                else:
                    self.perder_vida()
                    return True

        return False
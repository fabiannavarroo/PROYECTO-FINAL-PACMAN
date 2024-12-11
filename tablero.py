from pacman import Pacman
from collections import deque
from fantasmas import *
from puntos import Puntos
from bloque import Bloque
from constantes import *
import random
import time
import pyxel


class Tablero:
    def __init__(self):
        # Inicializar la ventana del juego
        pyxel.init(400, 400, title="Pacman", fps=30)
        # Cargar los recursos del archivo .pyxres
        pyxel.load("assets/recursos.pyxres")
        # Iniciar la música 
        pyxel.playm(0,0,True)

        # Crear el objeto bloque, que representa el mapa
        self.bloque = Bloque()  
        # Crear el objeto Pacman, en la posición 192, 304
        self.pacman = Pacman(192, 304)
        # Crear la lista de fantasmas con sus posiciones iniciales
        self.fantasmas = [
            FantasmaRojo(160, 208),
            FantasmaRosa(181, 208),
            FantasmaAzul(203, 208),
            FantasmaNaranja(225, 208),
        ]
        # Crear el objeto Puntos, que sera el encargado los puntos, frutas y regalos
        self.puntos = Puntos(OBJETOS)

        # Generar puntos por todo el mapa
        self.generar_puntos()

        # Variable para controlar el mensaje READY!
        self.mostrar_ready = True
        self.contador_ready = 0

        # Variables para controlar GAME OVER
        self.contador_game_over = 0
        self.mostrar_fin = False

        # Controlar la animación de muerte final de Pac-Man
        self.animacion_muerte_finalizada = False

        # Controlar la condición de victoria
        self.victoria = False

        # Distancia de emboscada para el fantasma rosa
        self.celdas_para_emboscada = 4

        # Cambiar la dirección de los fantasmas
        self.fantasmas_cambio_de_movimiento = 20

        # Iniciar el bucle principal de Pyxel
        pyxel.run(self.update, self.draw)

    def update(self):

        if self.pacman.vidas > 0:
            # Mientras Pac-Man tenga vidas
            if self.contador_ready < 90:
                # Mostrar el mensaje READY! por un tiempo
                self.contador_ready += 1
                if self.contador_ready == 90:
                    self.mostrar_ready = False  # Ocultar READY! después de un tiempo

            if not self.pacman.en_muerte:
                # Actualizar el juego si Pac-Man no está en estado de muerte
                
                # Mover Pac-Man según la dirección del jugador
                self.movimineto_pacman()
                # Comprobar si Pac-Man come puntos
                self.comer_puntos()
                # Comprobar si Pac-Man come fruta
                self.comer_fruta()
                # Intentar generar una fruta cada cierto tiempo
                self.generar_fruta()

                # Actualizar cada fantasma
                for index, fantasma in enumerate(self.fantasmas):
                    if fantasma.en_trampa():
                        # Si el fantasma está en la trampa, esperar un tiempo antes de que salga
                        tiempo_espera = (index + 1) * 2
                        if time.time() - fantasma.tiempo_trampa >= tiempo_espera:
                            fantasma.salir_de_trampa()
                    else:
                        # Movimiento normal de los fantasmas fuera de la trampa
                        if isinstance(fantasma, FantasmaRojo):
                            self.mover_fantasma_rojo(fantasma)
                        elif isinstance(fantasma, FantasmaRosa):
                            self.mover_fantasma_rosa(fantasma)
                        elif isinstance(fantasma, FantasmaAzul):
                            self.mover_fantasma_azul(fantasma)
                        elif isinstance(fantasma, FantasmaNaranja):
                            self.mover_fantasma_naranja(fantasma)

                    # Actualizar el estado del fantasma 
                    fantasma.actualizar_estado()

                # Comprobar colisiones entre fantasmas y Pac-Man
                self.colision_fantasmas_con_pacman()
                # Comprobar colisiones de fantasmas con el mapa
                self.colision_fantasmas(fantasma.x, fantasma.y)

                # Comprobar si se han comido todos los puntos y regalos
                if self.comprobar_puntos_restantes():
                    # Si hay un siguiente nivel, pasar al siguiente
                    if self.bloque.nivel + 1 in self.bloque.mapas:
                        self.bloque.nivel += 1
                        self.bloque.cargar_mapa()
                        self.reiniciar_puntos()
                        self.reiniciar_tablero()
                    else:
                        # Si no hay más niveles, ganar el juego
                        self.victoria = True
                        
            else:
                # Si Pac-Man está en muerte, ejecutar la animación de muerte
                self.animar_muerte()

        else:
            # Pac-Man no tiene vidas
            if not self.animacion_muerte_finalizada:
                # Ejecutar la animación de muerte final de Pac-Man
                self.animar_muerte()
                if self.pacman.animacion_frame >= len(ANIMACION_MUERTE):
                    self.animacion_muerte_finalizada = True
            else:
                # Después de la animación de muerte final, esperar antes de mostrar GAME OVER fijo
                self.contador_game_over += 1

    def draw(self):
        pyxel.cls(0)  # Limpiar la pantalla
        self.dibujar_letras_mapa(120,16,"HIGHSCORE")
        self.puntos.ver_puntuacion(195,16)
        if self.pacman.vidas > 0:
            # Mientras Pac-Man tenga vidas, dibujar el mapa y los objetos
            self.bloque.draw()  # Dibujar el mapa
            if self.pacman.en_muerte:
                # Si Pac-Man está en animación de muerte, dibujar solo la animación
                self.animar_muerte()
            else:
                # Dibujar puntos, frutas, puntuación
                self.puntos.draw()
                # Dibujar las vidas de Pac-Man
                self.pacman.ver_vidas(10, 10)
                # Dibujar a Pac-Man
                self.pacman.draw()
                # Dibujar los fantasmas
                for fantasma in self.fantasmas:
                    fantasma.draw()

                # Dibujar el mensaje READY! si corresponde
                if self.mostrar_ready:
                    self.animar_ready()

                # Si Pac-Man ha comido un fantasma, mostrar los puntos que ganó
                if self.pacman.mostrar_puntos and time.time() - self.pacman.texto_tiempo_inicio < 1.5:
                    pyxel.text(self.pacman.posicion_fantasma_comido_x, self.pacman.posicion_fantasma_comido_y, "+200 puntos", pyxel.COLOR_RED)
                else:
                    self.pacman.mostrar_puntos = False

            # Si se ganó la partida, limpiar pantalla y volver a dibujar el mapa
            if self.victoria:
                pyxel.cls(0)
                self.bloque.draw()
        else:
            # Si Pac-Man no tiene vidas, mostrar GAME OVER
            pyxel.cls(0)
            self.bloque.draw()
            self.animar_muerte()
            self.animar_fin()

    #--------------------------------------------------------------------REINICIO--------------------------------------------------------------------#

    def reiniciar_fantasmas(self):
        # Reiniciar fantasmas a su posición original después de una muerte o cambio de nivel
        for fantasma in self.fantasmas:
            fantasma.volver_a_posicion_inicial()
            fantasma.siguiente_celda = None
            fantasma.tiempo_trampa = time.time()

    def reiniciar_tablero(self):
        # Reinicia las condiciones iniciales después de la animación de muerte o al cambiar de nivel
        self.mostrar_ready = True
        self.contador_ready = 0
        self.bloque.cargar_mapa()
        self.reiniciar_posiciones()
        self.pacman.en_muerte = False
        self.pacman.animacion_frame = 0

    def reiniciar_posiciones(self):
        # Reiniciar las posiciones de Pac-Man y fantasmas a sus posiciones iniciales
        self.pacman.x, self.pacman.y = 192, 304
        for fantasma in self.fantasmas:
            fantasma.volver_a_posicion_inicial()
        self.pacman.reiniciando = False

    def reiniciar_puntos(self):
        # Reiniciar los puntos, regalos y frutas al cambiar de nivel
        self.puntos.regalos = [(16, 304), (368, 304), (16, 80),(368, 80)]
        self.puntos.lista_puntos = []
        self.generar_puntos()
        self.puntos.ultimo_tiempo_fruta = time.time()
        self.puntos.fruta_actual = None
        self.puntos.posicion_fruta = None
        self.puntos.animacion_activa = False
        self.puntos.animacion_contador = 0

    #--------------------------------------------------------------------ANIMACIONES--------------------------------------------------------------------#

    def animar_ready(self):
        # Animación del mensaje READY! durante los primeros segundos del nivel
        if self.contador_ready < 90:
            # Alternar el mensaje cada cierto tiempo para parpadear
            if (self.contador_ready // 10) % 2 == 0:
                self.dibujar_letras_mapa(180,240,"READY!")
            else:
                pyxel.blt(180, 245, 2, 0, 0, 0, 0, colkey=0)
        else:
            # Mantener un vacio después del tiempo
            pyxel.blt(180, 245, 2, 0, 0, 0, 0, colkey=0)

    def animar_fin(self):
        # Animación del mensaje GAME OVER cuando se acaban las vidas de Pac-Man
        if self.contador_game_over < 70:
            if (self.contador_game_over // 10) % 2 == 0:
                self.dibujar_letras_mapa(185,208,"GAME OVER")
            else:
                pyxel.blt(180, 245, 2, 0, 0, 0, 0, colkey=0)
        else:
            # Mantener el texto "GAME OVER" visible
            self.dibujar_letras_mapa(185,208,"GAME OVER")

    def animar_muerte(self):
        # Animación de la muerte de Pac-Man
        if self.pacman.animacion_frame < len(ANIMACION_MUERTE):
            sprite_x, sprite_y = ANIMACION_MUERTE[self.pacman.animacion_frame]
            pyxel.cls(0)
            self.bloque.draw()
            pyxel.blt(self.pacman.x, self.pacman.y, 0, sprite_x, sprite_y, 16, 16, colkey=0)
            
            # Cambiar de frame cada cierto número de frames
            if pyxel.frame_count % 5 == 0:
                self.pacman.animacion_frame += 1
        else:
            # Una vez terminada la animación, reiniciar el tablero o marcar el fin del juego
            if self.pacman.vidas > 0:
                self.reiniciar_tablero()
            else:
                self.animacion_muerte_finalizada = True
                self.pacman.en_muerte = False

    #--------------------------------------------------------------------MAPA--------------------------------------------------------------------#

    def dibujar_letras_mapa(self, x, y, sprite):
        # Dibuja textos como READY!, GAME OVER o HIGHSCORE, usando los datos en TEXTO
        sprite = TEXTO[sprite]
        pyxel.blt(x, y, 0, sprite["Coordenadas"][0], sprite["Coordenadas"][1], sprite["Tamaño"][0], sprite["Tamaño"][1], colkey=0)

    def esta_en_zona_prohibida(self, x, y):
        # Verificar si la posición (x, y) está en una zona prohibida
        for lugar in self.puntos.zonas_prohibidas[self.bloque.nivel]:
            x1, y1, x2, y2 = lugar
            if x1 <= x <= x2 and y1 <= y <= y2:
                return True

        # Comprobar también si hay un muro
        if self.bloque.colision(x, y):
            return True
        return False

    def encontrar_celdas_vacias(self):
        # Encuentra celdas vacías donde colocar frutas u otros objetos
        celdas_vacias = []
        for x in range(0, pyxel.width, 16):
            for y in range(0, pyxel.height, 16):
                # Verificar que no haya un punto en esa celda
                punto_encontrado = False
                for p in self.puntos.lista_puntos:
                    if (x, y) == (p[0], p[1]):
                        punto_encontrado = True
                
                # Debe no estar en zona prohibida, no ser la fruta actual ni un regalo
                if (not punto_encontrado and
                    not self.esta_en_zona_prohibida(x, y) and
                    (x, y) != self.puntos.posicion_fruta and
                    (x, y) not in self.puntos.regalos):
                    celdas_vacias.append((x, y))
        return celdas_vacias

    #--------------------------------------------------------------------PUNTOS--------------------------------------------------------------------#

    def generar_puntos(self):
        # Generar los puntos en todas las celdas válidas del mapa
        for x in range(0, pyxel.width, 16):
            for y in range(0, pyxel.height, 16):
                if not self.esta_en_zona_prohibida(x, y) and (x, y) not in self.puntos.regalos:
                    self.puntos.lista_puntos.append((x, y, "BASTON"))

    def generar_fruta(self):
        # Generar una fruta cada 30 segundos, si es posible
        if time.time() - self.puntos.ultimo_tiempo_fruta < 30:
            return False

        objetos_dispo = ["CEREZA", "FRESA", "NARANJA", "MANZANA", "MELON", "PARAGUAS", "CAMPANA", "LLAVE"]
        self.puntos.fruta_actual = random.choice(objetos_dispo)

        celdas_vacias = self.encontrar_celdas_vacias()
        if celdas_vacias:
            self.puntos.posicion_fruta = random.choice(celdas_vacias)
            self.puntos.animacion_activa = True
            self.puntos.animacion_contador = 0
        else:
            self.puntos.posicion_fruta = None

        self.puntos.ultimo_tiempo_fruta = time.time()

    def comprobar_puntos_restantes(self):
        # Comprueba si ya no quedan puntos ni regalos
        if len(self.puntos.lista_puntos) == 0 and len(self.puntos.regalos) == 0:
            return True
        return False

    #--------------------------------------------------------------------FANTASMAS--------------------------------------------------------------------#

    def mover_fantasma_rojo(self, fantasma):
        # Fantasma rojo: persigue a Pac-Man
        if self.victoria or self.pacman.en_muerte:
            return False

        if fantasma.asustado:
            self.alejarse_de_pacman(fantasma)
        else:
            self.seguir_a_pacman(fantasma)

    def mover_fantasma_rosa(self, fantasma):
        # Fantasma rosa: intenta emboscar a Pac-Man
        if self.victoria or self.pacman.en_muerte:
            return False

        if fantasma.asustado:
            self.alejarse_de_pacman(fantasma)
        else:
            # Intentar emboscar a Pac-Man
            posicion_emboscada = self.predecir_posicion_pacman(self.celdas_para_emboscada)
            self.movimiento_emboscada(fantasma, posicion_emboscada)


    def mover_fantasma_azul(self, fantasma):

        if self.victoria or self.pacman.en_muerte:
            return False

        if fantasma.asustado:
            self.alejarse_de_pacman(fantasma)
        else:
            posicion_emboscada = self.predecir_posicion_pacman(self.celdas_para_emboscada)
            self.movimiento_emboscada(fantasma, posicion_emboscada)


    def mover_fantasma_naranja(self, fantasma):
  
        if self.victoria or self.pacman.en_muerte:
            return False

        if fantasma.asustado:
            self.alejarse_de_pacman(fantasma)
        else:
            if time.time() % self.fantasmas_cambio_de_movimiento < 1:
                self.seguir_a_pacman(fantasma)
            else:
                self.alejarse_de_pacman(fantasma)

    #--------------------------------------------------------------------MOVIMIENTO--------------------------------------------------------------------#

    def movimineto_pacman(self):
        # Actualiza la posición de Pac-Man según las teclas presionadas y evita colisiones
        if self.pacman.vidas <= 0 or self.pacman.en_muerte or self.pacman.reiniciando:
            return False

        nueva_x, nueva_y = self.pacman.x, self.pacman.y

        # Leer las teclas para cambiar dirección
        if pyxel.btnp(pyxel.KEY_UP):
            self.pacman.direccion_pendiente = PACMAN_ARRIBA
        elif pyxel.btnp(pyxel.KEY_DOWN):
            self.pacman.direccion_pendiente = PACMAN_ABAJO
        elif pyxel.btnp(pyxel.KEY_LEFT):
            self.pacman.direccion_pendiente = PACMAN_IZQUIERDA
        elif pyxel.btnp(pyxel.KEY_RIGHT):
            self.pacman.direccion_pendiente = PACMAN_DERECHA
        elif pyxel.btnp(pyxel.KEY_W):
            self.pacman.direccion_pendiente = PACMAN_ARRIBA
        elif pyxel.btnp(pyxel.KEY_S):
            self.pacman.direccion_pendiente = PACMAN_ABAJO
        elif pyxel.btnp(pyxel.KEY_A):
            self.pacman.direccion_pendiente = PACMAN_IZQUIERDA
        elif pyxel.btnp(pyxel.KEY_D):
            self.pacman.direccion_pendiente = PACMAN_DERECHA

        # Comprobar si la dirección pendiente se puede usar es decir no hay colisión
        if self.pacman.direccion_pendiente:
            if self.pacman.direccion_pendiente == PACMAN_ARRIBA and not self.bloque.colision(self.pacman.x, self.pacman.y - self.pacman.velocidad):
                self.pacman.direccion_actual = self.pacman.direccion_pendiente
            elif self.pacman.direccion_pendiente == PACMAN_ABAJO and not self.bloque.colision(self.pacman.x, self.pacman.y + self.pacman.velocidad):
                self.pacman.direccion_actual = self.pacman.direccion_pendiente
            elif self.pacman.direccion_pendiente == PACMAN_IZQUIERDA and not self.bloque.colision(self.pacman.x - self.pacman.velocidad, self.pacman.y):
                self.pacman.direccion_actual = self.pacman.direccion_pendiente
            elif self.pacman.direccion_pendiente == PACMAN_DERECHA and not self.bloque.colision(self.pacman.x + self.pacman.velocidad, self.pacman.y):
                self.pacman.direccion_actual = self.pacman.direccion_pendiente

        # Mover Pac-Man en la dirección actual si no hay colisión
        if self.pacman.direccion_actual == PACMAN_ARRIBA:
            nueva_y -= self.pacman.velocidad
        elif self.pacman.direccion_actual == PACMAN_ABAJO:
            nueva_y += self.pacman.velocidad
        elif self.pacman.direccion_actual == PACMAN_IZQUIERDA:
            nueva_x -= self.pacman.velocidad
        elif self.pacman.direccion_actual == PACMAN_DERECHA:
            nueva_x += self.pacman.velocidad

        # Comprobar colisiones con muros
        if not self.bloque.colision(nueva_x, self.pacman.y):
            self.pacman.x = nueva_x
        if not self.bloque.colision(self.pacman.x, nueva_y):
            self.pacman.y = nueva_y

        # Portales: si Pac-Man entra en un portal, salir por el otro lado del mapa
        if (self.pacman.x, self.pacman.y) in PORTALES:
            self.pacman.x, self.pacman.y = PORTALES[(self.pacman.x, self.pacman.y)]

        print("Pacman", self.pacman.x, self.pacman.y)

    def seguir_a_pacman(self, fantasma):
        # El fantasma busca una ruta simple hacia la posición de Pac-Man
        if fantasma.siguiente_celda is None or (fantasma.x == fantasma.siguiente_celda[0] and fantasma.y == fantasma.siguiente_celda[1]):
            inicio = (fantasma.x // 16 * 16, fantasma.y // 16 * 16)
            objetivo = (self.pacman.x // 16 * 16, self.pacman.y // 16 * 16)
            ruta = self.buscar_ruta_simple(inicio, objetivo)

            if ruta and len(ruta) > 1:
                fantasma.siguiente_celda = ruta[1]
            else:
                fantasma.siguiente_celda = None

        self.mover_hacia_siguiente_celda(fantasma)

    def alejarse_de_pacman(self, fantasma):
        # El fantasma busca una celda cercana que lo aleje de Pac-Man
        if fantasma.siguiente_celda is None or (fantasma.x == fantasma.siguiente_celda[0] and fantasma.y == fantasma.siguiente_celda[1]):
            inicio = (fantasma.x // 16 * 16, fantasma.y // 16 * 16)
            pacman_pos = (self.pacman.x // 16 * 16, self.pacman.y // 16 * 16)

            opciones = []
            for dx, dy in [(-16, 0), (16, 0), (0, -16), (0, 16)]:
                posible_celda = (inicio[0] + dx, inicio[1] + dy)
                if not self.colision_fantasmas(posible_celda[0], posible_celda[1]):
                    distancia = abs(posible_celda[0] - pacman_pos[0]) + abs(posible_celda[1] - pacman_pos[1])
                    opciones.append((distancia, posible_celda))

            if opciones:
                mayor_distancia = -1
                mejor_celda = None
                for distancia, celda in opciones:
                    if distancia > mayor_distancia:
                        mayor_distancia = distancia
                        mejor_celda = celda
                fantasma.siguiente_celda = mejor_celda
            else:
                fantasma.siguiente_celda = None

        self.mover_hacia_siguiente_celda(fantasma)

    
    def predecir_posicion_pacman(self, casillas_adelante):
        # Predecir la posición futura de Pac-Man según su dirección y un número de celdas
        dx, dy = 0, 0
        if self.pacman.direccion_actual == PACMAN_ARRIBA:
            dy = -16 * casillas_adelante
        elif self.pacman.direccion_actual == PACMAN_ABAJO:
            dy = 16 * casillas_adelante
        elif self.pacman.direccion_actual == PACMAN_IZQUIERDA:
            dx = -16 * casillas_adelante
        elif self.pacman.direccion_actual == PACMAN_DERECHA:
            dx = 16 * casillas_adelante

        pos_futura = ((self.pacman.x // 16) * 16 + dx, (self.pacman.y // 16) * 16 + dy)
        return pos_futura

    def movimiento_emboscada(self, fantasma, objetivo):
        # Mover el fantasma rosa hacia la posición emboscada o hacia Pac-Man si no hay ruta
        if fantasma.siguiente_celda is None or (fantasma.x == fantasma.siguiente_celda[0] and fantasma.y == fantasma.siguiente_celda[1]):
            inicio = (fantasma.x // 16 * 16, fantasma.y // 16 * 16)
            ruta = self.buscar_ruta_simple(inicio, objetivo)

            if ruta and len(ruta) > 1:
                fantasma.siguiente_celda = ruta[1]
            else:
                # Si no hay ruta a la emboscada, seguir a Pac-Man directamente
                objetivo_pacman = (self.pacman.x // 16 * 16, self.pacman.y // 16 * 16)
                ruta = self.buscar_ruta_simple(inicio, objetivo_pacman)
                if ruta and len(ruta) > 1:
                    fantasma.siguiente_celda = ruta[1]
                else:
                    fantasma.siguiente_celda = None

        self.mover_hacia_siguiente_celda(fantasma)


    def mover_hacia_siguiente_celda(self, fantasma):
        # Mueve el fantasma hacia la siguiente celda de su ruta
        if fantasma.siguiente_celda:
            dx = fantasma.siguiente_celda[0] - fantasma.x
            dy = fantasma.siguiente_celda[1] - fantasma.y

            if dx > 0:
                fantasma.x += min(fantasma.velocidad, dx)
                fantasma.direccion_actual = "DERECHA"
            elif dx < 0:
                fantasma.x += max(-fantasma.velocidad, dx)
                fantasma.direccion_actual = "IZQUIERDA"
            elif dy > 0:
                fantasma.y += min(fantasma.velocidad, dy)
                fantasma.direccion_actual = "ABAJO"
            elif dy < 0:
                fantasma.y += max(-fantasma.velocidad, dy)
                fantasma.direccion_actual = "ARRIBA"


            # Si el fantasma llega a una posición que es un portal se hace tp
            if (fantasma.x, fantasma.y) in PORTALES:
                fantasma.x, fantasma.y = PORTALES[(fantasma.x, fantasma.y)]

    def buscar_ruta_simple(self, inicio, objetivo):
        # Búsqueda en anchura para encontrar una ruta simple entre inicio y objetivo
        # Se limita el número de pasos para evitar que se cuelgue
        max_pasos = 1000
        cola = deque([inicio])
        visitados = {inicio: None}
        pasos = 0

        while cola:
            actual = cola.popleft()
            pasos += 1

            if pasos > max_pasos:
                # Si excede el número máximo de pasos, abandonar la búsqueda para evitar que vaya lento el juego
                return None

            if actual == objetivo:
                # Si se encontró el objetivo buscar la ruta
                ruta = []
                while actual is not None:
                    ruta.append(actual)
                    actual = visitados[actual]
                ruta.reverse()
                return ruta

            for dx, dy in [(-16, 0), (16, 0), (0, -16), (0, 16)]:
                posible_celda = (actual[0] + dx, actual[1] + dy)
                if posible_celda not in visitados and not self.bloque.colision(posible_celda[0], posible_celda[1]):
                    visitados[posible_celda] = actual
                    cola.append(posible_celda)

        return None

    #--------------------------------------------------------------------COLISIONES--------------------------------------------------------------------#

    def colision_fantasmas_con_pacman(self):
        # Comprobar si algún fantasma colisiona con Pac-Man
        if self.pacman.en_muerte or self.pacman.reiniciando or self.pacman.vidas <= 0:
            return False

        pacman_x = self.pacman.x + 8
        pacman_y = self.pacman.y + 8

        for fantasma in self.fantasmas:
            fantasma_x = fantasma.x + 8
            fantasma_y = fantasma.y + 8

            # Si la distancia es pequeña, hay colisión
            if abs(pacman_x - fantasma_x) < 16 and abs(pacman_y - fantasma_y) < 16:
                if fantasma.asustado:
                    # Si el fantasma está asustado, Pac-Man lo come y gana 200 puntos
                    self.puntos.puntos += 200
                    self.fantasmas_comido = True
                    self.pacman.mostrar_puntos = True
                    self.pacman.texto_tiempo_inicio = time.time()
                    self.pacman.posicion_fantasma_comido_x, self.pacman.posicion_fantasma_comido_y = self.pacman.x, self.pacman.y
                    fantasma.volver_a_trampa()
                    return True
                else:
                    # Si el fantasma no está asustado, Pac-Man pierde una vida
                    self.pacman.perder_vida()
                    return True
        return False

    def colision_fantasmas(self, x, y):
        # Comprobar si una posición (x, y) colisiona con muros o zonas prohibidas para el fantasma
        puerta_x, puerta_y = PUERTA_SALIDA
        sprite_tamaño = self.bloque.celda_tamaño

        # Permitir pasar por la puerta de la trampa
        if puerta_x <= x < puerta_x + sprite_tamaño and puerta_y <= y < puerta_y + sprite_tamaño:
            return False

        if self.bloque.colision(x, y):
            return True

        if self.esta_en_zona_prohibida(x, y):
            return True

        return False

    def detectar_colision_puntos(self, pacman_x, pacman_y, punto_x, punto_y):
        # Detecta si Pac-Man ha comido un punto
        return abs(pacman_x - punto_x) < 10 and abs(pacman_y - punto_y) < 10

    def comer_puntos(self):
        # Comprueba si Pac-Man ha comido puntos o regalos
        puntos_sin_comer = []
        for x, y, tipo in self.puntos.lista_puntos:
            if self.detectar_colision_puntos(self.pacman.x, self.pacman.y, x, y):
                self.puntos.puntos += OBJETOS[tipo]["Puntos"]
            else:
                puntos_sin_comer.append((x, y, tipo))
        self.puntos.lista_puntos = puntos_sin_comer

        regalos_sin_comer = []
        for x, y in self.puntos.regalos:
            if self.detectar_colision_puntos(self.pacman.x, self.pacman.y, x, y):
                # Comer un regalo hace que los fantasmas se pongan asustados
                for fantasma in self.fantasmas:
                    fantasma.activar_asustado()
                self.puntos.puntos += OBJETOS["REGALO"]["Puntos"]
            else:
                regalos_sin_comer.append((x, y))
        self.puntos.regalos = regalos_sin_comer

    def comer_fruta(self):
        # Comprueba si Pac-Man ha comido la fruta
        if self.puntos.posicion_fruta and self.detectar_colision_puntos(self.pacman.x, self.pacman.y, self.puntos.posicion_fruta[0], self.puntos.posicion_fruta[1]):
            self.puntos.puntos += OBJETOS[self.puntos.fruta_actual]["Puntos"]
            self.puntos.posicion_fruta = None
            self.puntos.fruta_actual = None


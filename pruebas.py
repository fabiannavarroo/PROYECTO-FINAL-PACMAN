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
        # Inicializar la ventana del juego con Pyxel
        pyxel.init(400, 400, title="Pacman", fps=30)  # Crear la pantalla
        pyxel.load("assets/recursos.pyxres")  # Cargar recursos gráficos
        pyxel.playm(0,0,True)

        # Inicializar elementos del juego
        self.bloque = Bloque()  # Mapa del juego
        self.pacman = Pacman(192, 304)  # Pacman y su posición inicial
        self.fantasmas = [
            FantasmaRojo(160, 208),
            FantasmaRosa(181, 176),
            FantasmaAzul(203, 208),
            FantasmaNaranja(225, 208),
        ]
        self.puntos = Puntos(OBJETOS)  # Puntos y frutas

        # Generar los puntos en el mapa
        self.generar_puntos()

        self.mostrar_ready = True
        self.contador_ready = 0

        self.contador_game_over = 0
        self.mostrar_fin = False

        self.animacion_muerte_finalizada = False
        self.victoria = False
        self.celdas_para_emboscada = 6

        # Caché de rutas
        self.rutas_cache = {}
        # Control de frecuencia de cálculo de ruta
        self.ultimo_calculo_ruta = pyxel.frame_count
        self.intervalo_calculo_ruta = 10  # Sólo recalcular cada 10 frames

        pyxel.run(self.update, self.draw)

    def update(self):
        if self.pacman.vidas > 0:  # Mientras Pacman tenga vidas
            if self.contador_ready < 90:
                self.contador_ready += 1 
                if self.contador_ready == 90:
                    self.mostrar_ready = False

            if not self.pacman.en_muerte:
                self.movimineto_pacman()
                self.comer_puntos()
                self.comer_fruta()
                self.generar_fruta()

                for index, fantasma in enumerate(self.fantasmas):
                    if fantasma.en_trampa():
                        tiempo_espera = (index + 1) * 2
                        if time.time() - fantasma.tiempo_trampa >= tiempo_espera:
                            fantasma.salir_de_trampa()
                    else:
                        if isinstance(fantasma, FantasmaRojo):
                            self.mover_fantasma_rojo(fantasma)
                        elif isinstance(fantasma, FantasmaRosa):
                            self.mover_fantasma_rosa(fantasma)
                        elif isinstance(fantasma, FantasmaAzul):
                            self.mover_fantasma_azul(fantasma)
                        elif isinstance(fantasma, FantasmaNaranja):
                            self.mover_fantasma_naranja(fantasma)

                    fantasma.actualizar_estado()

                self.colision_fantasmas_con_pacman()

                if self.comprobar_puntos_restantes():
                    if self.bloque.nivel + 1 in self.bloque.mapas:
                        self.bloque.nivel += 1
                        self.bloque.cargar_mapa()
                        self.reiniciar_puntos()
                        self.reiniciar_tablero()
                    else:
                        self.victoria = True
            else:
                self.animar_muerte()

        else:
            if not self.animacion_muerte_finalizada:
                self.animar_muerte()
                if self.pacman.animacion_frame >= len(ANIMACION_MUERTE):
                    self.animacion_muerte_finalizada = True
            else:
                self.contador_game_over += 1

    def draw(self):
        pyxel.cls(0)
        self.dibujar_letras_mapa(120,16, "HIGHSCORE")
        self.puntos.ver_puntuacion(195,16)
        if self.pacman.vidas > 0:
            self.bloque.draw()
            if self.pacman.en_muerte:
                self.animar_muerte()
            else:
                self.puntos.draw()
                self.pacman.ver_vidas(10, 10)
                self.pacman.draw()
                for fantasma in self.fantasmas:
                    fantasma.draw()
                
                if self.mostrar_ready:
                    self.animar_ready()

                if self.pacman.mostrar_puntos and time.time() - self.pacman.texto_tiempo_inicio < 1.5:
                    pyxel.text(self.pacman.posicion_fantasma_comido_x, self.pacman.posicion_fantasma_comido_y, "+200 puntos", pyxel.COLOR_RED)
                else:
                    self.pacman.mostrar_puntos = False

            if self.victoria:
                pyxel.cls(0)
                self.bloque.draw()
        else:
            pyxel.cls(0)
            self.bloque.draw()
            self.animar_muerte()
            self.animar_fin()

    #--------------------------------------------------------------------REINICIO--------------------------------------------------------------------#

    def reiniciar_fantasmas(self):
        for fantasma in self.fantasmas:
            fantasma.volver_a_posicion_inicial()
            fantasma.siguiente_celda = None
            fantasma.tiempo_trampa = time.time()

    def reiniciar_tablero(self):
        self.mostrar_ready = True
        self.contador_ready = 0
        self.bloque.cargar_mapa()
        self.reiniciar_posiciones()
        self.pacman.en_muerte = False
        self.pacman.animacion_frame = 0

    def reiniciar_posiciones(self):
        self.pacman.x, self.pacman.y = 192, 304
        for fantasma in self.fantasmas:
            fantasma.volver_a_posicion_inicial()
        self.pacman.reiniciando = False

    def reiniciar_puntos(self):
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
        if self.contador_ready < 90:
            if (self.contador_ready // 10) % 2 == 0:
                self.dibujar_letras_mapa(180,240,"READY!")
            else:
                pyxel.blt(180, 245, 2, 0, 0, 0, 0, colkey=0)
        else:
            pyxel.blt(180, 245, 2, 0, 0, 0, 0, colkey=0)

    def animar_fin(self):
        if self.contador_game_over < 70:
            if (self.contador_game_over // 10) % 2 == 0:
                self.dibujar_letras_mapa(185,208,"GAME OVER")
            else:
                pyxel.blt(180, 245, 2, 0, 0, 0, 0, colkey=0)
        else:
            self.dibujar_letras_mapa(185,208,"GAME OVER")

    def animar_muerte(self):
        if self.pacman.animacion_frame < len(ANIMACION_MUERTE):
            sprite_x, sprite_y = ANIMACION_MUERTE[self.pacman.animacion_frame]
            pyxel.cls(0)
            self.bloque.draw()
            pyxel.blt(self.pacman.x, self.pacman.y, 0, sprite_x, sprite_y, 16, 16, colkey=0)
            
            if pyxel.frame_count % 5 == 0:
                self.pacman.animacion_frame += 1
        else:
            if self.pacman.vidas > 0:
                self.reiniciar_tablero()
            else:
                self.animacion_muerte_finalizada = True
                self.pacman.en_muerte = False

    #--------------------------------------------------------------------MAPA--------------------------------------------------------------------#

    def dibujar_letras_mapa(self, x, y, sprite):
        sprite = TEXTO[sprite]
        pyxel.blt(x, y, 0, sprite["Coordenadas"][0], sprite["Coordenadas"][1], sprite["Tamaño"][0], sprite["Tamaño"][1], colkey=0)

    def esta_en_zona_prohibida(self, x, y):
        for lugar in self.puntos.zonas_prohibidas[self.bloque.nivel]:
            x1, y1, x2, y2 = lugar
            if x1 <= x <= x2 and y1 <= y <= y2:  
                return True

        if self.bloque.colision(x, y):
            return True
        return False

    def encontrar_celdas_vacias(self):
        celdas_vacias = []
        for x in range(0, pyxel.width, 16):
            for y in range(0, pyxel.height, 16):
                punto_encontrado = False
                for p in self.puntos.lista_puntos:
                    if (x, y) == (p[0], p[1]):
                        punto_encontrado = True
                        break
                
                if (not punto_encontrado and
                    not self.esta_en_zona_prohibida(x, y) and
                    (x, y) != self.puntos.posicion_fruta and
                    (x, y) not in self.puntos.regalos):
                    celdas_vacias.append((x, y))
        return celdas_vacias

    #--------------------------------------------------------------------PUNTOS--------------------------------------------------------------------#

    def generar_puntos(self):
        for x in range(0, pyxel.width, 16):
            for y in range(0, pyxel.height, 16):
                if not self.esta_en_zona_prohibida(x, y) and (x, y) not in self.puntos.regalos:
                    self.puntos.lista_puntos.append((x, y, "BASTON"))

    def generar_fruta(self):
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
        if len(self.puntos.lista_puntos) == 0 and len(self.puntos.regalos) == 0:
            return True
        return False

    #--------------------------------------------------------------------FANTASMAS--------------------------------------------------------------------#

    def mover_fantasma_rojo(self, fantasma):
        if self.victoria or self.pacman.en_muerte:
            return False

        if fantasma.asustado:
            self.alejarse_de_pacman(fantasma)
        else:
            self.seguir_a_pacman(fantasma)

    def mover_fantasma_rosa(self, fantasma):
        if self.victoria or self.pacman.en_muerte:
            return False

        if fantasma.asustado:
            self.alejarse_de_pacman(fantasma)
        else:
            posicion_emboscada = self.predecir_posicion_pacman(self.celdas_para_emboscada)
            self.movimiento_emboscada(fantasma, posicion_emboscada)

    def predecir_posicion_pacman(self, casillas_adelante):
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
        if fantasma.siguiente_celda is None or (fantasma.x == fantasma.siguiente_celda[0] and fantasma.y == fantasma.siguiente_celda[1]):
            inicio = (fantasma.x // 16 * 16, fantasma.y // 16 * 16)

            ruta = self.buscar_ruta_simple(inicio, objetivo)
            if ruta and len(ruta) > 1:
                fantasma.siguiente_celda = ruta[1]
            else:
                objetivo_pacman = (self.pacman.x // 16 * 16, self.pacman.y // 16 * 16)
                ruta = self.buscar_ruta_simple(inicio, objetivo_pacman)
                if ruta and len(ruta) > 1:
                    fantasma.siguiente_celda = ruta[1]
                else:
                    fantasma.siguiente_celda = None

        self.mover_hacia_siguiente_celda(fantasma)

    def mover_fantasma_azul(self, fantasma):
        if self.victoria or self.pacman.en_muerte:
            return False

        if fantasma.asustado:
            self.alejarse_de_pacman(fantasma)
        else:
            pass

    def mover_fantasma_naranja(self, fantasma):
        if self.victoria or self.pacman.en_muerte:
            return False

        if fantasma.asustado:
            self.alejarse_de_pacman(fantasma)
        else:
            pass

    #--------------------------------------------------------------------MOVIMIENTO--------------------------------------------------------------------#

    def movimineto_pacman(self):
        if self.pacman.vidas <= 0 or self.pacman.en_muerte or self.pacman.reiniciando:
            return False

        nueva_x, nueva_y = self.pacman.x, self.pacman.y

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

        if self.pacman.direccion_pendiente:
            if self.pacman.direccion_pendiente == PACMAN_ARRIBA and not self.bloque.colision(self.pacman.x, self.pacman.y - self.pacman.velocidad):
                self.pacman.direccion_actual = self.pacman.direccion_pendiente
            elif self.pacman.direccion_pendiente == PACMAN_ABAJO and not self.bloque.colision(self.pacman.x, self.pacman.y + self.pacman.velocidad):
                self.pacman.direccion_actual = self.pacman.direccion_pendiente
            elif self.pacman.direccion_pendiente == PACMAN_IZQUIERDA and not self.bloque.colision(self.pacman.x - self.pacman.velocidad, self.pacman.y):
                self.pacman.direccion_actual = self.pacman.direccion_pendiente
            elif self.pacman.direccion_pendiente == PACMAN_DERECHA and not self.bloque.colision(self.pacman.x + self.pacman.velocidad, self.pacman.y):
                self.pacman.direccion_actual = self.pacman.direccion_pendiente

        if self.pacman.direccion_actual == PACMAN_ARRIBA:
            nueva_y -= self.pacman.velocidad
        elif self.pacman.direccion_actual == PACMAN_ABAJO:
            nueva_y += self.pacman.velocidad
        elif self.pacman.direccion_actual == PACMAN_IZQUIERDA:
            nueva_x -= self.pacman.velocidad
        elif self.pacman.direccion_actual == PACMAN_DERECHA:
            nueva_x += self.pacman.velocidad

        if not self.bloque.colision(nueva_x, self.pacman.y):
            self.pacman.x = nueva_x
        if not self.bloque.colision(self.pacman.x, nueva_y):
            self.pacman.y = nueva_y

        if (self.pacman.x, self.pacman.y) in PORTALES:
            self.pacman.x, self.pacman.y = PORTALES[(self.pacman.x, self.pacman.y)]

    def seguir_a_pacman(self, fantasma):
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

    def mover_hacia_siguiente_celda(self, fantasma):
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

    def buscar_ruta_simple(self, inicio, objetivo):
        # No recalcular rutas con demasiada frecuencia
        if pyxel.frame_count - self.ultimo_calculo_ruta < self.intervalo_calculo_ruta:
            # Demasiado pronto para recalcular, si no tenemos cache, no hacemos nada
            key = (inicio, objetivo)
            return self.rutas_cache.get(key, None)

        if inicio == objetivo:
            return [inicio]

        key = (inicio, objetivo)
        if key in self.rutas_cache:
            return self.rutas_cache[key]

        cola = deque([inicio])
        visitados = {inicio: None}

        while cola:
            actual = cola.popleft()

            if actual == objetivo:
                ruta = []
                while actual is not None:
                    ruta.append(actual)
                    actual = visitados[actual]
                ruta.reverse()
                self.rutas_cache[key] = ruta
                self.ultimo_calculo_ruta = pyxel.frame_count
                return ruta

            for dx, dy in [(-16, 0), (16, 0), (0, -16), (0, 16)]:
                posible_celda = (actual[0] + dx, actual[1] + dy)
                if posible_celda not in visitados and not self.bloque.colision(posible_celda[0], posible_celda[1]):
                    visitados[posible_celda] = actual
                    cola.append(posible_celda)

        # No hay ruta
        self.rutas_cache[key] = None
        self.ultimo_calculo_ruta = pyxel.frame_count
        return None

    #--------------------------------------------------------------------COLISIONES--------------------------------------------------------------------#

    def colision_fantasmas_con_pacman(self):
        if self.pacman.en_muerte or self.pacman.reiniciando or self.pacman.vidas <= 0:
            return False

        pacman_x = self.pacman.x + 8
        pacman_y = self.pacman.y + 8

        for fantasma in self.fantasmas:
            fantasma_x = fantasma.x + 8
            fantasma_y = fantasma.y + 8

            if abs(pacman_x - fantasma_x) < 16 and abs(pacman_y - fantasma_y) < 16:
                if fantasma.asustado:
                    self.puntos.puntos += 200
                    self.fantasmas_comido = True
                    self.pacman.mostrar_puntos = True
                    self.pacman.texto_tiempo_inicio = time.time()
                    self.pacman.posicion_fantasma_comido_x, self.pacman.posicion_fantasma_comido_y = self.pacman.x, self.pacman.y
                    fantasma.volver_a_trampa()
                    return True
                else:
                    self.pacman.perder_vida()
                    return True
        return False

    def colision_fantasmas(self, x, y):
        puerta_x, puerta_y = PUERTA_SALIDA
        sprite_tamaño = self.bloque.celda_tamaño

        if puerta_x <= x < puerta_x + sprite_tamaño and puerta_y <= y < puerta_y + sprite_tamaño:
            return False

        if self.bloque.colision(x, y):
            return True

        if self.esta_en_zona_prohibida(x, y):
            return True

        return False

    def detectar_colision_puntos(self, pacman_x, pacman_y, punto_x, punto_y):
        return abs(pacman_x - punto_x) < 10 and abs(pacman_y - punto_y) < 10

    def comer_puntos(self):
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
                for fantasma in self.fantasmas:
                    fantasma.activar_asustado()
                self.puntos.puntos += OBJETOS["REGALO"]["Puntos"]
            else:
                regalos_sin_comer.append((x, y))
        self.puntos.regalos = regalos_sin_comer

    def comer_fruta(self):
        if self.puntos.posicion_fruta and self.detectar_colision_puntos(self.pacman.x, self.pacman.y, self.puntos.posicion_fruta[0], self.puntos.posicion_fruta[1]):
            self.puntos.puntos += OBJETOS[self.puntos.fruta_actual]["Puntos"]
            self.puntos.posicion_fruta = None
            self.puntos.fruta_actual = None


Tablero()
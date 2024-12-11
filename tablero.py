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
        pyxel.init(400, 400, title="Pacman", fps=30)
        pyxel.load("assets/recursos.pyxres")
        pyxel.playm(0,0,True)

        self.bloque = Bloque()
        self.pacman = Pacman(192, 304)
        self.fantasmas = [
            FantasmaRojo(160, 208),
            FantasmaRosa(181, 208),
            FantasmaAzul(203, 208),
            FantasmaNaranja(225, 208),
        ]
        self.puntos = Puntos(OBJETOS)
        self.generar_puntos()

        self.mostrar_ready = True
        self.contador_ready = 0
        self.contador_game_over = 0
        self.mostrar_fin = False
        self.animacion_muerte_finalizada = False
        self.victoria = False
        self.celdas_para_emboscada = 4
        self.fantasmas_cambio_de_movimiento = 20

        pyxel.run(self.update, self.draw)

    def update(self):

        if self.pacman.vidas > 0:
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
                self.colision_fantasmas(fantasma.x, fantasma.y)

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
        self.dibujar_letras_mapa(120,16,"HIGHSCORE")
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

    def dibujar_letras_mapa(self, x, y, sprite):
        sprite = TEXTO[sprite]
        pyxel.blt(x, y, 0, sprite["Coordenadas"][0], sprite["Coordenadas"][1],
                  sprite["Tamaño"][0], sprite["Tamaño"][1], colkey=0)

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

                if (not punto_encontrado and
                    not self.esta_en_zona_prohibida(x, y) and
                    (x, y) != self.puntos.posicion_fruta and
                    (x, y) not in self.puntos.regalos):
                    celdas_vacias.append((x, y))
        return celdas_vacias

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

    def mover_fantasma_rojo(self, fantasma):
        if self.victoria or self.pacman.en_muerte:
            return False

        if fantasma.asustado and not fantasma.en_trampa():
            self.movimiento_simple(fantasma, modo="alejar")
        else:
            self.movimiento_simple(fantasma, modo="seguir")

    def mover_fantasma_rosa(self, fantasma):
        if self.victoria or self.pacman.en_muerte:
            return False

        if fantasma.asustado and not fantasma.en_trampa():
            self.movimiento_simple(fantasma, modo="alejar")
        else:
            objetivo = self.predecir_posicion_pacman(self.celdas_para_emboscada)
            self.movimiento_simple(fantasma, modo="posicion", objetivo=objetivo)

    def mover_fantasma_azul(self, fantasma):
        if self.victoria or self.pacman.en_muerte:
            return False

        if not fantasma.en_trampa():
            if time.time() - fantasma.ultimo_cambio_modo >= 10:
                if random.random() < 0.5:
                    pass
                else:
                    fantasma.modo_perseguir = not fantasma.modo_perseguir
                fantasma.ultimo_cambio_modo = time.time()

        if fantasma.asustado and not fantasma.en_trampa():
            self.movimiento_simple(fantasma, modo="alejar")
        else:
            if fantasma.modo_perseguir:
                objetivo = self.predecir_posicion_pacman(self.celdas_para_emboscada)
                self.movimiento_simple(fantasma, modo="posicion", objetivo=objetivo)
            else:
                if not fantasma.en_trampa():
                    self.movimiento_simple(fantasma, modo="alejar")

    def mover_fantasma_naranja(self, fantasma):
        if self.victoria or self.pacman.en_muerte:
            return False

        if not fantasma.en_trampa():
            if time.time() - fantasma.ultimo_cambio_modo >= 10:
                if random.random() < 0.5:
                    pass
                else:
                    fantasma.modo_perseguir = not fantasma.modo_perseguir
                fantasma.ultimo_cambio_modo = time.time()

        if fantasma.asustado and not fantasma.en_trampa():
            self.movimiento_simple(fantasma, modo="alejar")
        else:
            if fantasma.modo_perseguir:
                self.movimiento_simple(fantasma, modo="seguir")
            else:
                if not fantasma.en_trampa():
                    self.movimiento_simple(fantasma, modo="alejar")

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

        print("Pacman", self.pacman.x, self.pacman.y)

    def movimiento_simple(self, fantasma, modo="seguir", objetivo=None):
        if objetivo is None:
            if modo == "seguir":
                objetivo = (self.pacman.x, self.pacman.y)
            elif modo == "alejar":
                px, py = self.pacman.x, self.pacman.y
                fx, fy = fantasma.x, fantasma.y
                objetivo = (fx - (px - fx), fy - (py - fy))
            else:
                objetivo = (self.pacman.x, self.pacman.y)

        fx, fy = fantasma.x, fantasma.y
        ox, oy = objetivo

        direcciones = [("ARRIBA",0,-fantasma.velocidad),
                       ("ABAJO",0,fantasma.velocidad),
                       ("IZQUIERDA",-fantasma.velocidad,0),
                       ("DERECHA",fantasma.velocidad,0)]

        opuesta = {"ARRIBA":"ABAJO","ABAJO":"ARRIBA","IZQUIERDA":"DERECHA","DERECHA":"IZQUIERDA"}
        direcciones = [d for d in direcciones if opuesta.get(fantasma.direccion_actual,"") != d[0]]

        def distancia(a,b,c,d):
            return abs(a-c)+abs(b-d)

        def nuevo_dist(dx,dy):
            return distancia(fx+dx, fy+dy, ox, oy)

        if modo in ["seguir","posicion"]:
            direcciones.sort(key=lambda d: nuevo_dist(d[1],d[2]))
        elif modo == "alejar":
            direcciones.sort(key=lambda d: nuevo_dist(d[1],d[2]), reverse=True)

        movido = False
        for dir_name,ddx,ddy in direcciones:
            nx, ny = fx+ddx, fy+ddy
            if not self.colision_fantasmas(nx, ny):
                fantasma.x, fantasma.y = nx, ny
                fantasma.direccion_actual = dir_name
                movido = True
                break

        if not movido:
            for dir_name,ddx,ddy in [("ARRIBA",0,-fantasma.velocidad),
                                     ("ABAJO",0,fantasma.velocidad),
                                     ("IZQUIERDA",-fantasma.velocidad,0),
                                     ("DERECHA",fantasma.velocidad,0)]:
                nx, ny = fx+ddx, fy+ddy
                if not self.colision_fantasmas(nx, ny):
                    fantasma.x, fantasma.y = nx, ny
                    fantasma.direccion_actual = dir_name
                    break

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
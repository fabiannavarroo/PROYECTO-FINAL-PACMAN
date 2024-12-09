from constantes import *
import random
import time
import pyxel


class Puntos:
    def __init__(self, sprite, pacman, fantasmas, bloque):
        self.sprite = sprite
        self.pacman = pacman
        self.fantasmas = fantasmas
        self.bloque = bloque
        self.puntos = 0
        self.puntos_alcanzados = 0  # Rango de 500 en 500 de la última meta alcanzada de puntos
        self.color_actual = NUMEROS_BLANCOS  # Color inicial de los números
        self.ultimo_tiempo_fruta = time.time()  # Tiempo de la última fruta generada
        self.fruta_actual = None  # Información de la fruta actual
        self.posicion_fruta = None  # Posición actual de la fruta
        self.animacion_activa = False  # Indica si hay animación activa
        self.animacion_contador = 0  # Contador para animación de aparición
        self.zonas_prohibidas = ZONAS_PROHIBIDAS
        self.regalos = [(16, 304), (368, 304), (16, 80),(368, 80)] # Coordenadas fijas de los regalos
        self.lista_puntos = [] # Lista de puntos generados
        self.generar_puntos()
        self.lista_frutas = [] # Lista de frutas generadas


    def draw(self):
        # Dibuja los puntos, frutas y regalos en el mapa.
        # Dibujar puntos
        for x, y, tipo in self.lista_puntos:
            sprite = OBJETOS[tipo]["Coordenadas"]
            pyxel.blt(x, y, 0, sprite[0], sprite[1], 16, 16, colkey=0)

        # Dibujar fruta actual
        if self.posicion_fruta and self.fruta_actual:
            if self.animacion_activa and self.animacion_contador < 30:
                # Parpadea cada 5 frames
                if self.animacion_contador// REFRESH % 2 == 0:
                    sprite = OBJETOS[self.fruta_actual]["Coordenadas"]
                    pyxel.blt(self.posicion_fruta[0], self.posicion_fruta[1], 0, sprite[0], sprite[1], 16, 16, colkey=0)
                self.animacion_contador += 1
            else:
                # Detiene la animación y dibuja la fruta
                self.animacion_activa = False
                sprite = OBJETOS[self.fruta_actual]["Coordenadas"]
                pyxel.blt(self.posicion_fruta[0], self.posicion_fruta[1], 0, sprite[0], sprite[1], 16, 16, colkey=0)
            

        # Dibujar regalos
        for x, y in self.regalos:
            if pyxel.frame_count // REFRESH_REGALOS % 2:
                coord = OBJETOS["REGALO_BRILLANTE"]["Coordenadas"]
                pyxel.blt(x, y, 0, coord[0], coord[1], 16, 16, colkey=0)
            else:
                coord = OBJETOS["REGALO"]["Coordenadas"]
                pyxel.blt(x, y, 0, coord[0], coord[1], 16, 16, colkey=0)

        # Dibuja las letras
        self.dibujar_letras_mapa(120,16, "HIGHSCORE")

        # Mostrar la puntuación
        self.ver_puntuacion(195, 16)


    def reiniciar_puntos(self):
        # Reinica los puntos
        self.regalos = [(16, 304), (368, 304), (16, 80),(368, 80)] # Coordenadas de los regalos
        self.lista_puntos = [] # Lista de puntos generados
        self.generar_puntos()
        self.ultimo_tiempo_fruta = time.time()  # Tiempo de la última fruta generada
        self.fruta_actual = None  # Información de la fruta actual
        self.posicion_fruta = None  # Posición actual de la fruta
        self.animacion_activa = False  # Indica si hay animación activa
        self.animacion_contador = 0




    
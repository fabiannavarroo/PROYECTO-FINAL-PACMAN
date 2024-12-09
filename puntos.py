from constantes import *
import random
import time
import pyxel


class Puntos:
    def __init__(self, sprite):
        self.sprite = sprite
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


    def ver_puntuacion(self, x, y):
        # Cambia el color solo cuando se supera un nuevo múltiplo de 500
        colores_dispo = [NUMEROS_BLANCOS, NUMEROS_MORADOS, NUMEROS_NARANJAS, NUMEROS_VERDES]
        if self.puntos // 500 > self.puntos_alcanzados:
            self.puntos_alcanzados = self.puntos // 500  # Actualiza los puntos alcanzados
            self.color_actual = random.choice(colores_dispo)  # Elige un nuevo color aleatorio

        color_numeros = self.color_actual
        puntuacion_str = str(self.puntos)
        pos_x = x

        for num in puntuacion_str:
            num = int(num)
            sprite = color_numeros[str(num)]
            sprite_x, sprite_y = sprite["Coordenadas"]
            sprite_w, sprite_h = sprite["Tamaño"]

            pyxel.blt(
                pos_x, y,
                0, sprite_x, sprite_y, sprite_w, sprite_h, colkey=0
            )
            pos_x += sprite_w + 1  # Espacio entre los numeros






    
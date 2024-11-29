from constantes import *
import random
import time
from muro import Muro
import pyxel


class Puntos:
    def __init__(self, muro, sprite, pacman):
        self.muro = muro
        self.sprite = sprite
        self.pacman = pacman
        self.puntos = 0
        self.puntos_alcanzados = 0  # Rango de 500 en 500 de la última meta alcanzada de puntos
        self.color_actual = NUMEROS_BLANCOS  # Color inicial de los números
        self.ultimo_tiempo_fruta = time.time()  # Marca de tiempo de la última fruta
        self.fruta_actual = None  # Información de la fruta actual
        self.posicion_actual = None  # Posición actual de la fruta
        self.posicion_destino = None  # Posición destino de la fruta


    def draw(self):
        # Poner los puntos en el mapa
        for y in range(len(self.muro.mapa)):
            for x in range(len(self.muro.mapa[y])):
                if self.muro.mapa[y][x] == 0:
                    sprite = OBJETOS["BASTON"]
                    sprite_x, sprite_y = sprite["Coordenadas"]
                    sprite_w, sprite_h = 16, 16  # Ancho y largo del sprite
                    pyxel.blt(
                        x * self.muro.celda_tamaño, y * self.muro.celda_tamaño,  # Coordenadas donde se dibuja el punto
                        0,  # Banco de imágenes
                        sprite_x, sprite_y,  # Coordenadas del sprite en recursos.pyxres
                        sprite_w, sprite_h,  # Tamaño del sprite
                        colkey=0  # Transparencia
                    )

                # Poner los regalos con su animación
                if self.muro.mapa[y][x] == 98:
                    if pyxel.frame_count // REFRESH_REGALOS % 2:
                        sprite = OBJETOS["REGALO_BRILLANTE"]
                        sprite_x, sprite_y = sprite["Coordenadas"]
                        sprite_w, sprite_h = 16, 16  # Ancho y largo del sprite
                    else:
                        sprite = OBJETOS["REGALO"]
                        sprite_x, sprite_y = sprite["Coordenadas"]
                        sprite_w, sprite_h = 16, 16  # Ancho y largo del sprite
                    #Dibujar el regalo
                    pyxel.blt(
                        x * self.muro.celda_tamaño, y * self.muro.celda_tamaño,  # Coordenadas donde se dibuja el punto
                        0,  # Banco de imágenes
                        sprite_x, sprite_y,  # Coordenadas del sprite en recursos.pyxres
                        sprite_w, sprite_h,  # Tamaño del sprite
                        colkey=0  # Transparencia
                    )

                # Dibuja la fruta si existe
                if self.fruta_actual and self.posicion_actual:
                    sprite = OBJETOS[self.fruta_actual]
                    sprite_x, sprite_y = sprite["Coordenadas"]
                    sprite_w, sprite_h = 16, 16
                    x_pixel = self.posicion_actual[0] * self.muro.celda_tamaño
                    y_pixel = self.posicion_actual[1] * self.muro.celda_tamaño
                    pyxel.blt(
                        x_pixel, y_pixel, 0,
                        sprite_x, sprite_y, sprite_w, sprite_h, colkey=0
                    )

                    self.dibujar_letras_mapa(69, "READY!")
                    self.dibujar_letras_mapa(70, "HIGHSCORE")

        self.ver_puntuacion(188, 16)  # Mostrar la puntuación

    def dibujar_letras_mapa (self, num, sprite):
        for y in range(len(self.muro.mapa)):
            for x in range(len(self.muro.mapa[y])):
                if self.muro.mapa[y][x] == num:
                    sprite = TEXTO[sprite]
                    sprite_x, sprite_y = sprite["Coordenadas"]
                    sprite_w, sprite_h = sprite["Tamaño"]
                    pyxel.blt(x * self.muro.celda_tamaño, y * self.muro.celda_tamaño,0,sprite_x, sprite_y,sprite_w, sprite_h,colkey=0)

        
    def comer_puntos(self):
        pacman_x = self.pacman.x // self.muro.celda_tamaño  # Índice X en el mapa
        pacman_y = self.pacman.y // self.muro.celda_tamaño  # Índice Y en el mapa

        if self.muro.mapa[pacman_y][pacman_x] in [0, 98]:
            if self.muro.mapa[pacman_y][pacman_x] == 0:
                tipo_consumible = "BASTON"
            elif self.muro.mapa[pacman_y][pacman_x] == 98:
                tipo_consumible = "REGALO"

            # Sumar puntos
            self.puntos += OBJETOS[tipo_consumible]["Puntos"]

            # Eliminar el objeto del mapa
            self.muro.mapa[pacman_y][pacman_x] = -1

    def ver_puntuacion(self, x, y):
        colores_dispo = [NUMEROS_BLANCOS, NUMEROS_MORADOS, NUMEROS_NARANJAS, NUMEROS_VERDES]

        # Cambia el color solo cuando se supera un nuevo múltiplo de 500
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
                pos_x, y,           # Coordenadas en pantalla
                0,                  # Banco de imágenes
                sprite_x, sprite_y, # Coordenadas del sprite en el banco
                sprite_w, sprite_h, # Tamaño del sprite
                colkey=0            # Color transparente
            )
            pos_x += sprite_w + 1  # Espacio entre los dígitos

    def encontrar_celdas_vacias(self):
        celdas_vacias = []
        for y in range(len(self.muro.mapa)):
            for x in range(len(self.muro.mapa[y])):
                if self.muro.mapa[y][x] == -1:
                    celdas_vacias.append((x, y))  # Guarda las coordenadas de las celdas vacías
        return celdas_vacias

    def mover_fruta(self):
        if not self.posicion_actual or not self.posicion_destino:
            return  # Nada que mover

        x_actual, y_actual = self.posicion_actual
        x_destino, y_destino = self.posicion_destino

        if (x_actual, y_actual) == (x_destino, y_destino):
            self.posicion_actual = None  # Movimiento completado
            self.posicion_destino = None
            return

        # Mover hacia el destino
        if x_actual < x_destino:
            x_actual += 1
        elif x_actual > x_destino:
            x_actual -= 1

        if y_actual < y_destino:
            y_actual += 1
        elif y_actual > y_destino:
            y_actual -= 1

        self.posicion_actual = (x_actual, y_actual)
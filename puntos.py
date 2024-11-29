from constantes import OBJETOS, REFRESH_REGALOS, TEXTO
from muro import Muro
import pyxel

class Puntos:
    def __init__(self, muro, sprite, pacman):
        self.muro = muro
        self.sprite = sprite
        self.pacman = pacman
        self.puntos = 0

    def draw(self):
        # Poner los puntos y otros objetos en el mapa
        for y in range(len(self.muro.mapa)):
            for x in range(len(self.muro.mapa[y])):
                if self.muro.mapa[y][x] == 0:
                    sprite = OBJETOS["BASTON"]
                    sprite_x, sprite_y = sprite["Coordenadas"]
                    sprite_w, sprite_h = 16, 16
                    pyxel.blt(
                        x * self.muro.celda_tamaño, y * self.muro.celda_tamaño,
                        0,
                        sprite_x, sprite_y,
                        sprite_w, sprite_h,
                        colkey=0
                    )
                elif self.muro.mapa[y][x] == 98:
                    if pyxel.frame_count // REFRESH_REGALOS % 2:
                        sprite = OBJETOS["REGALO_BRILLANTE"]
                    else:
                        sprite = OBJETOS["REGALO"]
                    sprite_x, sprite_y = sprite["Coordenadas"]
                    sprite_w, sprite_h = 16, 16
                    pyxel.blt(
                        x * self.muro.celda_tamaño, y * self.muro.celda_tamaño,
                        0,
                        sprite_x, sprite_y,
                        sprite_w, sprite_h,
                        colkey=0
                    )

        # Mostrar la puntuación con texto más grande
        self.texto_mas_grande(50, 20, f"Puntos: {self.puntos}", 7, 3)

    def comer_puntos(self):
        pacman_x = self.pacman.x // self.muro.celda_tamaño  # Índice X en el mapa
        pacman_y = self.pacman.y // self.muro.celda_tamaño  # Índice Y en el mapa

        if self.muro.mapa[pacman_y][pacman_x] in [0, 98]:
            # Cuando se trata de un punto normal
            if self.muro.mapa[pacman_y][pacman_x] == 0:
                tipo_consumible = "BASTON"
            # Cuando es una pastilla de poder
            elif self.muro.mapa[pacman_y][pacman_x] == 98:
                tipo_consumible = "REGALO"

            # Sumar puntos
            self.puntos += OBJETOS[tipo_consumible]["Puntos"]

            # Eliminar el objeto del mapa
            self.muro.mapa[pacman_y][pacman_x] = -1

    # Hacer texto más grande
    def texto_mas_grande(self, x, y, text, color, tamaño):
        for i, char in enumerate(text):
            for dx in range(tamaño):
                for dy in range(tamaño):
                    pyxel.text(x + i * 4 * tamaño + dx, y + dy, char, color)
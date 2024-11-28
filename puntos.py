from constantes import OBJETOS
from muro import Muro
import pyxel

class Puntos:
    def __init__(self,muro,sprite):
        self.muro = muro
        self.sprite = sprite

    def draw(self):

        for y in range (len(self.muro.mapa)):
            for x in range(len(self.muro.mapa[y])):
                if self.muro.mapa[y][x] == 0:
                    sprite = OBJETOS["REGALO"]
                    sprite_x, sprite_y = sprite["Coordenadas"]
                    sprite_w, sprite_h = 16 # Ancho y largo del sprite
                    pyxel.blt(
                        y * self.muro.celda_tamaño, x * self.muro.celda_tamaño,  # Coordenadas donde se dibuja el punto
                        1,  # Banco de imágenes
                        sprite_x, sprite_y,  # Coordenadas del sprite en recursos.pyxres
                        sprite_w, sprite_h,  # Tamaño del sprite
                        colkey=0  # Transparencia
                    )
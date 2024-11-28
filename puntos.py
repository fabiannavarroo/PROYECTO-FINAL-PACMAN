from constantes import OBJETOS, REFRESH
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
                    sprite = OBJETOS["BASTON"]
                    sprite_x, sprite_y = sprite["Coordenadas"]
                    sprite_w, sprite_h = 16, 16 # Ancho y largo del sprite
                    pyxel.blt(
                        x * self.muro.celda_tamaño, y * self.muro.celda_tamaño,  # Coordenadas donde se dibuja el punto
                        0,  # Banco de imágenes
                        sprite_x, sprite_y,  # Coordenadas del sprite en recursos.pyxres
                        sprite_w, sprite_h,  # Tamaño del sprite
                        colkey=0  # Transparencia
                    )
                if self.muro.mapa[y][x] == 98:
                    if pyxel.frame_count // REFRESH % 1:
                        sprite = (256,256)
                    else:
                        sprite = OBJETOS["REGALO"]
                        sprite_x, sprite_y = sprite["Coordenadas"]
                        sprite_w, sprite_h = 16, 16 # Ancho y largo del sprite
                        pyxel.blt(
                            x * self.muro.celda_tamaño, y * self.muro.celda_tamaño,  # Coordenadas donde se dibuja el punto
                            0,  # Banco de imágenes
                            sprite_x, sprite_y,  # Coordenadas del sprite en recursos.pyxres
                            sprite_w, sprite_h,  # Tamaño del sprite
                            colkey=0  # Transparencia
                        )
                    
from constantes import OBJETOS
import pyxel

class Puntos:
    def __init__(self,muro,sprite):
        self.muro = muro
        self.sprite = sprite

    def pintar_puntos(self):
        self.muro.mapa
        for y in range(self.muro.mapa):
            for x in range(self.muro.mapa[y]):
                if self.muro.mapa[y][x] == 0:
                    sprite = OBJETOS
                    sprite_x, sprite_y = sprite["Coordenadas"]
                    sprite_w, sprite_h = sprite["Tamaño"]
                    pyxel.blt(
                        columna * self.celda_tamaño, fila * self.celda_tamaño,  # Coordenadas donde se dibuja el muro
                        1,  # Banco de imágenes
                        sprite_x, sprite_y,  # Coordenadas del sprite en recursos.pyxres
                        sprite_w, sprite_h,  # Tamaño del sprite
                        colkey=0  # Transparencia
                    )
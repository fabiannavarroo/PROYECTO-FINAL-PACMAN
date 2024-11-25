

from constantes import *
import pyxel

class Muro:
    def __init__(self):
        # Matriz que representa el mapa usando constantes
        self.mapa = [
            [1,0,1,2,3],
            [0,0,0,1,1]
        ]

    def draw(self):
        """
        Dibuja los muros en la pantalla adaptando el tamaño de los sprites.
        """
        for fila in range(len(self.mapa)):
            for columna in range(len(self.mapa[0])):
                muro = self.mapa[fila][columna]
                if muro:  # Si no es un espacio vacío
                    sprite_x, sprite_y = muro["Coordenadas"]
                    sprite_w, sprite_h = muro["Tamaño"]
                    pyxel.blt(
                        columna * 8, fila * 8,  # Coordenadas donde se dibuja el muro
                        0,  # Banco de imágenes
                        sprite_x, sprite_y,  # Coordenadas del sprite en recursos.pyxres
                        sprite_w, sprite_h,  # Tamaño del sprite
                        colkey=0  # Transparencia
                    )
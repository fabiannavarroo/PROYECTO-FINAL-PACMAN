import pyxel
from constantes import MUROS

class Muro:
    def __init__(self):
        # Matriz que representa el mapa usando números
        self.mapa = [
            [1, 2, 2, 2, 3],
            [9, 0, 0, 0, 10],
            [9, 0, 13, 14, 10],
            [9, 0, 0, 0, 10],
            [4, 5, 5, 5, 6],
        ]

    def draw(self):

        #Dibuja los muros en la pantalla adaptando el tamaño de los sprites.
        for fila in range(len(self.mapa)):
            for columna in range(len(self.mapa[0])):
                tipo_muro = self.mapa[fila][columna]
                if tipo_muro != 0:  # Si no es un espacio vacío
                    sprite = MUROS[tipo_muro]
                    sprite_x, sprite_y = sprite["Coordenadas"]
                    sprite_w, sprite_h = sprite["Tamaño"]
                    pyxel.blt(
                        columna * 8, fila * 8,  # Coordenadas donde se dibuja el muro
                        0,  # Banco de imágenes
                        sprite_x, sprite_y,  # Coordenadas del sprite en recursos.pyxres
                        sprite_w, sprite_h,  # Tamaño del sprite
                        colkey=0  # Transparencia
                    )
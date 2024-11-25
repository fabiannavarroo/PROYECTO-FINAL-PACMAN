import pyxel
from constantes import MUROS

class Muro:
    def __init__(self):
        # Matriz que representa el mapa usando números
        self.mapa = [
            [11,    2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  7,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  12],
            [5,     0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  5,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  5],
            [5,     0,  1,  2,  3,  0,  1,  2,  2,  3,  0,  0,  0,  5,  0,  1,  2,  2,  2,  3,  0,  1,  2,  3,  0,  0,  5],
            
        ]

        # Tamaño de cada celda en píxeles
        self.celda_tamaño = 16  # Escala el tamaño de las celdas

    def colision(self, x, y):

        #Comprueba si hay un muro en la posición (x, y).

        fila = y // self.celda_tamaño
        columna = x // self.celda_tamaño

        # Comprobar si está dentro de los límites del mapa
        if 0 <= fila < len(self.mapa) and 0 <= columna < len(self.mapa[0]):
            return self.mapa[fila][columna] != 0
        return False

    def draw(self):
    
        #Dibuja los muros en la pantalla
        for fila in range(len(self.mapa)):
            for columna in range(len(self.mapa[0])):
                tipo_muro = self.mapa[fila][columna]
                if tipo_muro != 0:  # Si no es un espacio vacío
                    sprite = MUROS[tipo_muro]
                    sprite_x, sprite_y = sprite["Coordenadas"]
                    sprite_w, sprite_h = sprite["Tamaño"]
                    pyxel.blt(
                        columna * self.celda_tamaño, fila * self.celda_tamaño,  # Coordenadas donde se dibuja el muro
                        1,  # Banco de imágenes
                        sprite_x, sprite_y,  # Coordenadas del sprite en recursos.pyxres
                        sprite_w, sprite_h,  # Tamaño del sprite
                        colkey=0  # Transparencia
                    )
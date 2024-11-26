import pyxel
from constantes import MUROS

class Muro:
    def __init__(self):
        # Matriz que representa el mapa usando números
        self.mapa = [
            [11,2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  7,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  12],  # Fila 1
            [5, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  5,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  5],  # Fila 2
            [5, 0,  1,  2,  2,  3,  0,  1,  2,  2,  2,  3,  0,  6,  0,  1,  2,  2,  2,  3,  0,  1,  2,  2,  3,  0,  5],  # Fila 3
            [5, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  5],  # Fila 4 
            [5, 0,  1,  2,  2,  3,  0,  4,  0,  1,  2,  2,  7,  2,  2,  2,  3,  0,  4,  0,  1,  2,  2,  2,  3,  0,  5],  # Fila 5
            [5, 0,  0,  0,  0,  0,  0,  5,  0,  0,  0,  0,  5,  0,  0,  0,  0,  0,  5,  0,  0,  0,  0,  0,  0,  0,  5],  # Fila 6
            [13,2,  2,  2,  2,  12 ,0,  9,  2,  2,  3,  0,  6,  0,  1,  2,  2,  2,  10, 0,  11, 2,  2,  2,  2,  2,  14],  # Fila 7
            [0, 0,  0,  0,  0,  5,  0,  5,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  5,  0,  5,  0,  0,  0,  0,  0,  0],  # Fila 8
            [2, 2,  2,  2,  2,  14, 0,  6,  0,  15, 19, 19, 16, 16, 19, 19, 17, 0,  6,  0,  13, 2,  2,  2,  2,  2,  2],  # Fila 9
            [0, 0,  0,  0,  0,  0,  0,  0,  0,  21, 0,  0,  0,  0,  0,  0,  22, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],  # Fila 10
            [2, 2,  2,  2,  2,  12, 0,  4,  0,  18, 23, 23, 23, 23, 23, 23, 20, 0,  4,  0,  11, 2,  2,  2,  2,  2,  2],  # Fila 11
            [0, 0,  0,  0,  0,  5,  0,  5,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  5,  0,  5,  0,  0,  0,  0,  0,  0],  # Fila 12
            [11,2,  2,  2,  2,  14, 0,  6,  0,  1,  2,  2,  2,  7,  2,  2,  3,  0,  6,  0,  13, 2,  2,  2,  2,  2,  12],  # Fila 13
            [5, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  5,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  5],  # Fila 14
            [5, 0,  1,  2,  2,  12, 0,  1,  2,  2,  2,  3,  0,  6,  0,  1,  2,  2,  2,  3,  0,  11, 2,  2,  3,  0,  5],  # Fila 15
            [5, 0,  0,  0,  0,  5,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  5,  0,  0,  0,  0,  5],  # Fila 16
            [9, 2,  2,  3,  0,  6,  0,  4,  0,  1,  2,  2,  7,  2,  2,  3,  0,   4, 0,  0,  0,  6,  0,  1,  2,  2,  10],  # Fila 17
            [],  # Fila 18
            [],  # Fila 19
            [],  # Fila 20
            [],  # Fila 21
        ]

        # Tamaño de cada celda en píxeles
        self.celda_tamaño = 16  # Escala el tamaño de las celdas

    def colision(self, x, y):
    
        #Comprueba si hay un muro en la posición (x, y) considerando el tamaño del sprite.
        # Tamaño del sprite de Pac-Man
        sprite_tamaño = 16

        # Convertir las coordenadas de los bordes del sprite a índices de la matriz
        puntos_a_verificar = [
            (x, y),  # Esquina superior izquierda
            (x + sprite_tamaño - 1, y),  # Esquina superior derecha
            (x, y + sprite_tamaño - 1),  # Esquina inferior izquierda
            (x + sprite_tamaño - 1, y + sprite_tamaño - 1),  # Esquina inferior derecha
        ]

        for px, py in puntos_a_verificar:
            fila = py // self.celda_tamaño
            columna = px // self.celda_tamaño

            # Comprobar si está dentro de los límites del mapa
            if 0 <= fila < len(self.mapa) and 0 <= columna < len(self.mapa[0]):
                # Si hay un muro, devuelve True
                if self.mapa[fila][columna] != 0:
                    return True
        return False  # No hay colisión


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
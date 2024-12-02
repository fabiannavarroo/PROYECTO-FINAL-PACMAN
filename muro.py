import pyxel
from constantes import MUROS,TEXTO

class Muro:
    def __init__(self):
        # Matriz que representa el mapa usando números
        self.mapa = [
            [99, 99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99],
            [99, 99,  99,  99,  99,  99,  99,  70,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99],
            [99, 99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99],
            [11,2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  7,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  12],  # Fila 1
            [5, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  5,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  5],  # Fila 2
            [5,98,  1,  2,  2,  3,  0,  1,  2,  2,  2,  3,  0,  6,  0,  1,  2,  2,  2,  3,  0,  1,  2,  2,  3, 98,  5],  # Fila 3
            [5, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  5],  # Fila 4 
            [5, 0,  1,  2,  2,  3,  0,  4,  0,  1,  2,  2,  7,  2,  2,  2,  3,  0,  4,  0,  1,  2,  2,  2,  3,  0,  5],  # Fila 5
            [5, 0,  0,  0,  0,  0,  0,  5,  0,  0,  0,  0,  5,  0,  0,  0,  0,  0,  5,  0,  0,  0,  0,  0,  0,  0,  5],  # Fila 6
            [13,2,  2,  2,  2,  12, 0,  9,  2,  2,  3,  99,  6, 99,  1,  2,  2,  2,  10, 0,  11, 2,  2,  2,  2,  2,  14],  # Fila 7
            [99,99, 99, 99, 99,  5, 0,  5,  99, 99, 99, 99, 99, 99, 99, 99, 99, 99,  5,  0,  5,  99, 99, 99, 99, 99, 99],  # Fila 8
            [2, 2,  2,  2,  2,  14, 0,  6,  99, 15, 19, 19, 16, 16, 19, 19, 17, 99,  6,  0,  13, 2,  2,  2,  2,  2,  2],  # Fila 9
            [99,99, 99, 99, 99, 99, 0, 99,  99, 21, 99, 99, 99, 99, 99, 99, 22, 99, 99,  0,  99, 99, 99, 99, 99, 99, 99],  # Fila 10
            [2, 2,  2,  2,  2,  12, 0,  4,  99, 18, 23, 23, 23, 23, 23, 23, 20, 99,  4,  0,  11, 2,  2,  2,  2,  2,  2],  # Fila 11
            [99,99, 99, 99, 99,  5, 0,  5,  99, 99, 99, 99, 69, 99, 99, 99, 99, 99,  5,  0,  5,  99, 99, 99, 99, 99, 99],  # Fila 12
            [11,2,  2,  2,  2,  14, 0,  6,  99,  1,  2,  2,  2,  7,  2,  2,  3, 99,  6,  0,  13, 2,  2,  2,  2,  2,  12],  # Fila 13
            [5, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  5,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  5],  # Fila 14
            [5, 0,  1,  2,  2,  12, 0,  1,  2,  2,  2,  3,  0,  6,  0,  1,  2,  2,  2,  3,  0,  11, 2,  2,  3,  0,  5],  # Fila 15
            [5,98,  0,  0,  0,  5,  0,  0,  0,  0,  0,  0,  0,  99, 0,  0,  0,  0,  0,  0,  0,  5,  0,  0,  0, 98,  5],  # Fila 16
            [9, 2,  2,  3,  0,  6,  0,  4,  0,  1,  2,  2,  2,  7,  2,  2,  2,  3,  0,  4,  0,  6,  0,  1,  2,  2,  10],  # Fila 17
            [5, 0,  0,  0,  0,  0,  0,  5,  0,  0,  0,  0,  0,  5,  0,  0,  0,  0,  0,  5,  0,  0,  0,  0,  0,  0,  5],  # Fila 18
            [5, 0,  1,  2,  2,  2,  2,  8,  2,  2,  2,  3,  0,  6,  0,  1,  2,  2,  2,  8,  2,  2,  2,  2,  3,  0,  5],  # Fila 19
            [5, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  5],  # Fila 20
            [13,2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  14],  # Fila 21
            [99, 99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99],
            [99, 99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99,  99]
        ]

        # Tamaño de cada celda en píxeles
        self.celda_tamaño = 16 
        self.otros_objetos = [-1,0,69,70,71,90,91,92,93,94,95,96,97,98,99]
        

    def colision(self, x, y):
        #Comprueba si hay un muro en la posición (x, y) considerando el tamaño del sprite.
        # Tamaño del sprite de Pac-Man y Fantasmas
        sprite_tamaño = 16

        # Convertir las coordenadas de los bordes del sprite a índices de la matriz
        puntos_a_verificar = [
            (x, y),  # Esquina superior izquierda
            (x + sprite_tamaño - 1, y),  # Esquina superior derecha
            (x, y + sprite_tamaño - 1),  # Esquina inferior izquierda
            (x + sprite_tamaño - 1, y + sprite_tamaño - 1),  # Esquina inferior derecha
        ]

        # Convertir la posición vertical y horizontal a un indice de la matriz∫
        for px, py in puntos_a_verificar:
            fila = int(py // self.celda_tamaño)
            columna = int(px // self.celda_tamaño)

            # Comprobar si está dentro de los límites del mapa
            if 0 <= fila < len(self.mapa) and 0 <= columna < len(self.mapa[0]):
                # Si hay un muro, devuelve True
                if self.mapa[fila][columna] not in self.otros_objetos:
                    return True
        return False  # No hay colisión
    

    def draw(self):
        #Dibuja los muros en la pantalla
        for fila in range(len(self.mapa)):
            for columna in range(len(self.mapa[0])):
                tipo_muro = self.mapa[fila][columna]
                if tipo_muro not in self.otros_objetos:  # Si no es un espacio vacío
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
    
    def fin(self):
        # Dibujar las vidas restantes
        sprite = TEXTO["GAME OVER"]
        sprite_x, sprite_y = sprite["Coordenadas"]
        sprite_w, sprite_h = sprite["Tamaño"]
        pos_x = 10
        pos_y= 12
        pyxel.blt(pos_x, pos_y, 0, sprite_x, sprite_y, sprite_w, sprite_h, colkey=0)
        pos_x += sprite_w + 2


import pyxel

class Mapa:
    def __init__(self):
        # Matriz que define el diseño del mapa
        self.mapa = [
            [1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 24, 25, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 2],  # Fila 1
            [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],  # Fila 2
            [7, 0, 9, 15, 15, 11, 0, 9, 15, 15, 15, 11, 0, 13, 14, 0, 9, 15, 15, 15, 11, 0, 9, 15, 15, 11, 0, 8],  # Fila 3
            [7, 0, 13, 0, 0, 14, 0, 13, 0, 0, 0, 14, 0, 13, 14, 0, 13, 0, 0, 0, 14, 0, 13, 0, 0, 14, 0, 8],  # Fila 4
            [7, 0, 10, 16, 16, 12, 0, 10, 16, 16, 16, 12, 0, 10, 12, 0, 10, 16, 16, 16, 12, 0, 10, 16, 16, 12, 0, 8],  # Fila 5
            [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],  # Fila 6
            [7, 0, 18, 22, 22, 20, 0, 9, 11, 0, 18, 22, 22, 22, 22, 22, 22, 20, 0, 9, 11, 0, 18, 22, 22, 20, 0, 8],  # Fila 7
            [7, 0, 19, 23, 23, 21, 0, 13, 14, 0, 19, 23, 23, 27, 32, 23, 23, 21, 0, 13, 14, 0, 19, 23, 23, 21, 0, 8],  # Fila 8
            [7, 0, 0, 0, 0, 0, 0, 13, 14, 0, 0, 0, 0, 13, 14, 0, 0, 0, 0, 13, 14, 0, 0, 0, 0, 0, 0, 8],  # Fila 9
            [3, 6, 6, 6, 6, 35, 0, 13, 29, 22, 22, 20, 0, 13, 14, 0, 18, 22, 22, 31, 14, 0, 34, 6, 6, 6, 6 ,4],  # Fila 10
            [0, 0, 0, 0, 0, 8, 0, 13, 32, 23, 23, 21, 0, 10, 12, 0, 19, 23, 23, 27, 14, 0, 7, 0, 0, 0, 0, 0],  # Fila 11
            [0 ,0 ,0 ,0 ,0 ,8 ,0 ,13 ,14 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0, 0 ,0 ,13 ,14 ,0 ,7 ,0 ,0 ,0 ,0 ,0],  # Fila 12
            [0 ,0 ,0 ,0 ,0 ,8 ,0 ,13 ,14 ,0 ,1 ,5 ,5 ,17 ,17 ,5 ,5 , 2, 0, 13 , 14 , 0, 7, 0, 0, 0, 0, 0],  # Fila 13
            [5, 5, 5, 5, 5, 37, 0, 10, 12, 0, 7, 0, 0, 0, 0, 0, 0, 8, 0, 10, 12, 0, 3, 6, 6, 6, 6, 6],  # Fila 14
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Fila 15
            [5, 5, 5, 5, 5, 2, 0, 9, 11, 0, 7, 0, 0, 0, 0, 0, 0, 8, 0, 9, 11, 0, 1, 5, 5, 5, 5, 5],  # Fila 16
            [0, 0, 0, 0, 0, 8, 0, 13, 14, 0, 3, 6, 6, 6, 6, 6, 6, 4, 0, 13, 14, 0, 7, 0, 0, 0, 0, 0],  # Fila 17
            [0, 0, 0, 0, 0, 8, 0, 13, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 14, 0, 7, 0, 0, 0, 0, 0],  # Fila 18
            [0, 0, 0, 0, 0, 8, 0, 13, 14, 0, 18, 22, 22, 22, 22, 22, 22, 20, 0, 13, 14, 0, 7, 0, 0, 0, 0, 0],  # Fila 19
            [34, 6, 6, 6, 6, 4, 0, 10, 12, 0, 19, 23, 23, 27, 32, 23, 23, 21, 0, 10, 12, 0, 3, 6, 6, 6, 6, 35],  # Fila 20
            [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],  # Fila 21
            [7, 0, 18, 22, 22, 48, 0, 18, 22, 22, 22, 20, 0, 13, 14, 0, 18, 22, 22, 22, 20, 0, 46, 22, 22, 20, 0, 8],  # Fila 22
            [7, 0, 19, 23, 27, 14, 0, 19, 23, 23, 23, 21, 0, 10, 12, 0, 19, 23, 23, 23, 21, 0, 13, 46, 23, 21, 0, 8],  # Fila 23
            [7, 0, 0, 0, 13, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 14, 0, 0, 0, 8],  # Fila 24
            [41, 22, 20, 0, 13, 14, 0, 9, 11, 0, 18, 22, 22, 22, 22, 22, 22, 20, 0, 9, 11, 0, 13, 14, 0, 18, 22, 40],  # Fila 25
            [43, 23, 21, 0, 29, 31, 0, 13, 14, 0, 19, 23, 23, 27, 32, 23, 23, 21, 0, 13, 14, 0, 29, 31, 0, 19, 23, 42],  # Fila 26
            [7, 0, 0, 0, 0, 0, 0, 13, 14, 0, 0, 0, 0, 13, 14, 0, 0, 0, 0, 13, 14, 0, 0, 0, 0, 0, 0, 8],  # Fila 27
            [7, 0, 18, 22, 22, 22, 22, 31, 29, 22, 22, 20, 0, 13, 14, 0, 18, 22, 22, 31, 29, 22, 22, 22, 22, 20, 0, 8],  # Fila 28
            [7, 0, 19, 23, 23, 23, 23, 23, 23, 23, 23, 21, 0, 10, 12, 0, 19, 23, 23, 23, 23, 23, 23, 23, 23, 21, 0, 8],  # Fila 29
            [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8],  # Fila 30
            [3, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 4]  # Fila 31

        ]

    def draw(self):
        # Diccionario que da valores de la matriz a coordenadas en el archivo de recursos
        sprites = {
            1: (0, 120),  # Esquina superior izquierda
            2: (32, 120),  # Esquina superior derecha
            3: (0, 152),  # Esquina inferior izquierda
            4: (32, 152),  # Esquina inferior derecha
            5: (16, 120),  # Borde superior 
            6: (16, 152),  # Borde inferior
            7: (0, 136),  # Borde izquierdo
            8: (40, 136),  # Borde derecho
            9: (0, 184),  # Esquina simple izquierda superior
            10: (0, 216),  # Esquina simple izquierda inferior
            11: (32, 184),  # Esquina simple derecha superior
            12: (32, 216),   # Esquina simple derecha inferior
            13: (0, 200),   # Borde lateral simple izquierda
            14: (32, 200),   # Borde lateral simple derecha
            15: (16, 176),   # Borde superior simple 
            16: (16, 224),   # Borde inferior simple 
            17: (40, 16),   # Salida de los fantasmas
            18: (0, 56),    # Semi circulo izquierda arriba horizontal
            19: (0, 88),   # Semi circulo izquierda abajo horizontal
            20: (32, 56),   # Semi circulo derecha arriba horizontal
            21: (32, 88),    # Semi circulo derecha abajo horizontal
            22: (16, 56),   # recta simple arriba horizontal
            23: (16, 88),   # recta simple abajo horizontal
            24: (64, 0),  # giro abjo con borde izquierda
            25: (80, 0),   # giro abjo con borde derecha
            27: (64, 120),  # cambio de sentido hacia abjo izquierda
            29: (72, 144),  # cambio de sentido hacia izquierda abajo
            31: (96, 144),  # cambio de sentido hacia arriba derecha
            32: (104, 120),  # cambio de sentido hacia derecha derecha
            34: (0, 24),  # giro de borde izquierda superior
            35: (16, 24),  # giro de borde derecha superior
            36: (0, 40),  # giro de borde izquierda inferior
            37: (16, 40),  # giro de borde derecha inferior
            38: (64, 16),  # giro abajo con borde izquierda
            39: (80, 16),  # giro abjo con borde derecha
            40: (56, 40),  # giro izquierda con borde izquierda
            41: (72, 40),  # giro derecha con borde derecha
            42: (56, 56),  # giro izquierda con borde izquierda
            43: (72, 56),  # giro derecha con borde derecha
            44: (0, 72),   #recta media izquierda cerrado
            45: (32 , 72),  #recta media derecha cerrado
            46: (56, 80),  # semicirculo arriba izquierda
            47: (56, 96),  # semicirculo abajo izquierda
            48: (72, 80),  # semicirculo arriba derecha
            49: (72, 96)  # semicirculo abjo derecha
        }

        # Dibuja cada celda del mapa en la pantalla

        
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
            [3,6,6,6,6,2],  # Fila 10
            [],  # Fila 11
            [],  # Fila 12
            [],  # Fila 13
            [],  # Fila 14
            [],  # Fila 15
            [],  # Fila 16
            [],  # Fila 17
            [],  # Fila 18
            [],  # Fila 19
            [],  # Fila 20
            [],  # Fila 21
            [],  # Fila 22
            [],  # Fila 23
            [],  # Fila 24
            [],  # Fila 25
            [],  # Fila 26
            [],  # Fila 27
            [],  # Fila 28
            [],  # Fila 29
            [],  # Fila 30
            [],  # Fila 31
            []  # Fila 32
        ]

    def draw(self):
        # Tamaño de cada sprite en píxeles
        sprite_size = 8

        # Diccionario que da valores de la matriz a coordenadas en el archivo de recursos
        sprites = {
            1: (0, 0),  # Esquina superior izquierda
            2: (16, 0),  # Esquina superior derecha
            3: (0, 16),  # Esquina inferior izquierda
            4: (16, 16),  # Esquina inferior derecha
            5: (8, 0),  # Borde superior 
            6: (8, 16),  # Borde inferior
            7: (0, 8),  # Borde izquierdo
            8: (16, 8),  # Borde derecho
            9: (32, 0),  # Esquina simple izquierda superior
            10: (32, 16),  # Esquina simple izquierda inferior
            11: (48, 0),  # Esquina simple derecha superior
            12: (48, 16),   # Esquina simple derecha inferior
            13: (32, 8),   # Borde lateral simple izquierda
            14: (48, 8),   # Borde lateral simple derecha
            15: (40, 0),   # Borde superior simple 
            16: (40, 16),   # Borde inferior simple 
            17: (0, 24),   # Salida de los fantasmas
            18: (0, 32),    # Semi circulo izquierda arriba horizontal
            19: (0, 40),   # Semi circulo izquierda abajo horizontal
            20: (16, 32),   # Semi circulo derecha arriba horizontal
            21: (16, 40),    # Semi circulo derecha abajo horizontal
            22: (8, 32),   # recta simple arriba horizontal
            23: (8, 40),   # recta simple abajo horizontal
            24: (8, 24),  # giro abjo con borde izquierda
            25: (16, 24),   # giro abjo con borde derecha
            27: (8, 56),  # cambio de sentido hacia abjo izquierda
            28: (8, 64),   # recta abajo simple para cambio de sentido izquierda
            29: (8, 72),  # cambio de sentido hacia izquierda abajo
            30: (16, 72),   # recta abajo cambio de sentido
            31: (24, 72),  # cambio de sentido hacia arriba derecha
            32: (24, 56),  # cambio de sentido hacia derecha derecha
            33: (24, 64)  # recta simple cambio de sentido derecha
        }

        # Dibuja cada celda del mapa en la pantalla
        for y, row in enumerate(self.mapa):
            for x, cell in enumerate(row):
                if cell in sprites:
                    sprite_x, sprite_y = sprites[cell]
                    pyxel.blt(x * sprite_size, y * sprite_size, 0, sprite_x, sprite_y, sprite_size, sprite_size)

class App:
    def __init__(self):
        # Inicializa Pyxel con el tamaño de la ventana
        pyxel.init(226, 226)
        # Establece el título de la ventana
        pyxel.title = "Pacman"
        # Carga los recursos del archivo .pyxres
        pyxel.load("assets/map.pyxres")
        self.mapa = Mapa()
        # Ejecuta el bucle principal
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)  # Limpia la pantalla
        self.mapa.draw()  # Dibuja el mapa

# Inicia la aplicación
App()
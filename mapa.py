import pyxel

class Mapa:
    def __init__(self):
        # Matriz que define el diseño del mapa
        self.mapa = [
            [1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7, 8, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 2],
            [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],
            [6, 0, 11, 14, 14, 12, 0, 11, 14, 14, 14, 12, 0, 16, 15, 0, 11, 14, 14, 14, 12, 0, 11, 14, 14, 12, 0, 6],
            [6, 0, 16, 0, 0, 15, 0, 16, 0, 0, 0, 15, 0, 16, 15, 0, 16, 0, 0, 0, 15, 0, 16, 0, 0, 15, 0, 6],
            [6, 0, 9, 13, 13, 10, 0, 9, 13, 13, 13, 10, 0, 9, 10, 0, 9, 13, 13, 13, 10, 0, 9, 13, 13, 10, 0, 6],
            [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],
            [6, 0, 11, 14, 14, 12, 0, 11, 12, 0, 11, 14, 14, 14, 14, 14, 14, 12, 0, 11, 12, 0, 11, 14, 14, 12, 0, 6],
            [6, 0, 9, 13, 13, 10, 0, 16, 15, 0, 9, 13, 13, 7, 8, 13, 13, 10, 0, 16, 15, 0, 9, 13, 13, 10, 0, 6],
            [6, 0, 0, 0, 0, 0, 0, 16, 15, 0, 0, 0, 0, 16, 15, 0, 0, 0, 0, 16, 15, 0, 0, 0, 0, 0, 0, 6]
        ]

    def draw(self):
        # Tamaño de cada sprite en píxeles
        sprite_size = 8

        # Diccionario que mapea valores de la matriz a coordenadas en el archivo de recursos
        sprites = {
            1: (0, 8),  # Esquina superior izquierda
            2: (8, 8),  # Esquina superior derecha
            5: (16, 8), # Borde horizontal
            6: (0, 16), # Borde vertical
            7: (0, 24), # Intersección superior
            8: (8, 24), # Intersección inferior
            9: (16, 24), # Borde inferior izquierdo
            10: (24, 24), # Borde inferior derecho
            11: (0, 32), # Esquina interior superior izquierda
            12: (8, 32), # Esquina interior superior derecha
            13: (16, 32), # Esquina interior inferior izquierda
            14: (24, 32), # Esquina interior inferior derecha
            15: (32, 32), # Centro vacío
            16: (40, 32)  # Relleno especial
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
        pyxel.init(224, 72)
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
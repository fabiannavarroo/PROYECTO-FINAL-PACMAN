import pyxel

class Mapa:
    def __init__(self):
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
        # Tamaño del sprite en píxeles
        sprite_size = 8

        # Diccionario que mapea valores de la matriz a coordenadas en el archivo de recursos
        sprites = {
            1: (0, 8),  # Esquina superior izquierda
            2: (8, 8),  # Esquina superior derecha
            5: (16, 8), # Borde horizontal
            6: (0, 16), # Borde vertical
            7: (0, 24), # Intersección superior
            8: (8, 24), # Intersección inferior
            # Agrega aquí más valores según corresponda...
        }

        # Dibujar cada celda del mapa
        for y, row in enumerate(self.mapa):
            for x, cell in enumerate(row):
                if cell in sprites:
                    sprite_x, sprite_y = sprites[cell]
                    pyxel.blt(x * sprite_size, y * sprite_size, 0, sprite_x, sprite_y, sprite_size, sprite_size)

class App:
    def __init__(self):
        pyxel.init(224, 72, caption="Pacman")
        pyxel.load("assets/map.pyxres")
        self.mapa = Mapa()
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)
        self.mapa.draw()

# Inicia la aplicación
App()
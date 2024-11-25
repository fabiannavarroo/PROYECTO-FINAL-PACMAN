import pyxel

class Muro:
    def __init__(self):
        # Matriz que representa el mapa
        self.mapa = [
            [3, 2, 2, 2, 4, 2, 2, 2, 4],
            [1, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 3, 4, 1, 3, 4, 0, 1],
            [1, 0, 1, 1, 0, 1, 1, 0, 1],
            [5, 2, 6, 0, 0, 0, 3, 2, 6],
            [1, 0, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 1],
            [7, 2, 2, 2, 8, 2, 2, 2, 8],
        ]

        # Tamaño de cada celda (en píxeles)
        self.celda = 8

        # Diccionario para mapear tipos de muros a sprites
        self.sprites = {
            1: (0, 0),   # Muro vertical
            2: (8, 0),  # Muro horizontal
            3: (0, 32),  # Esquina superior izquierda
            4: (48, 0),  # Esquina superior derecha
            5: (32, 16), # Esquina inferior izquierda
            6: (48, 16), # Esquina inferior derecha
            7: (0, 16),  # Unión izquierda
            8: (16, 16), # Unión derecha
        }

    def colision(self, x, y):
        """
        Comprueba si hay un muro en la posición (x, y).
        :param x: Posición x (en píxeles).
        :param y: Posición y (en píxeles).
        :return: True si hay colisión con un muro, False en caso contrario.
        """
        fila = y // self.celda
        columna = x // self.celda

        # Comprobar si está dentro de los límites del mapa
        if 0 <= fila < len(self.mapa) and 0 <= columna < len(self.mapa[0]):
            return self.mapa[fila][columna] != 0  # Cualquier número distinto de 0 es un muro
        return False

    def draw(self):
        """
        Dibuja los muros en la pantalla.
        """
        for fila in range(len(self.mapa)):
            for columna in range(len(self.mapa[0])):
                tipo_muro = self.mapa[fila][columna]
                if tipo_muro != 0:  # Si no es un espacio vacío
                    sprite_x, sprite_y = self.sprites[tipo_muro]
                    pyxel.blt(
                        columna * self.celda, fila * self.celda,
                        1,  # Banco de imágenes
                        sprite_x, sprite_y,  # Coordenadas del sprite
                        self.celda, self.celda,  # Tamaño del sprite
                        colkey=0  # Transparencia
                    )
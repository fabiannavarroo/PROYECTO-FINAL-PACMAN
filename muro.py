

import pyxel

class Muro:
    def __init__(self):
        # Matriz que representa el mapa
        # 1 = muro, 0 = espacio vacío
        self.mapa = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]

        # Tamaño de cada celda (en píxeles)
        self.celda = 16

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
            return self.mapa[fila][columna] == 1
        return False

    def draw(self):
        """
        Dibuja los muros en la pantalla.
        """
        for fila in range(len(self.mapa)):
            for columna in range(len(self.mapa[0])):
                if self.mapa[fila][columna] == 1:
                    pyxel.blt(
                        columna * self.celda, fila * self.celda,
                        0,  # Banco de imágenes
                        0, 32,  # Coordenadas del sprite del muro en recursos.pyxres
                        self.celda, self.celda,  # Tamaño del sprite
                        colkey=0  # Transparencia
                    )
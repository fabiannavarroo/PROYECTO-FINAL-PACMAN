import pyxel
from constantes import MUROS

class Muro:
    def __init__(self):
        # Matriz que representa el mapa usando números
        self.mapa = [
            [17, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 15, 16, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,2,18]
        ]

        # Tamaño de cada celda en píxeles
        self.celda_tamano = 16  # Escala el tamaño de las celdas

    def colision(self, x, y):
        """
        Comprueba si hay un muro en la posición (x, y).
        :param x: Coordenada x en píxeles.
        :param y: Coordenada y en píxeles.
        :return: True si hay colisión con un muro, False en caso contrario.
        """
        fila = y // self.celda_tamano
        columna = x // self.celda_tamano

        # Comprobar si está dentro de los límites del mapa
        if 0 <= fila < len(self.mapa) and 0 <= columna < len(self.mapa[0]):
            return self.mapa[fila][columna] != 0
        return False

    def draw(self):
        """
        Dibuja los muros en la pantalla adaptando el tamaño de los sprites.
        """
        for fila in range(len(self.mapa)):
            for columna in range(len(self.mapa[0])):
                tipo_muro = self.mapa[fila][columna]
                if tipo_muro != 0:  # Si no es un espacio vacío
                    sprite = MUROS[tipo_muro]
                    sprite_x, sprite_y = sprite["Coordenadas"]
                    sprite_w, sprite_h = sprite["Tamaño"]
                    pyxel.blt(
                        columna * self.celda_tamano, fila * self.celda_tamano,  # Coordenadas donde se dibuja el muro
                        1,  # Banco de imágenes
                        sprite_x, sprite_y,  # Coordenadas del sprite en recursos.pyxres
                        sprite_w, sprite_h,  # Tamaño del sprite
                        colkey=0  # Transparencia
                    )
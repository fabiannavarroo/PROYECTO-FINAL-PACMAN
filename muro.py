import pyxel
from constantes import MUROS

class Muro:
    def __init__(self):
        # Matriz que representa el mapa usando números
        self.mapa = [
            [17,2,2,2,2,2,2,2,2,2,2,2,2,15,16,2,2,2,2,2,2,2,2,2,2,2,2,18], # Fila 1
            [], # Fila 2
            [], # Fila 3
            [], # Fila 5
            [], # Fila 6
            [], # Fila 7
            [], # Fila 8
            [], # Fila 9
            [], # Fila 10
            [], # Fila 11
            [], # Fila 12
            [], # Fila 13
            [], # Fila 14
            [], # Fila 15
            [], # Fila 16
            [], # Fila 17
            [], # Fila 18
            [], # Fila 19
            [], # Fila 20
            [], # Fila 21
            [], # Fila 22
            [], # Fila 23
            [], # Fila 24
            [], # Fila 25
            [], # Fila 26
            [], # Fila 27
            [], # Fila 28
            [], # Fila 29
            [], # Fila 30
            [], # Fila 31
        ]

        # Tamaño de cada celda en píxeles
        self.celda_tamano = 32  # Escala el tamaño de las celdas a 16x16 píxeles

    def colision(self, x, y):

        #Comprueba si hay un muro en la posición (x, y)
        # Convertir coordenadas de píxeles a índices de la matriz
        fila = y // 8  # Cada celda del mapa tiene 8 píxeles de alto
        columna = x // 8  # Cada celda del mapa tiene 8 píxeles de ancho

        # Comprobar si está dentro de los límites del mapa
        if 0 <= fila < len(self.mapa) and 0 <= columna < len(self.mapa[0]):
            # Si el valor de la celda no es 0, hay un muro
            return self.mapa[fila][columna] != 0
        return False

    def draw(self):
        
        #Dibuja los muros en la pantalla adaptando el tamaño de los sprites.
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


import pyxel

class Pacman:
    def __init__(self, x, y):
        self.x = x  # Posición inicial en X
        self.y = y  # Posición inicial en Y
        self.velocidad = 2  # Velocidad de movimiento

    def mover(self):
        # Movimiento usando teclas
        if pyxel.btn(pyxel.KEY_UP):
            self.y -= self.velocidad
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += self.velocidad
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= self.velocidad
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += self.velocidad

    def dibujar(self):
        # Dibuja a Pacman en la pantalla
        # Sprite en posición (0, 0) en el archivo recursos.pyxres
        pyxel.blt(self.x, self.y, 0, 0, 0, 16, 16, 0)  # Sprite de 16x16 px
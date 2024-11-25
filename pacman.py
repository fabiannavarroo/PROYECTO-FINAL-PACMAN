

import pyxel

class Pacman:
    def __init__(self, x, y):
        self.x = x  # Posición inicial en X
        self.y = y  # Posición inicial en Y
        self.velocidad = 2  # Velocidad de movimiento

    def mover(self):
        # Control de movimiento usando teclas
        if pyxel.btn(pyxel.KEY_UP):
            self.y -= self.velocidad
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += self.velocidad
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= self.velocidad
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += self.velocidad

    def dibujar(self):
        # Dibuja a Pacman desde la página 0 del banco 0
        pyxel.blt(self.x, self.y, 0, 0, 0, 16, 16, 0)  # Usa el sprite de Pacman
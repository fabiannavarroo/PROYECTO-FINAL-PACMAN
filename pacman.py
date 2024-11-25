

import pyxel

class Pacman:
    def __init__(self, x, y, muro):
        self.x = x
        self.y = y
        self.velocidad = 2
        self.muro = muro  # Referencia a la clase Muro

    def mover(self):
        nueva_x, nueva_y = self.x, self.y

        # Control de movimiento usando teclas
        if pyxel.btn(pyxel.KEY_UP):
            nueva_y -= self.velocidad
        if pyxel.btn(pyxel.KEY_DOWN):
            nueva_y += self.velocidad
        if pyxel.btn(pyxel.KEY_LEFT):
            nueva_x -= self.velocidad
        if pyxel.btn(pyxel.KEY_RIGHT):
            nueva_x += self.velocidad

        # Verificar colisión antes de actualizar la posición
        if not self.muro.colision(nueva_x, self.y):
            self.x = nueva_x
        if not self.muro.colision(self.x, nueva_y):
            self.y = nueva_y

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 0, 16, 16, colkey=0)



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
        if pyxel.btn(pyxel.KEY_W):
            self.y -= self.velocidad
        if pyxel.btn(pyxel.KEY_S):
            self.y += self.velocidad
        if pyxel.btn(pyxel.KEY_A):
            self.x -= self.velocidad
        if pyxel.btn(pyxel.KEY_D):
            self.x += self.velocidad

    def dibujar(self):
        # Dibuja a Pacman sin reducir el tamaño
        sprite_x = 0  # Coordenada X en el recurso
        sprite_y = 0  # Coordenada Y en el recurso
        sprite_w = 16  # Ancho del sprite
        sprite_h = 16  # Alto del sprite

        pyxel.blt(
            self.x, self.y, 
            0,  # Banco de imágenes
            sprite_x, sprite_y, 
            sprite_w, sprite_h, 
            colkey=0  # Transparencia
            )
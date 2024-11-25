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
        # Escala del sprite (más pequeño)
        escala = 0.5  # Escala del sprite (50% del tamaño original)
        ancho_original = 16  # Ancho original del sprite
        alto_original = 16  # Alto original del sprite

        ancho_reducido = int(ancho_original * escala)
        alto_reducido = int(alto_original * escala)

        pyxel.blt(
            self.x, self.y, 0, 0, 0,
            ancho_reducido, alto_reducido, 0
        )
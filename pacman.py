import pyxel

class Pacman:
    def __init__(self, x, y):
        self.x = x  # Posición inicial en X
        self.y = y  # Posición inicial en Y
        self.velocidad = 2  # Velocidad de movimiento
        self.escala = 0.5  # Escala de Pacman (50% más pequeño)

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
        # Dibuja a Pacman con escala
        sprite_x = 0  # Coordenada X en el recurso
        sprite_y = 0  # Coordenada Y en el recurso
        sprite_w = 16  # Ancho original
        sprite_h = 16  # Alto original

        # Dibuja el sprite con transformación
        pyxel.blt(
            int(self.x), int(self.y), 
            0,  # Banco de imágenes
            sprite_x, sprite_y, 
            int(sprite_w * self.escala),  # Ancho escalado
            int(sprite_h * self.escala),  # Alto escalado
            colkey=0  # Transparencia
        )
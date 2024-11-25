

import pyxel

class Fantasma:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color  # Identifica al fantasma (rojo, rosa, azul, naranja)
        self.direccion = 1  # Dirección inicial: 1 (derecha), -1 (izquierda)
        self.velocidad = 1

    def mover(self):
        # Movimiento horizontal básico
        self.x += self.direccion * self.velocidad

        # Cambiar de dirección si alcanza los bordes
        if self.x < 0 or self.x > pyxel.width - 16:
            self.direccion *= -1

    def dibujar(self):
        # Dibuja al fantasma según su color desde la página 0
        if self.color == "rojo":
            pyxel.blt(self.x, self.y, 0, 0, 64, 16, 16, 0)  # Sprite en (16, 0)
        elif self.color == "rosa":
            pyxel.blt(self.x, self.y, 0, 0, 96, 16, 16, 0)  # Sprite en (32, 0)
        elif self.color == "azul":
            pyxel.blt(self.x, self.y, 0, 0, 48, 16, 16, 0)  # Sprite en (48, 0)
        elif self.color == "naranja":
            pyxel.blt(self.x, self.y, 0, 0, 80, 16, 16, 0)  # Sprite en (64, 0)

# Subclases para cada fantasma
class FantasmaRojo(Fantasma):
    def __init__(self, x, y):
        super().__init__(x, y, "rojo")

class FantasmaRosa(Fantasma):
    def __init__(self, x, y):
        super().__init__(x, y, "rosa")

class FantasmaAzul(Fantasma):
    def __init__(self, x, y):
        super().__init__(x, y, "azul")

class FantasmaNaranja(Fantasma):
    def __init__(self, x, y):
        super().__init__(x, y, "naranja")
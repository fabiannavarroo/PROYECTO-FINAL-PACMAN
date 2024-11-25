from constantes import (FANTASMA_ROJO_ABAJO, FANTASMA_ROSA_ABAJO, 
                        FANTASMA_AZUL_ABAJO, FANTASMA_NARANJA_ABAJO)
import pyxel

class Fantasma:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color  # Identifica al fantasma
        self.direccion = 1  # Dirección inicial: 1 (derecha), -1 (izquierda)
        self.velocidad = 1

    def mover(self):
        # Movimiento horizontal básico
        self.x += self.direccion * self.velocidad

        # Cambiar de dirección si alcanza los bordes
        if self.x < 0 or self.x > pyxel.width - 16:
            self.direccion *= -1

    def draw(self):
        # Dibuja el fantasma según su color
        if self.color == "rojo":
            sprite = FANTASMA_ROJO_ABAJO
        elif self.color == "rosa":
            sprite = FANTASMA_ROSA_ABAJO
        elif self.color == "azul":
            sprite = FANTASMA_AZUL_ABAJO
        elif self.color == "naranja":
            sprite = FANTASMA_NARANJA_ABAJO
        
        pyxel.blt(self.x, self.y, 0, *sprite, 16, 16, colkey=0)

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
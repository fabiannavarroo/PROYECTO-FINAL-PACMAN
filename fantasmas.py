

from constantes import (
    FANTASMA_ROJO_ARIBA, FANTASMA_ROJO_ABAJO, FANTASMA_ROJO_IZQUIERDA, FANTASMA_ROJO_DERECHA,
    FANTASMA_AZUL_ARIBA, FANTASMA_AZUL_ABAJO, FANTASMA_AZUL_IZQUIERDA, FANTASMA_AZUL_DERECHA,
    FANTASMA_NARANJA_ARIBA, FANTASMA_NARANJA_ABAJO, FANTASMA_NARANJA_IZQUIERDA, FANTASMA_NARANJA_DERECHA,
    FANTASMA_ROSA_ARIBA, FANTASMA_ROSA_ABAJO, FANTASMA_ROSA_IZQUIERDA, FANTASMA_ROSA_DERECHA,
)
import pyxel

class Fantasma:
    def __init__(self, x, y, sprites):
        self.x = x
        self.y = y
        self.sprites = sprites  # Diccionario con las direcciones del sprite
        self.direccion_actual = self.sprites["DERECHA"]
        self.velocidad = 1

    def mover(self):
        # Movimiento horizontal básico
        self.x += self.velocidad
        self.direccion_actual = self.sprites["DERECHA"]

        # Cambiar de dirección si alcanza los bordes
        if self.x < 0 or self.x > pyxel.width - 16:
            self.velocidad *= -1
            self.direccion_actual = self.sprites["IZQUIERDA"]

    def draw(self):
        sprite_x, sprite_y = self.direccion_actual
        pyxel.blt(self.x, self.y, 0, sprite_x, sprite_y, 16, 16, colkey=0)

# Subclases para cada fantasma
class FantasmaRojo(Fantasma):
    def __init__(self, x, y):
        sprites = {
            "ARRIBA": FANTASMA_ROJO_ARIBA,
            "ABAJO": FANTASMA_ROJO_ABAJO,
            "IZQUIERDA": FANTASMA_ROJO_IZQUIERDA,
            "DERECHA": FANTASMA_ROJO_DERECHA,
        }
        super().__init__(x, y, sprites)

class FantasmaRosa(Fantasma):
    def __init__(self, x, y):
        sprites = {
            "ARRIBA": FANTASMA_ROSA_ARIBA,
            "ABAJO": FANTASMA_ROSA_ABAJO,
            "IZQUIERDA": FANTASMA_ROSA_IZQUIERDA,
            "DERECHA": FANTASMA_ROSA_DERECHA,
        }
        super().__init__(x, y, sprites)

class FantasmaAzul(Fantasma):
    def __init__(self, x, y):
        sprites = {
            "ARRIBA": FANTASMA_AZUL_ARIBA,
            "ABAJO": FANTASMA_AZUL_ABAJO,
            "IZQUIERDA": FANTASMA_AZUL_IZQUIERDA,
            "DERECHA": FANTASMA_AZUL_DERECHA,
        }
        super().__init__(x, y, sprites)

class FantasmaNaranja(Fantasma):
    def __init__(self, x, y):
        sprites = {
            "ARRIBA": FANTASMA_NARANJA_ARIBA,
            "ABAJO": FANTASMA_NARANJA_ABAJO,
            "IZQUIERDA": FANTASMA_NARANJA_IZQUIERDA,
            "DERECHA": FANTASMA_NARANJA_DERECHA,
        }
        super().__init__(x, y, sprites)
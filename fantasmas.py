import pyxel
from constantes import FANTASMA_ROJO, FANTASMA_ROSA, FANTASMA_AZUL, FANTASMA_NARANJA, FANTASMAS_ASUSTADOS, REFRESH
import random
import time


class Fantasma:
    def __init__(self, x, y, muro, sprites):
        self.x = x
        self.y = y
        self.muro = muro
        self.sprites = sprites
        self.color_actual = sprites["DERECHA"]  # Color inicial basado en la dirección
        self.asustado = False
        self.tiempo_asustado = 0

    def activar_asustado(self):
        self.asustado = True
        self.tiempo_asustado = time.time()
        self.color_actual = FANTASMAS_ASUSTADOS["AZUL"]["Coordenadas"]  # Cambiar a color asustado

    def actualizar_estado(self):
        if self.asustado and time.time() - self.tiempo_asustado > 6:
            self.asustado = False
            self.color_actual = self.sprites["DERECHA"]  # Volver al color inicial

    def draw(self):
        # Dibujar el fantasma con el color actual
        pyxel.blt(self.x, self.y, 0, *self.color_actual, 16, 16, colkey=0)


# Subclases de los Fantasmas
class FantasmaRojo(Fantasma):
    def __init__(self, x, y, muro):
        super().__init__(x, y, FANTASMA_ROJO, muro)


class FantasmaRosa(Fantasma):
    def __init__(self, x, y, muro):
        super().__init__(x, y, FANTASMA_ROSA, muro)


class FantasmaAzul(Fantasma):
    def __init__(self, x, y, muro):
        super().__init__(x, y, FANTASMA_AZUL, muro)


class FantasmaNaranja(Fantasma):
    def __init__(self, x, y, muro):
        super().__init__(x, y, FANTASMA_NARANJA, muro)
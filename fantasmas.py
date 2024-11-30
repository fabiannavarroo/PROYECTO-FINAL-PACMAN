import pyxel
from constantes import FANTASMA_ROJO, FANTASMA_ROSA, FANTASMA_AZUL, FANTASMA_NARANJA, FANTASMAS_ASUSTADOS, REFRESH
import random
import time


class Fantasma:
    def __init__(self, x, y, sprites, muro):
        self.x = x
        self.y = y
        self.sprites = sprites  # Imágenes de los fantasmas
        self.muro = muro  # Referencia a la clase Muro
        self.velocidad = 1.5  # Velocidad de los fantasmas
        self.direccion_actual = "DERECHA"  # Comienza moviéndose hacia la derecha
        self.color_actual = sprites["DERECHA"]  # Color inicial basado en la dirección


    def draw(self):
        sprite_x, sprite_y = self.color_actual
        pyxel.blt(self.x, self.y, 0, sprite_x, sprite_y, 16, 16, colkey=0)
    

    import time

class Fantasma:
    def __init__(self, x, y, muro, color_original):
        self.x = x
        self.y = y
        self.muro = muro
        self.color_original = color_original
        self.asustado = False
        self.tiempo_asustado = 0

    def activar_asustado(self):
        self.asustado = True
        self.tiempo_asustado = time.time()

    def actualizar_estado(self):
        if self.asustado and time.time() - self.tiempo_asustado > 6:
            self.asustado = False

    def draw(self):
        color = FANTASMAS_ASUSTADOS["AZUL"]["Coordenadas"] if self.asustado else self.color_original
        # Lógica para dibujar el fantasma con su color correspondiente


# Subclases específicas
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
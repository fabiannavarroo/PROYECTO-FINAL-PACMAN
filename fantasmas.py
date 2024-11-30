import pyxel
from constantes import *
import random
import time


class Fantasma:
    def __init__(self, x, y, muro, sprites):
        self.x = x
        self.y = y
        self.muro = muro
        self.sprites = sprites
        self.color_actual = sprites["DERECHA"]  # Inicializar color según dirección
        self.direccion_actual = "DERECHA"  # Dirección inicial
        self.asustado = False
        self.tiempo_asustado = 0
        self.animacion_asustado = False
        self.en_trampa = False
        self.tiempo_en_trampa = 0


    def activar_asustado(self):
        self.asustado = True
        self.tiempo_asustado = time.time()
        self.animacion_asustado = True  # Activar animación
        self.color_actual = FANTASMAS_ASUSTADOS["AZUL"]["Coordenadas"]


    def volver_a_trampa(self):
        self.en_trampa = True
        self.x, self.y = 192, 192  # Coordenadas en la trampa

    def ocultar(self):
        self.x, self.y = -100, -100  # Sacar del mapa

    def mover(self):
        if not self.en_trampa:
            # Lógica de movimiento aquí
            pass


    def actualizar_estado(self):
        if self.asustado and time.time() - self.tiempo_asustado > 6:
            self.asustado = False
            self.color_actual = self.sprites[self.direccion_actual]

        if self.en_trampa and time.time() - self.tiempo_en_trampa > 5:
            self.en_trampa = False  # El fantasma sale de la trampa


    def draw(self):
        # Dibujar el fantasma con el color actual
        pyxel.blt(self.x, self.y, 0, self.color_actual[0], self.color_actual[1], 16, 16, colkey=0)

# Subclases de Fantasma
class FantasmaRojo(Fantasma):
    def __init__(self, x, y, muro):
        super().__init__(x, y, muro, FANTASMA_ROJO)

class FantasmaRosa(Fantasma):
    def __init__(self, x, y, muro):
        super().__init__(x, y, muro, FANTASMA_ROSA)

class FantasmaAzul(Fantasma):
    def __init__(self, x, y, muro):
        super().__init__(x, y, muro, FANTASMA_AZUL)

class FantasmaNaranja(Fantasma):
    def __init__(self, x, y, muro):
        super().__init__(x, y, muro, FANTASMA_NARANJA)
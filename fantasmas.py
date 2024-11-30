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

    def actualizar_estado(self):
        if self.asustado:
            # Alternar entre azul y blanco durante el estado asustado
            if pyxel.frame_count // REFRESH % 2 == 0:
                self.color_actual = FANTASMAS_ASUSTADOS["AZUL"]["Coordenadas"]
            else:
                self.color_actual = FANTASMAS_ASUSTADOS["BLANCO"]["Coordenadas"]

            # Verificar si el tiempo del estado asustado terminó
            if time.time() - self.tiempo_asustado > 6:
                self.asustado = False
                self.animacion_asustado = False
                # Restaurar el color original según la dirección actual
                self.color_actual = self.sprites[self.direccion_actual]

    def mover(self):
        # Lógica de movimiento y cambio de dirección
        pass

    def draw(self):
        # Dibujar el fantasma con el color actual
        pyxel.blt(self.x, self.y, 0, self.color_actual[0][1], 16, 16, colkey=0)

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
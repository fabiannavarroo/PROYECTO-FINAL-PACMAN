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
        self.color_actual = sprites["DERECHA"]  # Inicializa el color/dirección como "DERECHA"
        self.direccion_actual = "DERECHA"  # Dirección inicial
        self.asustado = False
        self.tiempo_asustado = 0

    def mover(self):
        # Movimiento aleatorio
        opciones_direccion = ["ARRIBA", "ABAJO", "IZQUIERDA", "DERECHA"]
        self.direccion_actual = random.choice(opciones_direccion)

        nueva_x, nueva_y = self.x, self.y

        if self.direccion_actual == "ARRIBA" and not self.muro.colision(self.x, self.y - 1):
            nueva_y -= 1
        elif self.direccion_actual == "ABAJO" and not self.muro.colision(self.x, self.y + 1):
            nueva_y += 1
        elif self.direccion_actual == "IZQUIERDA" and not self.muro.colision(self.x - 1, self.y):
            nueva_x -= 1
        elif self.direccion_actual == "DERECHA" and not self.muro.colision(self.x + 1, self.y):
            nueva_x += 1

        self.x, self.y = nueva_x, nueva_y

        # Actualizar el sprite según la dirección
        if not self.asustado:
            self.color_actual = self.sprites[self.direccion_actual]

    def activar_asustado(self):
        self.asustado = True
        self.tiempo_asustado = time.time()
        if pyxel.frame_count // REFRESH % 2 == 0:
            self.color_actual = FANTASMAS_ASUSTADOS["AZUL"]["Coordenadas"]  # Cambiar a color asustado
        else:
            self.color_actual = FANTASMAS_ASUSTADOS["BLANCO"]["Coordenadas"]  # Cambiar a color asustado


    def actualizar_estado(self):
        if self.asustado and time.time() - self.tiempo_asustado > 6:
            self.asustado = False
            self.color_actual = self.sprites[self.direccion_actual]  # Restaurar imagen según la dirección

    def draw(self):
        # Dibujar el fantasma con el sprite correspondiente
        pyxel.blt(self.x, self.y, 0, self.color_actual, 16, 16, colkey=0)


# Subclases de los Fantasmas
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
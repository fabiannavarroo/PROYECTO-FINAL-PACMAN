import pyxel
from constantes import FANTASMA_ROJO, FANTASMA_ROSA, FANTASMA_AZUL, FANTASMA_NARANJA, FANTASMAS_ASUSTADOS, REFRESH
import random


class Fantasma:
    def __init__(self, x, y, sprites, muro):
        self.x = x
        self.y = y
        self.sprites = sprites  # Imágenes de los fantasmas
        self.muro = muro  # Referencia a la clase Muro
        self.velocidad = 1.5  # Velocidad de los fantasmas
        self.direccion_actual = "DERECHA"  # Comienza moviéndose hacia la derecha
        self.asustado = False  # Indica si está en modo asustado
        self.color_actual = sprites["DERECHA"]  # Color inicial basado en la dirección
        self.tiempo_asustado = 0  # Duración restante del modo asustado en frames

    def activar_modo_asustado(self):
        self.asustado = True
        self.color_actual = FANTASMAS_ASUSTADOS["AZUL"]["Coordenadas"]
        self.tiempo_asustado = 7 * 30  # 7 segundos a 30 FPS

    def desactivar_modo_asustado(self):
        self.asustado = False
        self.color_actual = self.sprites["DERECHA"]  # Restaurar al color normal

    def cambiar_color_asustado(self):
        # Alternar entre azul y blanco si está asustado
        if pyxel.frame_count // REFRESH % 2 == 0:  # Últimos 2 segundos
            self.color_actual == FANTASMAS_ASUSTADOS["AZUL"]["Coordenadas"]
        else:
            self.color_actual = FANTASMAS_ASUSTADOS["BLANCO"]["Coordenadas"]

    def cambiar_direccion(self):
        # Direcciones posibles
        DIRECCIONES = ["ARRIBA", "ABAJO", "DERECHA", "IZQUIERDA"]
        self.direccion_actual = random.choice(DIRECCIONES)  # Escoge una nueva dirección aleatoria

    def update(self):
        # Actualizar el estado del modo asustado
        if self.asustado:
            self.tiempo_asustado -= 1
            if self.tiempo_asustado <= 0:
                self.desactivar_modo_asustado()
            elif self.tiempo_asustado <= 2 * 30:  # Alternar color en los últimos 2 segundos
                self.toggle_asustado_color()

    def draw(self):
        sprite_x, sprite_y = self.color_actual
        pyxel.blt(self.x, self.y, 0, sprite_x, sprite_y, 16, 16, colkey=0)


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
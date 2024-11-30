import pyxel
from constantes import FANTASMA_ROJO, FANTASMA_ROSA, FANTASMA_AZUL, FANTASMA_NARANJA, FANTASMAS_ASUSTADOS
import random


class Fantasma:
    def __init__(self, x, y, sprites, muro):
        self.x = x
        self.y = y
        self.sprites = sprites  # Imágenes de los fantasmas
        self.muro = muro  # Referencia a la clase Muro
        self.velocidad = 1.5  # Velocidad de los fantasmas
        self.direccion_actual = "DERECHA"  # Comienza moviéndose hacia la derecha
        self.modo_asustado = False  # Los fantasmas no están asustados al principio
        self.tiempo_modo_asustado = 0  # Duración restante del modo asustado en frames

    def cambiar_direccion(self):
        # Direcciones posibles
        DIRECCIONES = ["ARRIBA", "ABAJO", "DERECHA", "IZQUIERDA"]
        self.direccion_actual = random.choice(DIRECCIONES)  # Escoge una nueva dirección aleatoria

    def activar_modo_asustado(self):
        self.modo_asustado = True
        self.tiempo_asustado = 7 * 30  # 7 segundos a 30 FPS

    def desactivar_modo_asustado(self):
        self.modo_asustado = False
        self.tiempo_asustado = 0  # Resetear el tiempo restante

    def draw(self):
        if self.modo_asustado:
            if self.tiempo_modo_asustado <= 2 * 30:  # Últimos 2 segundos en frames
                # Alternar entre azul y blanco
                if pyxel.frame_count % 10 < 5:
                    sprite_x, sprite_y = FANTASMAS_ASUSTADOS["AZUL"]["Coordenadas"]
                else:
                    sprite_x, sprite_y = FANTASMAS_ASUSTADOS["BLANCO"]["Coordenadas"]
            else:
                # Dibujar en azul (asustado)
                sprite_x, sprite_y = FANTASMAS_ASUSTADOS["AZUL"]["Coordenadas"]
        else:
            # Dibujar en su color normal
            sprite_x, sprite_y = self.sprites[self.direccion_actual]

        pyxel.blt(self.x, self.y, 0, sprite_x, sprite_y, 16, 16, colkey=0)

    def update(self):
        # Actualizar el estado del modo asustado
        if self.modo_asustado:
            self.tiempo_modo_asustado -= 1
            if self.tiempo_modo_asustado <= 0:
                self.desactivar_modo_asustado()


class FantasmaRojo:
    def __init__(self, x, y, muro):
        self.x = x
        self.y = y
        self.muro = muro
        self.asustado = False
        self.color_actual = FANTASMAS_ASUSTADOS["AZUL"]["Coordenadas"]

    def activar_modo_asustado(self):
        self.asustado = True
        self.color_actual = FANTASMAS_ASUSTADOS["AZUL"]["Coordenadas"]

    def desactivar_modo_asustado(self):
        self.asustado = False
        # Restaurar al color normal del fantasma
        self.color_actual = FANTASMA_ROJO["DERECHA"]

    def toggle_asustado_color(self):
        # Alternar entre azul y blanco si está asustado
        if self.asustado:
            if self.color_actual == FANTASMAS_ASUSTADOS["AZUL"]["Coordenadas"]:
                self.color_actual = FANTASMAS_ASUSTADOS["BLANCO"]["Coordenadas"]
            else:
                self.color_actual = FANTASMAS_ASUSTADOS["AZUL"]["Coordenadas"]

    def draw(self):
        sprite_x, sprite_y = self.color_actual
        pyxel.blt(self.x, self.y, 0, sprite_x, sprite_y, 16, 16, colkey=0)


class FantasmaRosa(Fantasma):
    def __init__(self, x, y, muro):
        super().__init__(x, y, FANTASMA_ROSA, muro)


class FantasmaAzul(Fantasma):
    def __init__(self, x, y, muro):
        super().__init__(x, y, FANTASMA_AZUL, muro)


class FantasmaNaranja(Fantasma):
    def __init__(self, x, y, muro):
        super().__init__(x, y, FANTASMA_NARANJA, muro)
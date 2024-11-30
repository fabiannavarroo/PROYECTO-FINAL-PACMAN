import pyxel
from constantes import *
import time


class Fantasma:
    def __init__(self, x, y, muro, sprites):
        self.x = x
        self.y = y
        self.muro = muro
        self.sprites = sprites
        self.direccion_actual = "DERECHA"  # Dirección inicial
        self.asustado = False
        self.tiempo_asustado = 0
        self.tiempo_para_ser_comido = 10  # Tiempo para el estado asustado
        self.en_trampa = False

    def activar_asustado(self, duracion=None):
        # Activar el estado asustado
        self.asustado = True
        self.tiempo_asustado = time.time()

    def volver_a_trampa(self):
        # Envía al fantasma a su posición inicial según su clase
        self.en_trampa = True
        if isinstance(self, FantasmaRojo):
            self.x, self.y = 200, 160
        elif isinstance(self, FantasmaRosa):
            self.x, self.y = 176, 190
        elif isinstance(self, FantasmaAzul):
            self.x, self.y = 192, 190
        elif isinstance(self, FantasmaNaranja):
            self.x, self.y = 208, 190
        self.asustado = False  # Dejar de estar asustado al regresar a la trampa

    def actualizar_estado(self):
        # Cambia el estado asustado
        if self.asustado:
            tiempo_restante = self.tiempo_para_ser_comido - (time.time() - self.tiempo_asustado)
            if tiempo_restante <= 0:
                self.asustado = False  # El estado asustado termina

    def draw(self):
        # Dibujar el fantasma en su estado correspondiente
        if self.asustado:
            # Cambiar entre azul y blanco
            if pyxel.frame_count // REFRESH % 2 == 0:
                sprite = FANTASMAS_ASUSTADOS["AZUL"]["Coordenadas"]
            else:
                sprite = FANTASMAS_ASUSTADOS["BLANCO"]["Coordenadas"]
        else:
            sprite = self.sprites[self.direccion_actual]

        # Dibujar el sprite del fantasma
        pyxel.blt(self.x, self.y, 0, sprite[0], sprite[1], 16, 16, colkey=0)


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
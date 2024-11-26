from constantes import (
    FANTASMA_ROJO_ARIBA, FANTASMA_ROJO_ABAJO, FANTASMA_ROJO_IZQUIERDA, FANTASMA_ROJO_DERECHA,
    FANTASMA_AZUL_ARIBA, FANTASMA_AZUL_ABAJO, FANTASMA_AZUL_IZQUIERDA, FANTASMA_AZUL_DERECHA,
    FANTASMA_NARANJA_ARIBA, FANTASMA_NARANJA_ABAJO, FANTASMA_NARANJA_IZQUIERDA, FANTASMA_NARANJA_DERECHA,
    FANTASMA_ROSA_ARIBA, FANTASMA_ROSA_ABAJO, FANTASMA_ROSA_IZQUIERDA, FANTASMA_ROSA_DERECHA,
)
import pyxel

class Fantasma:
    def __init__(self, x, y, sprites, muro):
        self.x = x
        self.y = y
        self.sprites = sprites  # Diccionario con las direcciones del sprite
        self.direccion_actual = self.sprites["DERECHA"]
        self.velocidad = 1.5
        self.muro = muro  # Referencia al muro para verificar colisiones
        self.en_trampa = True  # Indica si el fantasma está en la trampa

    def mover(self):
        nueva_x, nueva_y = self.x, self.y

        # Lógica de movimiento básico (puedes implementar IA avanzada)
        if pyxel.frame_count % 60 < 30:  # Alternar entre direcciones
            nueva_x += self.velocidad
            self.direccion_actual = self.sprites["DERECHA"]
        else:
            nueva_x -= self.velocidad
            self.direccion_actual = self.sprites["IZQUIERDA"]

        # Colisión con muros
        if not self.muro.colision(nueva_x, self.y) or (self.en_trampa and self.puede_salir(nueva_x, self.y)):
            self.x = nueva_x
        if not self.muro.colision(self.x, nueva_y):
            self.y = nueva_y

        # Actualiza el estado de si está en la trampa
        if self.en_trampa and not self.muro.colision(self.x, self.y):
            self.en_trampa = False  # Sale de la trampa y no puede volver a entrar

    def puede_salir(self, x, y):
        """
        Permite que el fantasma atraviese la puerta de la trampa.
        """
        puerta_fila = 9  # Fila de la puerta de salida
        puerta_columna = 12  # Columna de la puerta de salida
        fila = y // self.muro.celda_tamaño
        columna = x // self.muro.celda_tamaño

        return fila == puerta_fila and columna == puerta_columna

    def draw(self):
        sprite_x, sprite_y = self.direccion_actual
        pyxel.blt(self.x, self.y, 0, sprite_x, sprite_y, 16, 16, colkey=0)


class FantasmaRojo(Fantasma):
    def __init__(self, x, y, muro):
        sprites = {
            "ARRIBA": FANTASMA_ROJO_ARIBA,
            "ABAJO": FANTASMA_ROJO_ABAJO,
            "IZQUIERDA": FANTASMA_ROJO_IZQUIERDA,
            "DERECHA": FANTASMA_ROJO_DERECHA,
        }
        super().__init__(x, y, sprites, muro)

class FantasmaRosa(Fantasma):
    def __init__(self, x, y, muro):
        sprites = {
            "ARRIBA": FANTASMA_ROSA_ARIBA,
            "ABAJO": FANTASMA_ROSA_ABAJO,
            "IZQUIERDA": FANTASMA_ROSA_IZQUIERDA,
            "DERECHA": FANTASMA_ROSA_DERECHA,
        }
        super().__init__(x, y, sprites, muro)

class FantasmaAzul(Fantasma):
    def __init__(self, x, y, muro):
        sprites = {
            "ARRIBA": FANTASMA_AZUL_ARIBA,
            "ABAJO": FANTASMA_AZUL_ABAJO,
            "IZQUIERDA": FANTASMA_AZUL_IZQUIERDA,
            "DERECHA": FANTASMA_AZUL_DERECHA,
        }
        super().__init__(x, y, sprites, muro)

class FantasmaNaranja(Fantasma):
    def __init__(self, x, y, muro):
        sprites = {
            "ARRIBA": FANTASMA_NARANJA_ARIBA,
            "ABAJO": FANTASMA_NARANJA_ABAJO,
            "IZQUIERDA": FANTASMA_NARANJA_IZQUIERDA,
            "DERECHA": FANTASMA_NARANJA_DERECHA,
        }
        super().__init__(x, y, sprites, muro)
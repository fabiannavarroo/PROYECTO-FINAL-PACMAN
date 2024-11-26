import pyxel
from constantes import FANTASMA_ROJO, FANTASMA_ROSA, FANTASMA_AZUL, FANTASMA_NARANJA

class Fantasma:
    def __init__(self, x, y, sprites, muro):
        self.x = x
        self.y = y
        self.sprites = sprites
        self.muro = muro
        self.velocidad = 1
        self.direccion_actual = self.sprites["DERECHA"]
        self.en_trampa = True

    def mover(self):
        if self.en_trampa:
            # Salir de la trampa
            if not self.muro.colision(self.x, self.y - self.velocidad):
                self.y -= self.velocidad
            if self.y < 192:  # Límites de la trampa (ajustar según sea necesario)
                self.en_trampa = False
        else:
            # Movimiento fuera de la trampa
            direcciones = [(self.velocidad, 0), (-self.velocidad, 0), (0, self.velocidad), (0, -self.velocidad)]
            for dx, dy in direcciones:
                nueva_x, nueva_y = self.x + dx, self.y + dy
                if not self.muro.colision(nueva_x, nueva_y):
                    self.x, self.y = nueva_x, nueva_y
                    break

    def draw(self):
        sprite_x, sprite_y = self.direccion_actual
        pyxel.blt(self.x, self.y, 0, sprite_x, sprite_y, 16, 16, colkey=0)

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
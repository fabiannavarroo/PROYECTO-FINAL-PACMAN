import pyxel
from constantes import FANTASMA_ROJO, FANTASMA_ROSA, FANTASMA_AZUL, FANTASMA_NARANJA, PORTALES
import random

class Fantasma:
    def __init__(self, x, y, sprites, muro):
        self.x = x
        self.y = y
        self.sprites = sprites
        self.muro = muro
        self.velocidad = 1
        self.direccion_actual = "DERECHA"  # Comienza moviéndose hacia la derecha
        self.en_trampa = True  # El fantasma empieza en la trampa

    def mover(self):
        if self.en_trampa:
            # Movimiento básico para salir de la trampa
            if not self.muro.colision(self.x, self.y - self.velocidad):
                self.y -= self.velocidad
            if self.y < 192:  # Coordenada límite para salir de la trampa
                self.en_trampa = False
        else:
            # Direcciones básicas: derecha, izquierda, arriba, abajo
            if self.direccion_actual == "DERECHA":
                nueva_x = self.x + self.velocidad
                nueva_y = self.y
                if not self.muro.colision(nueva_x, nueva_y):
                    self.x = nueva_x
                else:
                    self.direccion_actual = random.choice(["ARRIBA", "ABAJO", "IZQUIERDA"])
            elif self.direccion_actual == "IZQUIERDA":
                nueva_x = self.x - self.velocidad
                nueva_y = self.y
                if not self.muro.colision(nueva_x, nueva_y):
                    self.x = nueva_x
                else:
                    self.direccion_actual = random.choice(["ARRIBA", "ABAJO", "DERECHA"])
            elif self.direccion_actual == "ARRIBA":
                nueva_x = self.x
                nueva_y = self.y - self.velocidad
                if not self.muro.colision(nueva_x, nueva_y):
                    self.y = nueva_y
                else:
                    self.direccion_actual = random.choice(["DERECHA", "ABAJO", "IZQUIERDA"])
            elif self.direccion_actual == "ABAJO":
                nueva_x = self.x
                nueva_y = self.y + self.velocidad
                if not self.muro.colision(nueva_x, nueva_y):
                    self.y = nueva_y
                else:
                    self.direccion_actual = random.choice(["DERECHA", "ARRIBA", "IZQUIERDA"])

            # Teletransporte si está en un portal
            if (self.x, self.y) in PORTALES:
                self.x, self.y = PORTALES[(self.x, self.y)]

    def draw(self):
        # Dibujar el sprite del fantasma según su dirección
        sprite_x, sprite_y = self.sprites[self.direccion_actual]
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
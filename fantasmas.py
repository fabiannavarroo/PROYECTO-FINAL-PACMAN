import pyxel
from constantes import FANTASMA_ROJO, FANTASMA_ROSA, FANTASMA_AZUL, FANTASMA_NARANJA,PORTALES
import random


class Fantasma:
    def __init__(self, x, y, sprites, muro):
        self.x = x
        self.y = y
        self.sprites = sprites
        self.muro = muro
        self.velocidad = 1
        self.direccion_actual = "DERECHA"  
        self.en_trampa = True

    def mover(self):
        if self.en_trampa:
            # Movimiento para salir de la trampa
            if not self.muro.colision(self.x, self.y - self.velocidad):
                self.y -= self.velocidad
            if self.y < 192:  # Coordenada para salir de la trampa
                self.en_trampa = False
        else:
            # Obtener las posibles direcciones
            direcciones = {
                "DERECHA": (self.velocidad, 0),
                "IZQUIERDA": (-self.velocidad, 0),
                "ARRIBA": (0, -self.velocidad),
                "ABAJO": (0, self.velocidad),
            }

            # Intentar moverse en la dirección actual
            dx, dy = direcciones[self.direccion_actual]
            nueva_x, nueva_y = self.x + dx, self.y + dy

            # Si hay colisión, elegir una nueva dirección aleatoria válida
            if self.muro.colision(nueva_x, nueva_y):
                direcciones_validas = [
                    direccion
                    for direccion, (dx, dy) in direcciones.items()
                    if not self.muro.colision(self.x + dx, self.y + dy)
                ]
                if direcciones_validas:
                    self.direccion_actual = random.choice(direcciones_validas)
                    dx, dy = direcciones[self.direccion_actual]

            # Actualizar posición
            self.x += dx
            self.y += dy

            #Portal
            if (self.x,self.y)in PORTALES:
                self.x,self.y = PORTALES[(self.x,self.y)]

    def draw(self):
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
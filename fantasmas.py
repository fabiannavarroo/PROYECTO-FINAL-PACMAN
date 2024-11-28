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
        nueva_x, nueva_y = self.x, self.y
        if self.en_trampa:
            #
        else:
            # Obtener las posibles direcciones
            DIRECCIONES = {
                "DERECHA": (self.velocidad, 0),
                "IZQUIERDA": (-self.velocidad, 0),
                "ARRIBA": (0, -self.velocidad),
                "ABAJO": (0, self.velocidad),
            }

            # Intentar moverse en la dirección actual
            

            # Si hay colisión, elegir una nueva dirección aleatoria válida
            

            # Actualizar posición
            if self.direccion_actual == DIRECCIONES["ARRIBA"] and not self.muro.colision(self.x, self.y + DIRECCIONES["ARRIBA"]):
                nueva_y -= self.velocidad
            elif self.direccion_actual == DIRECCIONES["ABAJO"] and not self.muro.colision(self.x, self.y + DIRECCIONES["ABAJO"]):
                nueva_y += self.velocidad
            elif self.direccion_actual == DIRECCIONES["IZQUIERDA"] and not self.muro.colision(self.x, self.y + DIRECCIONES["IZQUIERDA"]):
                nueva_x -= self.velocidad
            elif self.direccion_actual == DIRECCIONES["DERECHA"] and not self.muro.colision(self.x, self.y + DIRECCIONES["DERECHA"]):
                nueva_x += self.velocidad

            #Portal
            if (self.x,self.y)in PORTALES:
                self.x,self.y = PORTALES[(self.x,self.y)]
                
    # Dibujar el sprite del fantasma en la dirección correspondiente.
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
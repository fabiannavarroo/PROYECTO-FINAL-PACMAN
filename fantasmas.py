import pyxel
from constantes import FANTASMA_ROJO, FANTASMA_ROSA, FANTASMA_AZUL, FANTASMA_NARANJA,PORTALES
import random


class Fantasma:
    def __init__(self, x, y, sprites, muro):
        self.x = x
        self.y = y
        self.sprites = sprites  # Imagenes de los fantasmas
        self.muro = muro # Referencia a la clase Muro
        self.velocidad = 1.5  # Velocidad de los fantasmas
        self.direccion_actual = "DERECHA"  # Comienza moviéndose hacia la derecha
        self.en_trampa = True  # El fantasma empieza en la trampa

    #def salir_trampa(self):
    
    def cambiar_direccion(self):
        # Direcciones que puede tener los fantasmas
        DIRECCIONES = ["ARRIBA", "ABAJO", "DERECHA", "IZQUIERDA"]
        nueva_direccion = random.choice(DIRECCIONES) # De forma aleatoria se escoge una direccion
        self.direccion_actual = nueva_direccion # Se le asigna esa direccion a la actual del fantasmas


    # Dibujar el sprite del fantasma en la dirección correspondiente.
    def draw(self):
        sprite_x, sprite_y = self.sprites[self.direccion_actual]
        pyxel.blt(self.x, self.y, 0, sprite_x, sprite_y, 16, 16, colkey=0)

class FantasmaRojo(Fantasma):
    def __init__(self, x, y, muro):
        super().__init__(x, y, FANTASMA_ROJO, muro)

    def mover(self, pacman_x, pacman_y):
        # Calcula la diferencia en X y Y
        diferencia_x = pacman_x - self.x
    diferencia_y = pacman_y - self.y

    # Definir prioridad de movimiento
    if abs(diferencia_x) > abs(diferencia_y):  # Prioridad al eje X
        if diferencia_x > 0 and not self.muro.colision(self.x + self.velocidad, self.y):
            self.x += self.velocidad
            self.direccion_actual = "DERECHA"
        elif diferencia_x < 0 and not self.muro.colision(self.x - self.velocidad, self.y):
            self.x -= self.velocidad
            self.direccion_actual = "IZQUIERDA"
        else:  # Si no puede moverse en X, intenta en Y
            if diferencia_y > 0 and not self.muro.colision(self.x, self.y + self.velocidad):
                self.y += self.velocidad
                self.direccion_actual = "ABAJO"
            elif diferencia_y < 0 and not self.muro.colision(self.x, self.y - self.velocidad):
                self.y -= self.velocidad
                self.direccion_actual = "ARRIBA"
    else:  # Prioridad al eje Y
        if diferencia_y > 0 and not self.muro.colision(self.x, self.y + self.velocidad):
            self.y += self.velocidad
            self.direccion_actual = "ABAJO"
        elif diferencia_y < 0 and not self.muro.colision(self.x, self.y - self.velocidad):
            self.y -= self.velocidad
            self.direccion_actual = "ARRIBA"
        else:  # Si no puede moverse en Y, intenta en X
            if diferencia_x > 0 and not self.muro.colision(self.x + self.velocidad, self.y):
                self.x += self.velocidad
                self.direccion_actual = "DERECHA"
            elif diferencia_x < 0 and not self.muro.colision(self.x - self.velocidad, self.y):
                self.x -= self.velocidad
                self.direccion_actual = "IZQUIERDA"

    # Si no puede moverse en ninguna dirección, cambia de dirección aleatoria
    if self.direccion_actual == "":
        self.cambiar_direccion()        

class FantasmaRosa(Fantasma):
    def __init__(self, x, y, muro):
        super().__init__(x, y, FANTASMA_ROSA, muro)

class FantasmaAzul(Fantasma):
    def __init__(self, x, y, muro):
        super().__init__(x, y, FANTASMA_AZUL, muro)

class FantasmaNaranja(Fantasma):
    def __init__(self, x, y, muro):
        super().__init__(x, y, FANTASMA_NARANJA, muro)
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
        # Calcula las diferencias entre las posiciones del fantasma y Pac-Man
        diferencia_x = pacman_x - self.x
        diferencia_y = pacman_y - self.y

        # Determina la dirección preferida
        if abs(diferencia_x) > abs(diferencia_y):
            # Prioriza el movimiento en el eje X
            if diferencia_x > 0:  # Pac-Man está a la derecha
                nueva_x = self.x + self.velocidad
                if not self.muro.colision(nueva_x, self.y):
                    self.x = nueva_x
                    self.direccion_actual = "DERECHA"
                else:
                    # Si hay colisión, intenta mover en Y
                    self.intentar_mover_en_y(diferencia_y)
            else:  # Pac-Man está a la izquierda
                nueva_x = self.x - self.velocidad
                if not self.muro.colision(nueva_x, self.y):
                    self.x = nueva_x
                    self.direccion_actual = "IZQUIERDA"
                else:
                    # Si hay colisión, intenta mover en Y
                    self.intentar_mover_en_y(diferencia_y)
        else:
            # Prioriza el movimiento en el eje Y
            if diferencia_y > 0:  # Pac-Man está abajo
                nueva_y = self.y + self.velocidad
                if not self.muro.colision(self.x, nueva_y):
                    self.y = nueva_y
                    self.direccion_actual = "ABAJO"
                else:
                    # Si hay colisión, intenta mover en X
                    self.intentar_mover_en_x(diferencia_x)
            else:  # Pac-Man está arriba
                nueva_y = self.y - self.velocidad
                if not self.muro.colision(self.x, nueva_y):
                    self.y = nueva_y
                    self.direccion_actual = "ARRIBA"
                else:
                    # Si hay colisión, intenta mover en X
                    self.intentar_mover_en_x(diferencia_x)

    def intentar_mover_en_y(self, diferencia_y):
        if diferencia_y > 0:  # Pac-Man está abajo
            nueva_y = self.y + self.velocidad
            if not self.muro.colision(self.x, nueva_y):
                self.y = nueva_y
                self.direccion_actual = "ABAJO"
        else:  # Pac-Man está arriba
            nueva_y = self.y - self.velocidad
            if not self.muro.colision(self.x, nueva_y):
                self.y = nueva_y
                self.direccion_actual = "ARRIBA"

    def intentar_mover_en_x(self, diferencia_x):
        if diferencia_x > 0:  # Pac-Man está a la derecha
            nueva_x = self.x + self.velocidad
            if not self.muro.colision(nueva_x, self.y):
                self.x = nueva_x
                self.direccion_actual = "DERECHA"
        else:  # Pac-Man está a la izquierda
            nueva_x = self.x - self.velocidad
            if not self.muro.colision(nueva_x, self.y):
                self.x = nueva_x
                self.direccion_actual = "IZQUIERDA"

class FantasmaRosa(Fantasma):
    def __init__(self, x, y, muro):
        super().__init__(x, y, FANTASMA_ROSA, muro)

class FantasmaAzul(Fantasma):
    def __init__(self, x, y, muro):
        super().__init__(x, y, FANTASMA_AZUL, muro)

class FantasmaNaranja(Fantasma):
    def __init__(self, x, y, muro):
        super().__init__(x, y, FANTASMA_NARANJA, muro)
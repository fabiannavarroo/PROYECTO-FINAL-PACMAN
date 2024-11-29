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

        # Si las diferencias son muy pequeñas, ajustar para garantizar precisión
        if abs(diferencia_x) < self.velocidad:
            diferencia_x = 0
        if abs(diferencia_y) < self.velocidad:
            diferencia_y = 0

        # Direcciones posibles y sus respectivas coordenadas de movimiento
        direcciones = {
            "DERECHA": (self.x + self.velocidad, self.y),
            "IZQUIERDA": (self.x - self.velocidad, self.y),
            "ARRIBA": (self.x, self.y - self.velocidad),
            "ABAJO": (self.x, self.y + self.velocidad),
        }

        # Ordenar las direcciones por proximidad a Pac-Man
        direcciones_ordenadas = sorted(
            direcciones.items(),
            key=lambda d: abs(pacman_x - d[1][0]) + abs(pacman_y - d[1][1])
        )

        # Intentar moverse en la dirección más cercana
        for direccion, (nueva_x, nueva_y) in direcciones_ordenadas:
            if not self.muro.colision(nueva_x, nueva_y):  # Si la dirección es transitable
                self.x, self.y = nueva_x, nueva_y
                self.direccion_actual = direccion
                return

        # Si todas las direcciones están bloqueadas, recalcular dirección
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
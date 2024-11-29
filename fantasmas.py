import pyxel
from constantes import FANTASMA_ROJO, FANTASMA_ROSA, FANTASMA_AZUL, FANTASMA_NARANJA, PORTALES
import random


class Fantasma:
    def __init__(self, x, y, sprites, muro, pacman):
        self.x = x
        self.y = y
        self.sprites = sprites  # Imágenes de los fantasmas
        self.muro = muro  # Referencia a la clase Muro
        self.pacman = pacman  # Referencia a Pac-Man
        self.velocidad = 1.5  # Velocidad de los fantasmas
        self.direccion_actual = "DERECHA"  # Dirección inicial
        self.en_trampa = True  # El fantasma empieza en la trampa

    def cambiar_direccion(self):
        # Direcciones que puede tomar el fantasma
        DIRECCIONES = ["ARRIBA", "ABAJO", "DERECHA", "IZQUIERDA"]
        nueva_direccion = random.choice(DIRECCIONES)  # Elegir una dirección aleatoria
        self.direccion_actual = nueva_direccion

    def mover_aleatorio(self):
        # Movimiento aleatorio si no se persigue a Pac-Man
        direcciones = {
            "ARRIBA": (self.x, self.y - self.velocidad),
            "ABAJO": (self.x, self.y + self.velocidad),
            "IZQUIERDA": (self.x - self.velocidad, self.y),
            "DERECHA": (self.x + self.velocidad, self.y)
        }

        # Verificar colisiones y mover en una dirección aleatoria válida
        direcciones_validas = {
            d: (nx, ny)
            for d, (nx, ny) in direcciones.items()
            if not self.muro.colision(nx, ny)
        }

        if direcciones_validas:
            self.direccion_actual, (self.x, self.y) = random.choice(list(direcciones_validas.items()))

    def draw(self):
        # Dibujar el sprite del fantasma
        sprite_x, sprite_y = self.sprites[self.direccion_actual]
        pyxel.blt(self.x, self.y, 0, sprite_x, sprite_y, 16, 16, colkey=0)


class FantasmaRojo(Fantasma):
    def __init__(self, x, y, muro, pacman):
        super().__init__(x, y, FANTASMA_ROJO, muro, pacman)

    def mover(self):
        # Coordenadas de Pac-Man
        pacman_x, pacman_y = self.pacman.x, self.pacman.y

        # Diferencias entre las posiciones del fantasma y Pac-Man
        diferencia_x = pacman_x - self.x
        diferencia_y = pacman_y - self.y

        # Lógica de persecución: eje prioritario según la distancia mayor
        if abs(diferencia_x) > abs(diferencia_y):  # Priorizar movimiento horizontal
            if diferencia_x > 0:  # Pac-Man está a la derecha
                nueva_x = self.x + self.velocidad
                if not self.muro.colision(nueva_x, self.y):  # Sin colisión
                    self.x = nueva_x
                    self.direccion_actual = "DERECHA"
                else:
                    self.mover_aleatorio()  # Si está bloqueado, moverse aleatoriamente
            else:  # Pac-Man está a la izquierda
                nueva_x = self.x - self.velocidad
                if not self.muro.colision(nueva_x, self.y):
                    self.x = nueva_x
                    self.direccion_actual = "IZQUIERDA"
                else:
                    self.mover_aleatorio()
        else:  # Priorizar movimiento vertical
            if diferencia_y > 0:  # Pac-Man está abajo
                nueva_y = self.y + self.velocidad
                if not self.muro.colision(self.x, nueva_y):
                    self.y = nueva_y
                    self.direccion_actual = "ABAJO"
                else:
                    self.mover_aleatorio()
            else:  # Pac-Man está arriba
                nueva_y = self.y - self.velocidad
                if not self.muro.colision(self.x, nueva_y):
                    self.y = nueva_y
                    self.direccion_actual = "ARRIBA"
                else:
                    self.mover_aleatorio()


class FantasmaRosa(Fantasma):
    def __init__(self, x, y, muro, pacman):
        super().__init__(x, y, FANTASMA_ROSA, muro, pacman)


class FantasmaAzul(Fantasma):
    def __init__(self, x, y, muro, pacman):
        super().__init__(x, y, FANTASMA_AZUL, muro, pacman)


class FantasmaNaranja(Fantasma):
    def __init__(self, x, y, muro, pacman):
        super().__init__(x, y, FANTASMA_NARANJA, muro, pacman)

from constantes import *
import random
import time

class Fantasma:
    def __init__(self, x, y, pacman, bloque):
        self.x = x
        self.y = y
        self.pacman = pacman
        self.bloque = bloque
        self.velocidad = 1.5
        self.asustado = False
        self.direccion = random.choice([PACMAN_ARRIBA, PACMAN_ABAJO, PACMAN_IZQUIERDA, PACMAN_DERECHA])
        self.en_trampa = True
        self.ultimo_movimiento = time.time()
        self.salida_trampa = time.time() + random.randint(2, 8)  # Diferenciar salidas de los fantasmas

    def mover(self):
        if self.en_trampa:
            if time.time() >= self.salida_trampa:
                self.en_trampa = False
            else:
                return  # Mientras están en la trampa, no se mueven
        
        if self.asustado:
            self.mover_asustado()
        else:
            self.mover_normal()

    def mover_asustado(self):
        self.velocidad = 1  # Reducir velocidad
        pacman_dx = self.pacman.x - self.x
        pacman_dy = self.pacman.y - self.y
        if abs(pacman_dx) > abs(pacman_dy):
            self.direccion = PACMAN_IZQUIERDA if pacman_dx > 0 else PACMAN_DERECHA
        else:
            self.direccion = PACMAN_ARRIBA if pacman_dy > 0 else PACMAN_ABAJO

        # Intentar alejarse en la dirección opuesta
        self.mover_en_direccion(opuesta=True)

    def mover_normal(self):
        self.velocidad = 1.5
        self.mover_en_direccion(opuesta=False)

    def mover_en_direccion(self, opuesta=False):
        if time.time() - self.ultimo_movimiento < 1 / self.velocidad:
            return  # Controlar velocidad

        dx, dy = 0, 0
        if self.direccion == PACMAN_ARRIBA:
            dy = -1
        elif self.direccion == PACMAN_ABAJO:
            dy = 1
        elif self.direccion == PACMAN_IZQUIERDA:
            dx = -1
        elif self.direccion == PACMAN_DERECHA:
            dx = 1

        if opuesta:
            dx, dy = -dx, -dy

        nueva_x = self.x + dx * self.velocidad
        nueva_y = self.y + dy * self.velocidad

        if not self.bloque.colision(nueva_x, nueva_y):
            self.x = nueva_x
            self.y = nueva_y

        self.ultimo_movimiento = time.time()

    def activar_asustado(self):
        self.asustado = True

    def desactivar_asustado(self):
        self.asustado = False

    def volver_a_trampa(self):
        self.x, self.y = 192, 192  # Posición dentro de la trampa
        self.en_trampa = True
        self.salida_trampa = time.time() + random.randint(2, 5)

class FantasmaRojo(Fantasma):
    def mover_normal(self):
        # Perseguir directamente a Pac-Man
        pacman_dx = self.pacman.x - self.x
        pacman_dy = self.pacman.y - self.y
        if abs(pacman_dx) > abs(pacman_dy):
            self.direccion = PACMAN_IZQUIERDA if pacman_dx < 0 else PACMAN_DERECHA
        else:
            self.direccion = PACMAN_ARRIBA if pacman_dy < 0 else PACMAN_ABAJO
        super().mover_normal()

class FantasmaRosa(Fantasma):
    def mover_normal(self):
        # Intentar emboscar moviéndose adelante de Pac-Man
        pacman_dx = self.pacman.x - self.x
        pacman_dy = self.pacman.y - self.y
        if abs(pacman_dx) > abs(pacman_dy):
            self.direccion = PACMAN_DERECHA if self.pacman.direccion_actual == PACMAN_DERECHA else PACMAN_IZQUIERDA
        else:
            self.direccion = PACMAN_ABAJO if self.pacman.direccion_actual == PACMAN_ABAJO else PACMAN_ARRIBA
        super().mover_normal()

class FantasmaAzul(Fantasma):
    def mover_normal(self):
        # Movimiento errático
        if random.random() < 0.5:
            pacman_dx = self.pacman.x - self.x
            pacman_dy = self.pacman.y - self.y
            if abs(pacman_dx) > abs(pacman_dy):
                self.direccion = PACMAN_IZQUIERDA if pacman_dx > 0 else PACMAN_DERECHA
            else:
                self.direccion = PACMAN_ARRIBA if pacman_dy > 0 else PACMAN_ABAJO
        else:
            self.direccion = random.choice([PACMAN_ARRIBA, PACMAN_ABAJO, PACMAN_IZQUIERDA, PACMAN_DERECHA])
        super().mover_normal()

class FantasmaNaranja(Fantasma):
    def mover_normal(self):
        # Movimiento aleatorio o hacia Pac-Man
        if random.random() < 0.3:
            pacman_dx = self.pacman.x - self.x
            pacman_dy = self.pacman.y - self.y
            if abs(pacman_dx) > abs(pacman_dy):
                self.direccion = PACMAN_IZQUIERDA if pacman_dx < 0 else PACMAN_DERECHA
            else:
                self.direccion = PACMAN_ARRIBA if pacman_dy < 0 else PACMAN_ABAJO
        else:
            self.direccion = random.choice([PACMAN_ARRIBA, PACMAN_ABAJO, PACMAN_IZQUIERDA, PACMAN_DERECHA])
        super().mover_normal()

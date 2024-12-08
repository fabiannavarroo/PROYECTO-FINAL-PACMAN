import pyxel
from constantes import *
import random  
import time


class Fantasma:
    def __init__(self, x, y, sprites, bloque, pacman):
        self.x = x
        self.y = y
        self.velocidad = 1.5
        self.x_inicial = x  # Guardar posición inicial
        self.y_inicial = y  # Guardar posición inicial
        self.sprites = sprites
        self.bloque = bloque  # Referencia al mapa del juego
        self.pacman = pacman  # Referencia a Pac-Man
        self.direccion_actual = None  # Dirección actual del fantasma
        self.asustado = False  # Indica si el fantasma está en estado asustado
        self.en_trampa = True  # Indica si el fantasma está atrapado
        self.tiempo_trampa = time.time()  # Temporizador inicial para salir de la trampa
        self.tiempo_asustado = 0  # Temporizador para estado asustado
        self.tiempo_para_salir = 3  # Tiempo que el fantasma debe esperar para salir de la trampa

    def activar_asustado(self):
        # Activa el estado asustado del fantasma
        self.asustado = True
        self.tiempo_asustado = time.time()

    def volver_a_trampa(self):
        # Enviar al fantasma de vuelta a la trampa
        self.en_trampa = True
        self.x, self.y = self.x_inicial, self.y_inicial
        self.asustado = False
        self.tiempo_trampa = time.time()  # Reiniciar el temporizador de trampa

    def mover_fuera_de_trampa(self):
        # Maneja la salida de la trampa después de esperar el tiempo necesario
        if time.time() - self.tiempo_trampa >= self.tiempo_para_salir:
            self.en_trampa = False
        else:
            # Mantenerse dentro de la trampa
            return

    def mover(self):
        pass  # Este método será sobrescrito en cada subclase según su lógica

    def draw(self):
        # Dibuja al fantasma, alternando sprites si está asustado
        if self.asustado:
            if pyxel.frame_count // REFRESH % 2 == 0:
                sprite = FANTASMAS_ASUSTADOS["AZUL"]["Coordenadas"]
            else:
                sprite = FANTASMAS_ASUSTADOS["BLANCO"]["Coordenadas"]
        else:
            sprite = self.sprites[self.direccion_actual]  # Seleccionar sprite según dirección

        pyxel.blt(self.x, self.y, 0, sprite[0], sprite[1], 16, 16, colkey=0)

    def mover_en_direccion(self, dx, dy):
        # Lógica básica de movimiento hacia Pac-Man con detección de colisiones
        if abs(dx) > abs(dy):
            # Priorizar el movimiento horizontal
            if dx > 0 and not self.bloque.colision(self.x + self.velocidad, self.y):
                self.x += self.velocidad
                self.direccion_actual = "DERECHA"
            elif dx < 0 and not self.bloque.colision(self.x - self.velocidad, self.y):
                self.x -= self.velocidad
                self.direccion_actual = "IZQUIERDA"
        else:
            # Priorizar el movimiento vertical
            if dy > 0 and not self.bloque.colision(self.x, self.y + self.velocidad):
                self.y += self.velocidad
                self.direccion_actual = "ABAJO"
            elif dy < 0 and not self.bloque.colision(self.x, self.y - self.velocidad):
                self.y -= self.velocidad
                self.direccion_actual = "ARRIBA"

# Fantasma Rojo: Persigue directamente a Pac-Man
class FantasmaRojo(Fantasma):
    def mover(self):
        if self.en_trampa:
            self.mover_fuera_de_trampa()
        else:
            dx, dy = self.pacman.x - self.x, self.pacman.y - self.y
            self.mover_en_direccion(dx, dy)

# Fantasma Rosa: Intenta anticipar los movimientos de Pac-Man
class FantasmaRosa(Fantasma):
    def mover(self):
        if self.en_trampa:
            self.mover_fuera_de_trampa()
        else:
            # Predecir la posición futura de Pac-Man en base a su dirección actual
            pred_x = self.pacman.x + 16 * PACMAN_DIRECCION[self.pacman.direccion_actual][0]
            pred_y = self.pacman.y + 16 * PACMAN_DIRECCION[self.pacman.direccion_actual][1]
            dx, dy = pred_x - self.x, pred_y - self.y
            self.mover_en_direccion(dx, dy)

# Fantasma Azul: Movimiento errático
class FantasmaAzul(Fantasma):
    def mover(self):
        if self.en_trampa:
            self.mover_fuera_de_trampa()
        else:
            if random.random() < 0.5:
                dx, dy = self.pacman.x - self.x, self.pacman.y - self.y
            else:
                dx, dy = random.choice([(16, 0), (0, 16), (-16, 0), (0, -16)])
            self.mover_en_direccion(dx, dy)

# Fantasma Naranja: Movimiento aleatorio con tendencia hacia Pac-Man
class FantasmaNaranja(Fantasma):
    def mover(self):
        if self.en_trampa:
            self.mover_fuera_de_trampa()
        else:
            if random.random() < 0.3:  # Alejarse de Pac-Man
                dx, dy = -(self.pacman.x - self.x), -(self.pacman.y - self.y)
            else:  # Acercarse a Pac-Man
                dx, dy = self.pacman.x - self.x, self.pacman.y - self.y
            self.mover_en_direccion(dx, dy)
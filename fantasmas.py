import pyxel
from constantes import *
import random  
import time

class Fantasma:
    def __init__(self, x, y, sprites):
        self.x = x
        self.y = y
        self.velocidad = 1.5
        self.x_inicial = x  # Guardar posición inicial
        self.y_inicial = y  # Guardar posición inicial
        self.sprites = sprites
        self.direccion_actual = "DERECHA"  # Dirección inicial
        self.asustado = False  # Indica si está en estado asustado
        self.tiempo_asustado = 0  # Temporizador para estado asustado
        self.tiempo_para_ser_comido = 10  # Duración por defecto del estado asustado
        self.en_trampa = False  # Indica si el fantasma está en la trampa


    def activar_asustado(self):
        #Activa el estado asustado
        self.asustado = True
        self.tiempo_asustado = time.time()


    def volver_a_trampa(self):
        # Envía al fantasma a la trampa
        self.en_trampa = True
        if isinstance(self, FantasmaRojo):
            self.x, self.y = 158, 208
        elif isinstance(self, FantasmaRosa):
            self.x, self.y = 181, 208
        elif isinstance(self, FantasmaAzul):
            self.x, self.y = 203, 208
        elif isinstance(self, FantasmaNaranja):
            self.x, self.y = 226, 208
        self.asustado = False  # Sale del estado asustado


    def volver_a_posicion_inicial(self):
        #Restaura la posición inicial del fantasma
        self.x = self.x_inicial
        self.y = self.y_inicial
        self.asustado = False
        self.en_trampa = False


    def actualizar_estado(self):
        #Verifica y actualiza el estado asustado
        if self.asustado:
            self.velocidad = 1
            tiempo_restante = self.tiempo_para_ser_comido - (time.time() - self.tiempo_asustado)
            if tiempo_restante <= 0:
                self.asustado = False  # Finaliza el estado asustado


    def draw(self):
        #Dibuja el fantasma en su estado actual.
        if self.asustado:
            # Alternar entre azul y blanco si está asustado
            if pyxel.frame_count // REFRESH % 2 == 0:
                sprite = FANTASMAS_ASUSTADOS["AZUL"]["Coordenadas"]
            else:
                sprite = FANTASMAS_ASUSTADOS["BLANCO"]["Coordenadas"]
        else:
            sprite = self.sprites[self.direccion_actual]  # Usar sprite según dirección

        # Dibuja el fantasma
        pyxel.blt(self.x, self.y, 0, sprite[0], sprite[1], 16, 16, colkey=0)


# Subclases de Fantasma
class FantasmaRojo(Fantasma):
    def __init__(self, x, y, pacman, bloque):
        super().__init__(x, y, FANTASMA_ROJO)
        self.pacman = pacman
        self.bloque = bloque

    def mover(self):
        if self.pacman.x > self.x and not self.bloque.colision(self.x + self.velocidad, self.y):
            self.x += self.velocidad
        elif self.pacman.x < self.x and not self.bloque.colision(self.x - self.velocidad, self.y):
            self.x -= self.velocidad

        if self.pacman.y > self.y and not self.bloque.colision(self.x, self.y + self.velocidad):
            self.y += self.velocidad
        elif self.pacman.y < self.y and not self.bloque.colision(self.x, self.y - self.velocidad):
            self.y -= self.velocidad


class FantasmaRosa(Fantasma):
    def __init__(self, x, y, pacman, bloque):
        super().__init__(x, y, FANTASMA_ROSA)
        self.pacman = pacman
        self.bloque = bloque

    def mover(self):
        pred_x = self.pacman.x + 16 * (self.pacman.direccion_actual == PACMAN_DERECHA) - 16 * (self.pacman.direccion_actual == PACMAN_IZQUIERDA)
        pred_y = self.pacman.y + 16 * (self.pacman.direccion_actual == PACMAN_ABAJO) - 16 * (self.pacman.direccion_actual == PACMAN_ARRIBA)

        if pred_x > self.x and not self.bloque.colision(self.x + self.velocidad, self.y):
            self.x += self.velocidad
        elif pred_x < self.x and not self.bloque.colision(self.x - self.velocidad, self.y):
            self.x -= self.velocidad

        if pred_y > self.y and not self.bloque.colision(self.x, self.y + self.velocidad):
            self.y += self.velocidad
        elif pred_y < self.y and not self.bloque.colision(self.x, self.y - self.velocidad):
            self.y -= self.velocidad


class FantasmaAzul(Fantasma):
    def __init__(self, x, y, pacman, bloque):
        super().__init__(x, y, FANTASMA_AZUL)
        self.pacman = pacman
        self.bloque = bloque

    def mover(self):
        if random.random() < 0.5:
            if self.pacman.x > self.x and not self.bloque.colision(self.x + self.velocidad, self.y):
                self.x += self.velocidad
            elif self.pacman.x < self.x and not self.bloque.colision(self.x - self.velocidad, self.y):
                self.x -= self.velocidad
        else:
            if self.pacman.y > self.y and not self.bloque.colision(self.x, self.y + self.velocidad):
                self.y += self.velocidad
            elif self.pacman.y < self.y and not self.bloque.colision(self.x, self.y - self.velocidad):
                self.y -= self.velocidad


class FantasmaNaranja(Fantasma):
    def __init__(self, x, y, pacman, bloque):
        super().__init__(x, y, FANTASMA_NARANJA)
        self.pacman = pacman
        self.bloque = bloque

    def mover(self):
        if random.random() < 0.3:
            if self.pacman.x > self.x and not self.bloque.colision(self.x - self.velocidad, self.y):
                self.x -= self.velocidad
            elif self.pacman.x < self.x and not self.bloque.colision(self.x + self.velocidad, self.y):
                self.x += self.velocidad

            if self.pacman.y > self.y and not self.bloque.colision(self.x, self.y - self.velocidad):
                self.y -= self.velocidad
            elif self.pacman.y < self.y and not self.bloque.colision(self.x, self.y + self.velocidad):
                self.y += self.velocidad
        else:
            if self.pacman.x > self.x and not self.bloque.colision(self.x + self.velocidad, self.y):
                self.x += self.velocidad
            elif self.pacman.x < self.x and not self.bloque.colision(self.x - self.velocidad, self.y):
                self.x -= self.velocidad

            if self.pacman.y > self.y and not self.bloque.colision(self.x, self.y + self.velocidad):
                self.y += self.velocidad
            elif self.pacman.y < self.y and not self.bloque.colision(self.x, self.y - self.velocidad):
                self.y -= self.velocidad
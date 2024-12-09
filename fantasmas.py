import pyxel
from constantes import *
from collections import deque
import time


class Fantasma:
    def __init__(self, x, y, sprites, pacman, bloque):
        self.x = x
        self.y = y
        self.velocidad = 1.5
        self.x_inicial = x
        self.y_inicial = y
        self.sprites = sprites
        self.pacman = pacman
        self.bloque = bloque
        self.direccion_actual = "DERECHA"
        self.asustado = False
        self.tiempo_asustado = 0
        self.en_trampa = False
        self.tiempo_trampa = 0  # Tiempo que el fantasma lleva en la trampa
        self.ultimo_movimiento = time.time()  # Temporizador para controlar la velocidad de movimiento

    def activar_asustado(self):
        self.asustado = True
        self.velocidad = 1
        self.tiempo_asustado = time.time()

    def volver_a_trampa(self):
        self.en_trampa = True
        self.tiempo_trampa = time.time()
        if isinstance(self, FantasmaRojo):
            self.x, self.y = 158, 208
        elif isinstance(self, FantasmaRosa):
            self.x, self.y = 181, 208
        elif isinstance(self, FantasmaAzul):
            self.x, self.y = 203, 208
        elif isinstance(self, FantasmaNaranja):
            self.x, self.y = 226, 208
        self.asustado = False
        self.velocidad = 1.5

    def salir_de_trampa(self):
        if self.en_trampa and time.time() - self.tiempo_trampa >= 3:
            self.en_trampa = False

    def mover(self, pacman, bloque):
        if time.time() - self.ultimo_movimiento >= 0.2:  # Limitar movimiento a cada 0.2 segundos
            self.ultimo_movimiento = time.time()
            # Implementar la lógica de movimiento de cada fantasma en subclases
            pass

    def draw(self):
        if self.asustado:
            sprite = FANTASMAS_ASUSTADOS["AZUL"]["Coordenadas"] if pyxel.frame_count // REFRESH % 2 == 0 else FANTASMAS_ASUSTADOS["BLANCO"]["Coordenadas"]
        else:
            sprite = self.sprites[self.direccion_actual]
        pyxel.blt(self.x, self.y, 0, sprite[0], sprite[1], 16, 16, colkey=0)


class FantasmaRojo(Fantasma):
    def mover(self):
        if not self.en_trampa:
            inicio = (self.x // 16 * 16, self.y // 16 * 16)
            objetivo = (self.pacman.x // 16 * 16, self.pacman.y // 16 * 16)
            ruta = self.buscar_ruta_simple(inicio, objetivo)
            if ruta and len(ruta) > 1:
                siguiente_celda = ruta[1]
                dx, dy = siguiente_celda[0] - self.x, siguiente_celda[1] - self.y
                if dx > 0:
                    self.x += min(self.velocidad, dx)
                    self.direccion_actual = "DERECHA"
                elif dx < 0:
                    self.x += max(-self.velocidad, dx)
                    self.direccion_actual = "IZQUIERDA"
                elif dy > 0:
                    self.y += min(self.velocidad, dy)
                    self.direccion_actual = "ABAJO"
                elif dy < 0:
                    self.y += max(-self.velocidad, dy)
                    self.direccion_actual = "ARRIBA"

    def buscar_ruta_simple(self, inicio, objetivo):
        cola = deque([inicio])
        visitados = {inicio: None}
        while cola:
            actual = cola.popleft()
            if actual == objetivo:
                ruta = []
                while actual:
                    ruta.append(actual)
                    actual = visitados[actual]
                ruta.reverse()
                return ruta
            for dx, dy in [(-16, 0), (16, 0), (0, -16), (0, 16)]:
                vecino = (actual[0] + dx, actual[1] + dy)
                if vecino not in visitados and not self.bloque.colision(vecino[0], vecino[1]):
                    visitados[vecino] = actual
                    cola.append(vecino)
        return None
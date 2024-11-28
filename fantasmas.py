import pyxel
import random
from constantes import FANTASMA_ROJO, FANTASMA_ROSA, FANTASMA_AZUL, FANTASMA_NARANJA

class Fantasma:
    def __init__(self, x, y, sprites, muro):
        self.x = x
        self.y = y
        self.sprites = sprites
        self.muro = muro
        self.direccion_actual = "DERECHA"
        self.en_trampa = True  # Inicia dentro de la trampa

    def mover(self, pacman_x, pacman_y):
        if self.en_trampa:
            # Movimiento dentro de la trampa
            direcciones = [(0, -1), (-1, 0), (1, 0), (0, 1)]  # Arriba, izquierda, derecha, abajo
            random.shuffle(direcciones)
            for dx, dy in direcciones:
                nueva_x = self.x + dx * 16
                nueva_y = self.y + dy * 16
                # Si no hay colisión y es la puerta, salir
                if not self.muro.colision(nueva_x, nueva_y):
                    self.x = nueva_x
                    self.y = nueva_y
                    if self.muro.es_puerta_salida(nueva_x, nueva_y):
                        self.en_trampa = False  # Fantasma ha salido
                    return
        else:
            # Movimiento fuera de la trampa
            if isinstance(self, FantasmaRojo):
                self.perseguir_pacman(pacman_x, pacman_y)
            elif isinstance(self, FantasmaRosa):
                self.emboscar_pacman(pacman_x, pacman_y)
            elif isinstance(self, FantasmaAzul):
                self.mover_erratico()
            elif isinstance(self, FantasmaNaranja):
                self.mover_aleatorio()

    def draw(self):
        sprite_x, sprite_y = self.sprites[self.direccion_actual]
        pyxel.blt(self.x, self.y, 0, sprite_x, sprite_y, 16, 16, colkey=0)

    def perseguir_pacman(self, pacman_x, pacman_y):
        if self.x < pacman_x:
            self.x += 1
        elif self.x > pacman_x:
            self.x -= 1
        if self.y < pacman_y:
            self.y += 1
        elif self.y > pacman_y:
            self.y -= 1

    def emboscar_pacman(self, pacman_x, pacman_y):
        if pacman_x % 2 == 0:
            self.perseguir_pacman(pacman_x + 16, pacman_y)
        else:
            self.perseguir_pacman(pacman_x, pacman_y + 16)

    def mover_erratico(self):
        direcciones = [(0, -1), (-1, 0), (1, 0), (0, 1)]
        random.shuffle(direcciones)
        dx, dy = direcciones[0]
        self.x += dx * 16
        self.y += dy * 16

    def mover_aleatorio(self):
        direcciones = [(0, -1), (-1, 0), (1, 0), (0, 1)]
        dx, dy = random.choice(direcciones)
        self.x += dx * 16
        self.y += dy * 16

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
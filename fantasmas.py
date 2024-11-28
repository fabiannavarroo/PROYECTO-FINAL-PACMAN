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
        self.velocidad = 1.5
        self.en_trampa = True  # Comienza dentro de la trampa
        self.ha_salido = False  # Indica si el fantasma ya salió y no puede volver a entrar

    def mover(self, pacman_x, pacman_y):
        if self.en_trampa:
            # Movimiento dentro de la trampa
            direcciones = [(0, -1), (-1, 0), (1, 0), (0, 1)]  # Arriba, izquierda, derecha, abajo
            random.shuffle(direcciones)
            for dx, dy in direcciones:
                nueva_x = self.x + dx * self.velocidad
                nueva_y = self.y + dy * self.velocidad
                # Si no hay colisión y es la puerta de salida, salir
                if not self.muro.colision(nueva_x, nueva_y):
                    self.x = nueva_x
                    self.y = nueva_y
                    if self.muro.es_puerta_salida(nueva_x, nueva_y):  # Verificar si es la puerta de salida
                        self.en_trampa = False
                        self.ha_salido = True  # Marca como que ya salió
                    return
        else:
            # Movimiento fuera de la trampa
            if not self.ha_salido and self.muro.es_trampa(self.x, self.y):
                self.en_trampa = True  # Reingresar a la trampa si es permitido
                return

            # Comportamiento según el tipo de fantasma
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
        # Perseguir directamente a PacMan
        if self.x < pacman_x and not self.muro.colision(self.x + 16, self.y):
            self.x += 1
            self.direccion_actual = "DERECHA"
        elif self.x > pacman_x and not self.muro.colision(self.x - 16, self.y):
            self.x -= 1
            self.direccion_actual = "IZQUIERDA"
        elif self.y < pacman_y and not self.muro.colision(self.x, self.y + 16):
            self.y += 1
            self.direccion_actual = "ABAJO"
        elif self.y > pacman_y and not self.muro.colision(self.x, self.y - 16):
            self.y -= 1
            self.direccion_actual = "ARRIBA"

    def emboscar_pacman(self, pacman_x, pacman_y):
        # Intentar adelantarse al movimiento de PacMan
        objetivo_x = pacman_x + 16 if pacman_x + 16 < len(self.muro.mapa[0]) * self.muro.celda_tamaño else pacman_x
        objetivo_y = pacman_y + 16 if pacman_y + 16 < len(self.muro.mapa) * self.muro.celda_tamaño else pacman_y
        self.perseguir_pacman(objetivo_x, objetivo_y)

    def mover_erratico(self):
        # Movimiento errático
        direcciones = ["ARRIBA", "ABAJO", "IZQUIERDA", "DERECHA"]
        random.shuffle(direcciones)
        for direccion in direcciones:
            dx, dy = {
                "ARRIBA": (0, -1),
                "ABAJO": (0, 1),
                "IZQUIERDA": (-1, 0),
                "DERECHA": (1, 0),
            }[direccion]
            nueva_x = self.x + dx * self.velocidad
            nueva_y = self.y + dy * self.velocidad
            if not self.muro.colision(nueva_x, nueva_y):
                self.x = nueva_x
                self.y = nueva_y
                self.direccion_actual = direccion
                return

    def mover_aleatorio(self):
        # Movimiento aleatorio
        direcciones = ["ARRIBA", "ABAJO", "IZQUIERDA", "DERECHA"]
        direccion = random.choice(direcciones)
        dx, dy = {
            "ARRIBA": (0, -1),
            "ABAJO": (0, 1),
            "IZQUIERDA": (-1, 0),
            "DERECHA": (1, 0),
        }[direccion]
        nueva_x = self.x + dx * self.velocidad
        nueva_y = self.y + dy * self.velocidad
        if not self.muro.colision(nueva_x, nueva_y):
            self.x = nueva_x
            self.y = nueva_y
            self.direccion_actual = direccion


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
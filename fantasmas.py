import pyxel
from constantes import FANTASMA_ROJO, FANTASMA_ROSA, FANTASMA_AZUL, FANTASMA_NARANJA,PORTALES
import random

class Fantasma:
    def __init__(self, x, y, sprites, muro):
        self.x = x
        self.y = y
        self.sprites = sprites
        self.muro = muro
        self.velocidad = 1
        self.direccion_actual = self.sprites["DERECHA"]
        self.en_trampa = True  # Indica si el fantasma está dentro de la trampa

    def mover(self):
        # Diccionario de posibles direcciones
        DIRECCIONES = {
            "ARRIBA": (0, -self.velocidad),
            "ABAJO": (0, self.velocidad),
            "IZQUIERDA": (-self.velocidad, 0),
            "DERECHA": (self.velocidad, 0),
        }

        # Verificar si el fantasma está en la trampa
        fila = self.y // self.muro.celda_tamaño
        columna = self.x // self.muro.celda_tamaño
        valor_celda = self.muro.mapa[fila][columna]

        if self.en_trampa:
            # Si está en la trampa y en la salida (16), sale de la trampa
            if valor_celda == 16:
                self.en_trampa = False
            else:
                # Movimiento aleatorio dentro de la trampa
                direcciones_validas = []
                for direccion, (dx, dy) in DIRECCIONES.items():
                    nueva_x = self.x + dx
                    nueva_y = self.y + dy
                    fila_nueva = nueva_y // self.muro.celda_tamaño
                    columna_nueva = nueva_x // self.muro.celda_tamaño
                    if (
                        0 <= fila_nueva < len(self.muro.mapa)
                        and 0 <= columna_nueva < len(self.muro.mapa[0])
                        and self.muro.mapa[fila_nueva][columna_nueva] in [15, 19, 16, 17]
                    ):
                        direcciones_validas.append(direccion)

                # Elegir una dirección válida aleatoria
                if direcciones_validas:
                    self.direccion_actual = random.choice(direcciones_validas)

        else:
            # Movimiento aleatorio fuera de la trampa
            direcciones_validas = []
            for direccion, (dx, dy) in DIRECCIONES.items():
                nueva_x = self.x + dx
                nueva_y = self.y + dy
                if not self.muro.colision(nueva_x, nueva_y):
                    direcciones_validas.append(direccion)

            # Elegir una dirección válida aleatoria
            if direcciones_validas:
                self.direccion_actual = random.choice(direcciones_validas)

        #Portal
        if (self.x,self.y)in PORTALES:
            self.x,self.y = PORTALES[(self.x,self.y)]

        # Actualizar la posición del fantasma
        dx, dy = DIRECCIONES[self.direccion_actual]
        self.x += dx
        self.y += dy
            
                
    # Dibujar el sprite del fantasma en la dirección correspondiente.
    def draw(self):
        sprite_x, sprite_y = self.sprites[self.direccion_actual]
        pyxel.blt(self.x, self.y, 0, sprite_x, sprite_y, 16, 16, colkey=0)

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
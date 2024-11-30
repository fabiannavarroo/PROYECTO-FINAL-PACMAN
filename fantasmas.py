import pyxel
from constantes import FANTASMA_ROJO, FANTASMA_ROSA, FANTASMA_AZUL, FANTASMA_NARANJA, PORTALES, FANTASMAS_ASUSTADOS
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
        self.modo_asustado = False  # Los fantasmas no estas asustado al empezar


    #def salir_trampa(self):
    

    def cambiar_direccion(self):
        # Direcciones que puede tener los fantasmas
        DIRECCIONES = ["ARRIBA", "ABAJO", "DERECHA", "IZQUIERDA"]
        nueva_direccion = random.choice(DIRECCIONES) # De forma aleatoria se escoge una direccion
        self.direccion_actual = nueva_direccion # Se le asigna esa direccion a la actual del fantasmas
    
    def activar_modo_asustado(self):
        self.modo_asustado = True
        for fantasma in self.lista_fantasmas:
            fantasma.cambiar_color(FANTASMAS_ASUSTADOS)  # Cambiar al color de "asustado"


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
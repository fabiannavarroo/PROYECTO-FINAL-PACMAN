import pyxel
from bloque import Bloque
from constantes import *

class Muro:
    def __init__(self):
        self.bloques = []
        for elemento in MAPA_1:
            x, y, tipo = elemento
            sprite = globals()[f"SPRITE_BLOQUE_{tipo[-1]}"]
            self.bloques.append(Bloque(x, y, sprite))

    def colision(self, x, y):
        for bloque in self.bloques:
            if (x >= bloque.x and x < bloque.x + 16 and 
                y >= bloque.y and y < bloque.y + 16):
                return True
        return False

    def draw(self):
        for bloque in self.bloques:
            pyxel.blt(bloque.x, bloque.y, *bloque.sprite)

    def fin(self):
        sprite = TEXTO["GAME OVER"]
        sprite_x, sprite_y = sprite["Coordenadas"]
        sprite_w, sprite_h = sprite["Tamaño"]
        pos_x = 192
        pos_y= 190
        pyxel.blt(pos_x, pos_y, 0, sprite_x, sprite_y, sprite_w, sprite_h, colkey=0)

    
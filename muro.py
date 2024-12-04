import pyxel
from bloque import Bloque
from constantes import *

class Muro:
    def __init__(self):
        self.bloque = []
        for x, y, tipo in MAPA_1:
            self.bloque.append(Bloque(x, y, tipo))

    def colision(self, x, y):
        for b in self.bloque:
            bloque_x = b.x
            bloque_y = b.y
            if (x >= bloque_x and x < bloque_x + 16 and 
                y >= bloque_y and y < bloque_y + 16):
                return True
        return False

    def draw(self):
        for b in self.bloque:
            pyxel.blt(b.x, b.y, *b.sprite)

    def fin(self):
        sprite = TEXTO["GAME OVER"]
        sprite_x, sprite_y = sprite["Coordenadas"]
        sprite_w, sprite_h = sprite["Tamaño"]
        pos_x = 192
        pos_y = 190
        pyxel.blt(pos_x, pos_y, 0, sprite_x, sprite_y, sprite_w, sprite_h, colkey=0)

    
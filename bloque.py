

from constantes import *
class Bloque:

    def __init__(self, x: int, y: int, tipo: int):

        self.x = x
        self.y = y
        self.tipo = tipo

        if self.tipo == 1:
            self.sprite = SPRITE_BLOQUE_1
        elif self.tipo == 2:
            self.sprite = SPRITE_BLOQUE_2
        elif self.tipo == 3:
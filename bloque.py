from constantes import *

class Bloque:
    def __init__(self, x: int, y: int, tipo: int):
        """
        Constructor de la clase Bloque.
        :param x: Coordenada X del bloque.
        :param y: Coordenada Y del bloque.
        :param tipo: Tipo del bloque (1 a 23).
        """
        self.x = x
        self.y = y
        self.tipo = tipo

        # Asignar el sprite basado en el tipo de bloque
        if self.tipo == 1:
            self.sprite = SPRITE_BLOQUE_1
        elif self.tipo == 2:
            self.sprite = SPRITE_BLOQUE_2
        elif self.tipo == 3:
            self.sprite = SPRITE_BLOQUE_3
        elif self.tipo == 4:
            self.sprite = SPRITE_BLOQUE_4
        elif self.tipo == 5:
            self.sprite = SPRITE_BLOQUE_5
        elif self.tipo == 6:
            self.sprite = SPRITE_BLOQUE_6
        elif self.tipo == 7:
            self.sprite = SPRITE_BLOQUE_7
        elif self.tipo == 8:
            self.sprite = SPRITE_BLOQUE_8
        elif self.tipo == 9:
            self.sprite = SPRITE_BLOQUE_9
        elif self.tipo == 10:
            self.sprite = SPRITE_BLOQUE_10
        elif self.tipo == 11:
            self.sprite = SPRITE_BLOQUE_11
        elif self.tipo == 12:
            self.sprite = SPRITE_BLOQUE_12
        elif self.tipo == 13:
            self.sprite = SPRITE_BLOQUE_13
        elif self.tipo == 14:
            self.sprite = SPRITE_BLOQUE_14
        elif self.tipo == 15:
            self.sprite = SPRITE_BLOQUE_15
        elif self.tipo == 16:
            self.sprite = SPRITE_BLOQUE_16
        elif self.tipo == 17:
            self.sprite = SPRITE_BLOQUE_17
        elif self.tipo == 18:
            self.sprite = SPRITE_BLOQUE_18
        elif self.tipo == 19:
            self.sprite = SPRITE_BLOQUE_19
        elif self.tipo == 20:
            self.sprite = SPRITE_BLOQUE_20
        elif self.tipo == 21:
            self.sprite = SPRITE_BLOQUE_21
        elif self.tipo == 22:
            self.sprite = SPRITE_BLOQUE_22
        elif self.tipo == 23:
            self.sprite = SPRITE_BLOQUE_23
        else:
            raise ValueError("Tipo de bloque", str(self.tipo), "no válido. Debe estar entre 1 y 23.")
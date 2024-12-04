from constantes import *
import pyxel   

class Bloque:
    def __init__(self, x, y, tipo):
        self.x = x
        self.y = y
        self.tipo = tipo

        # Asignar el sprite basado en el tipo de bloque
        if tipo == 1:
            self.sprite = SPRITE_BLOQUE_1
        elif tipo == 2:
            self.sprite = SPRITE_BLOQUE_2
        elif tipo == 3:
            self.sprite = SPRITE_BLOQUE_3
        elif tipo == 4:
            self.sprite = SPRITE_BLOQUE_4
        elif tipo == 5:
            self.sprite = SPRITE_BLOQUE_5
        elif tipo == 6:
            self.sprite = SPRITE_BLOQUE_6
        elif tipo == 7:
            self.sprite = SPRITE_BLOQUE_7
        elif tipo == 8:
            self.sprite = SPRITE_BLOQUE_8
        elif tipo == 9:
            self.sprite = SPRITE_BLOQUE_9
        elif tipo == 10:
            self.sprite = SPRITE_BLOQUE_10
        elif tipo == 11:
            self.sprite = SPRITE_BLOQUE_11
        elif tipo == 12:
            self.sprite = SPRITE_BLOQUE_12
        elif tipo == 13:
            self.sprite = SPRITE_BLOQUE_13
        elif tipo == 14:
            self.sprite = SPRITE_BLOQUE_14
        elif tipo == 15:
            self.sprite = SPRITE_BLOQUE_15
        elif tipo == 16:
            self.sprite = SPRITE_BLOQUE_16
        elif tipo == 17:
            self.sprite = SPRITE_BLOQUE_17
        elif tipo == 18:
            self.sprite = SPRITE_BLOQUE_18
        elif tipo == 19:
            self.sprite = SPRITE_BLOQUE_19
        elif tipo == 20:
            self.sprite = SPRITE_BLOQUE_20
        elif tipo == 21:
            self.sprite = SPRITE_BLOQUE_21
        elif tipo == 22:
            self.sprite = SPRITE_BLOQUE_22
        elif tipo == 23:
            self.sprite = SPRITE_BLOQUE_23
        else:
            raise ValueError("Tipo de bloque no válido. Debe estar entre 1 y 23.")

    def colision(self, x, y):
        # Comprueba si hay colisión con las coordenadas (x, y).
        sprite_w = self.sprite[3]
        sprite_h = self.sprite[4]

        if self.x <= x < self.x + sprite_w and self.y <= y < self.y + sprite_h:
            return True
        return False

    def draw(self):
        # Dibuja este bloque en la pantalla.
        sprite_x = self.sprite[0]
        sprite_y = self.sprite[1]
        sprite_bank = self.sprite[2]
        sprite_w = self.sprite[3]
        sprite_h = self.sprite[4]

        # Dibujar el sprite del bloque
        pyxel.blt(self.x, self.y, sprite_bank, sprite_x, sprite_y, sprite_w, sprite_h, colkey=0)

    def inicializar_mapa(mapa_data):
        # Crea instancias de Bloque para un mapa.
        bloques = []
        for data in mapa_data:
            bloque = Bloque(data[0], data[1], data[2])
            bloques.append(bloque)
        return bloques

    def dibujar_bloques(bloques):
        # Dibuja todos los bloques del mapa.
        for bloque in bloques:
            bloque.draw()

    def detectar_colision(bloques, x, y):
        # Detecta si hay colisión en las coordenadas (x, y).
        for bloque in bloques:
            if bloque.colision(x, y):
                return True
        return False
from constantes import *
import pyxel

class Bloque:
    def __init__(self):
        # Lista de bloques inicializada desde MAPA_1
        self.bloques = []
        self.celda_tamaño = 16

        # Crear bloques a partir de MAPA_1
        for x, y, tipo in MAPA_1:
            sprite = self.obtener_sprite(tipo)  # Obtener el sprite correspondiente
            self.bloques.append((x, y, sprite))  # Almacenar solo coordenadas y sprite

    def obtener_sprite(self, tipo):
        # Devuelve el sprite correspondiente al tipo
        if tipo == 1:
            return SPRITE_BLOQUE_1
        elif tipo == 2:
            return SPRITE_BLOQUE_2
        elif tipo == 3:
            return SPRITE_BLOQUE_3
        elif tipo == 4:
            return SPRITE_BLOQUE_4
        elif tipo == 5:
            return SPRITE_BLOQUE_5
        elif tipo == 6:
            return SPRITE_BLOQUE_6
        elif tipo == 7:
            return SPRITE_BLOQUE_7
        elif tipo == 8:
            return SPRITE_BLOQUE_8
        elif tipo == 9:
            return SPRITE_BLOQUE_9
        elif tipo == 10:
            return SPRITE_BLOQUE_10
        elif tipo == 11:
            return SPRITE_BLOQUE_11
        elif tipo == 12:
            return SPRITE_BLOQUE_12
        elif tipo == 13:
            return SPRITE_BLOQUE_13
        elif tipo == 14:
            return SPRITE_BLOQUE_14
        elif tipo == 15:
            return SPRITE_BLOQUE_15
        elif tipo == 16:
            return SPRITE_BLOQUE_16
        elif tipo == 17:
            return SPRITE_BLOQUE_17
        elif tipo == 18:
            return SPRITE_BLOQUE_18
        elif tipo == 19:
            return SPRITE_BLOQUE_19
        elif tipo == 20:
            return SPRITE_BLOQUE_20
        elif tipo == 21:
            return SPRITE_BLOQUE_21
        elif tipo == 22:
            return SPRITE_BLOQUE_22
        elif tipo == 23:
            return SPRITE_BLOQUE_23
        else:
            raise ValueError("Tipo de bloque no válido. Debe estar entre 1 y 23.")

    def colision(self, x, y):
        # Comprueba si hay colisión con las coordenadas (x, y)
        sprite_tamaño = 16

        # Puntos de las esquinas del sprite
        puntos_a_verificar = [
            (x, y),  # Esquina superior izquierda
            (x + sprite_tamaño - 1, y),  # Esquina superior derecha
            (x, y + sprite_tamaño - 1),  # Esquina inferior izquierda
            (x + sprite_tamaño - 1, y + sprite_tamaño - 1)  # Esquina inferior derecha
        ]

        # Verificar colisión para cada punto con los bloques
        for px, py in puntos_a_verificar:
            for bloque in self.bloques:
                bloque_x = bloque["x"]
                bloque_y = bloque["y"]
                sprite = bloque["sprite"]
                sprite_w = sprite[3]
                sprite_h = sprite[4]

                if bloque_x <= px < bloque_x + sprite_w and bloque_y <= py < bloque_y + sprite_h:
                    return True  # Colisión detectada
        return False  # No hay colisión

    def draw(self):
        # Dibuja todos los bloques
        for bloque in self.bloques:
            bloque_x = bloque["x"]
            bloque_y = bloque["y"]
            sprite = bloque["sprite"]
            sprite_x = sprite[0]
            sprite_y = sprite[1]
            sprite_bank = sprite[2]
            sprite_w = sprite[3]
            sprite_h = sprite[4]

            # Dibujar el sprite del bloque
            pyxel.blt(bloque_x, bloque_y, sprite_bank, sprite_x, sprite_y, sprite_w, sprite_h, colkey=0)
import pyxel
from constantes import *


class Bloque:
    def __init__(self):
        self.nivel = 1  # Nivel inicial
        self.celda_tamaño = 16
        self.bloques = []
        self.mapas = MAPA
        self.cargar_mapa()  # Cargar el mapa del nivel inicial 


    def cargar_mapa(self):
        # Cargar los bloques del nivel actual
        self.bloques = []
        for x, y, tipo in self.mapas[self.nivel]:
            sprite = self.obtener_sprite(tipo)  # Obtener el sprite 
            self.bloques.append((x, y, sprite))  # Guardar solo coordenadas y sprite


    def obtener_sprite(self, tipo):
        # Devuelve el sprite correspondiente al tipo
        if self.nivel == 1:
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
        elif self.nivel == 2:
            if tipo == 1:
                return SPRITE_BLOQUE_1_1
            elif tipo == 2:
                return SPRITE_BLOQUE_2_1
            elif tipo == 3:
                return SPRITE_BLOQUE_3_1
            elif tipo == 4:
                return SPRITE_BLOQUE_4_1
            elif tipo == 5:
                return SPRITE_BLOQUE_5_1
            elif tipo == 6:
                return SPRITE_BLOQUE_6_1
            elif tipo == 7:
                return SPRITE_BLOQUE_7_1
            elif tipo == 8:
                return SPRITE_BLOQUE_8_1
            elif tipo == 9:
                return SPRITE_BLOQUE_9_1
            elif tipo == 10:
                return SPRITE_BLOQUE_10_1
            elif tipo == 11:
                return SPRITE_BLOQUE_11_1
            elif tipo == 12:
                return SPRITE_BLOQUE_12_1
            elif tipo == 13:
                return SPRITE_BLOQUE_13_1
            elif tipo == 14:
                return SPRITE_BLOQUE_14_1
            elif tipo == 15:
                return SPRITE_BLOQUE_15_1
            elif tipo == 16:
                return SPRITE_BLOQUE_16_1
            elif tipo == 17:
                return SPRITE_BLOQUE_17_1
            elif tipo == 18:
                return SPRITE_BLOQUE_18_1
            elif tipo == 19:
                return SPRITE_BLOQUE_19_1
            elif tipo == 20:
                return SPRITE_BLOQUE_20_1
            elif tipo == 21:
                return SPRITE_BLOQUE_21_1
            elif tipo == 22:
                return SPRITE_BLOQUE_22_1
            elif tipo == 23:
                return SPRITE_BLOQUE_23_1
            else:
                raise ValueError("Tipo de bloque no válido. Debe estar entre 1 y 23.")
        else:
            if tipo == 1:
                return SPRITE_BLOQUE_1_2
            elif tipo == 2:
                return SPRITE_BLOQUE_2_2
            elif tipo == 3:
                return SPRITE_BLOQUE_3_2
            elif tipo == 4:
                return SPRITE_BLOQUE_4_2
            elif tipo == 5:
                return SPRITE_BLOQUE_5_2
            elif tipo == 6:
                return SPRITE_BLOQUE_6_2
            elif tipo == 7:
                return SPRITE_BLOQUE_7_2
            elif tipo == 8:
                return SPRITE_BLOQUE_8_2
            elif tipo == 9:
                return SPRITE_BLOQUE_9_2
            elif tipo == 10:
                return SPRITE_BLOQUE_10_2
            elif tipo == 11:
                return SPRITE_BLOQUE_11_2
            elif tipo == 12:
                return SPRITE_BLOQUE_12_2
            elif tipo == 13:
                return SPRITE_BLOQUE_13_2
            elif tipo == 14:
                return SPRITE_BLOQUE_14_2
            elif tipo == 15:
                return SPRITE_BLOQUE_15_2
            elif tipo == 16:
                return SPRITE_BLOQUE_16_2
            elif tipo == 17:
                return SPRITE_BLOQUE_17_2
            elif tipo == 18:
                return SPRITE_BLOQUE_18_2
            elif tipo == 19:
                return SPRITE_BLOQUE_19_2
            elif tipo == 20:
                return SPRITE_BLOQUE_20_2
            elif tipo == 21:
                return SPRITE_BLOQUE_21_2
            elif tipo == 22:
                return SPRITE_BLOQUE_22_2
            elif tipo == 23:
                return SPRITE_BLOQUE_23_2
            elif tipo == 24:
                return SPRITE_BLOQUE_24_2
            else:
                raise ValueError("Tipo de bloque no válido. Debe estar entre 1 y 23.")


    def colision(self, x, y):
        # Verifica si un punto (x, y) colisiona con un bloque del mapa.
        sprite_tamaño = self.celda_tamaño
        
        # Verificar los cuatro puntos clave del sprite
        puntos_a_verificar = [
            (x, y),  # Esquina superior izquierda
            (x + sprite_tamaño - 1, y),  # Esquina superior derecha
            (x, y + sprite_tamaño - 1),  # Esquina inferior izquierda
            (x + sprite_tamaño - 1, y + sprite_tamaño - 1)  # Esquina inferior derecha
        ]
        
        # Revisar si alguno de los puntos está dentro de un bloque
        for px, py in puntos_a_verificar:
            celda_x = px // sprite_tamaño
            celda_y = py // sprite_tamaño
            if (celda_x, celda_y) in self.bloques:  # `self.bloques` debería contener las celdas bloqueadas
                return True  # Hay colisión
        return False  # No hay colisión


    def draw(self):
        # Dibuja todos los bloques
        for bloque in self.bloques:
            bloque_x = bloque[0]  # Coordenada x del bloque
            bloque_y = bloque[1]  # Coordenada y del bloque
            sprite = bloque[2]  # Sprite del bloque
            sprite_x = sprite[0]
            sprite_y = sprite[1]
            sprite_bank = sprite[2]
            sprite_w = sprite[3]
            sprite_h = sprite[4]

            # Dibujar el sprite del bloque
            pyxel.blt(bloque_x, bloque_y, sprite_bank, sprite_x, sprite_y, sprite_w, sprite_h, colkey=0)



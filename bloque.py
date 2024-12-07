import pyxel
from constantes import *
from puntos import Puntos

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

    def subir_nivel(self):
        # Aumentar el nivel y cargar el nuevo mapa
        if self.nivel + 1 in self.mapas:
            self.nivel += 1
            self.cargar_mapa()
        else:
            print("No hay más niveles disponibles.")  # Mensaje opcional si no hay más niveles

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
        # Comprueba si hay un muro en la posición (x, y)
        sprite_tamaño = 16  # Tamaño del sprite
        puntos_a_verificar = [
            (x, y),  # Esquina superior izquierda
            (x + sprite_tamaño - 1, y),  # Esquina superior derecha
            (x, y + sprite_tamaño - 1),  # Esquina inferior izquierda
            (x + sprite_tamaño - 1, y + sprite_tamaño - 1),  # Esquina inferior derecha
        ]

        # Verificar cada punto contra los bloques
        colision_detectada = False
        for px, py in puntos_a_verificar:
            for bloque_x, bloque_y, _ in self.bloques:
                if bloque_x <= px < bloque_x + self.celda_tamaño and bloque_y <= py < bloque_y + self.celda_tamaño:
                    colision_detectada = True
            if colision_detectada:
                return True  # Colisión detectada

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

    def dibujar_letras_mapa(self, x, y, sprite):
        # Dibuja las letras en el mapa
        sprite = TEXTO[sprite]
        pyxel.blt(x, y, 0, sprite["Coordenadas"][0], sprite["Coordenadas"][1], sprite["Tamaño"][0], sprite["Tamaño"][1], colkey=0)
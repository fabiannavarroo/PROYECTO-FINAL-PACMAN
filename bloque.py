from constantes import *

class Bloque:
    def __init__(self, x: int, y: int, tipo: int):
        self.x = x
        self.y = y
        self.tipo = tipo
        self.sprite = self.obtener_sprite()

    def obtener_sprite(self):
        # Diccionario que mapea tipos de bloque a sus sprites
        sprites = {
            1: SPRITE_BLOQUE_1,   # Esquina izquierda horizontal
            2: SPRITE_BLOQUE_2,   # Borde horizontal
            3: SPRITE_BLOQUE_3,   # Esquina derecha horizontal
            4: SPRITE_BLOQUE_4,   # Esquina superior vertical
            5: SPRITE_BLOQUE_5,   # Borde vertical
            6: SPRITE_BLOQUE_6,   # Esquina inferior vertical
            7: SPRITE_BLOQUE_7,   # Cruce en T hacia abajo
            8: SPRITE_BLOQUE_8,   # Cruce en T hacia arriba
            9: SPRITE_BLOQUE_9,   # Cruce en T hacia derecha
            10: SPRITE_BLOQUE_10, # Cruce en T hacia izquierda
            11: SPRITE_BLOQUE_11, # Borde esquina superior izquierda
            12: SPRITE_BLOQUE_12, # Borde esquina superior derecha
            13: SPRITE_BLOQUE_13, # Borde esquina inferior izquierda
            14: SPRITE_BLOQUE_14, # Borde esquina inferior derecha
            15: SPRITE_BLOQUE_15, # Esquina izquierda superior trampa fantasmas
            16: SPRITE_BLOQUE_16, # Puerta salida de fantasmas
            17: SPRITE_BLOQUE_17, # Esquina derecha superior trampa fantasmas
            18: SPRITE_BLOQUE_18, # Esquina izquierda inferior trampa fantasmas
            19: SPRITE_BLOQUE_19, # Borde superior trampa fantasma
            20: SPRITE_BLOQUE_20, # Esquina derecha inferior trampa fantasmas
            21: SPRITE_BLOQUE_21, # Borde derecha trampa fantasmas
            22: SPRITE_BLOQUE_22, # Borde izquierda trampa fantasmas
            23: SPRITE_BLOQUE_23  # Borde inferior trampa fantasma
        }
        
        if self.tipo in sprites:
            return sprites[self.tipo]
        else:
            raise ValueError(f"Tipo de bloque {self.tipo} no válido. Debe estar entre 1 y 23.")
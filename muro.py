import pyxel

class Muro:
    def __init__(self):
        # Matriz que representa el mapa
        # Cada número en la matriz corresponde a un tipo de muro
        self.mapa = [
            [3, 2, 2, 2, 4],
            [1, 0, 0, 0, 1],
            [1, 0, 3, 4, 1],
            [1, 0, 0, 0, 1],
            [5, 2, 2, 2, 6],
        ]

        # Diccionario para mapear tipos de muros a sprites y tamaños
        self.sprites = {
            1: {"ubicacion": (48, 8), "tamaño": (16, 16)},  # Muro vertical, alto
            2: {"ubicacion": (16, 0), "tamaño": (32, 16)},  # Muro horizontal, ancho
            3: {"ubicacion": (32, 0), "tamaño": (16, 16)},  # Esquina superior izquierda
            4: {"ubicacion": (48, 0), "tamaño": (16, 16)},  # Esquina superior derecha
            5: {"ubicacion": (32, 16), "tamaño": (16, 16)}, # Esquina inferior izquierda
            6: {"ubicacion": (48, 16), "tamaño": (16, 16)},
            7: {"ubicacion": (48, 8), "tamaño": (16, 16)},  # Muro vertical, alto
            8: {"ubicacion": (16, 0), "tamaño": (32, 16)},  # Muro horizontal, ancho
            9: {"ubicacion": (32, 0), "tamaño": (16, 16)},  # Esquina superior izquierda
            10: {"ubicacion": (48, 0), "tamaño": (16, 16)},  # Esquina superior derecha
            11: {"ubicacion": (32, 16), "tamaño": (16, 16)}, # Esquina inferior izquierda
            12: {"ubicacion": (48, 16), "tamaño": (16, 16)},
            13: {"ubicacion": (48, 8), "tamaño": (16, 16)},  # Muro vertical, alto
            14: {"ubicacion": (16, 0), "tamaño": (32, 16)},  # Muro horizontal, ancho
            15: {"ubicacion": (32, 0), "tamaño": (16, 16)},  # Esquina superior izquierda
            16: {"ubicacion": (48, 0), "tamaño": (16, 16)},  # Esquina superior derecha
            17: {"ubicacion": (32, 16), "tamaño": (16, 16)}, # Esquina inferior izquierda
            18: {"ubicacion": (48, 16), "tamaño": (16, 16)}, # Esquina inferior derecha
        }

    def colision(self, x, y):
        """
        Comprueba si hay un muro en la posición (x, y).
        :param x: Posición x (en píxeles).
        :param y: Posición y (en píxeles).
        :return: True si hay colisión con un muro, False en caso contrario.
        """
        fila = y // 16
        columna = x // 16

        # Comprobar si está dentro de los límites del mapa
        if 0 <= fila < len(self.mapa) and 0 <= columna < len(self.mapa[0]):
            return self.mapa[fila][columna] != 0  # Cualquier número distinto de 0 es un muro
        return False

    def draw(self):
        """
        Dibuja los muros en la pantalla adaptando el tamaño de los sprites.
        """
        for fila in range(len(self.mapa)):
            for columna in range(len(self.mapa[0])):
                tipo_muro = self.mapa[fila][columna]
                if tipo_muro != 0:  # Si no es un espacio vacío
                    sprite = self.sprites[tipo_muro]
                    sprite_x, sprite_y = sprite["ubicacion"]
                    sprite_w, sprite_h = sprite["tamaño"]
                    pyxel.blt(
                        columna * 16, fila * 16,  # Coordenadas donde se dibuja el muro
                        1,  # Banco de imágenes
                        sprite_x, sprite_y,  # Coordenadas del sprite en recursos.pyxres
                        sprite_w, sprite_h,  # Tamaño del sprite
                        colkey=0  # Transparencia
                    )
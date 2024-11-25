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
        

    def colision(self, x, y):
        
        #Comprueba si hay un muro en la posición (x, y).
        
        fila = y // 16
        columna = x // 16


    def draw(self):

        #Dibuja los muros en la pantalla adaptando el tamaño de los sprites.
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
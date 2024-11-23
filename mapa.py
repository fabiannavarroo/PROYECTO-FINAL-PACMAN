import pyxel

class Mapa:
    def __init__(self):
        # Matriz que define el diseño del mapa
        self.mapa = [
            [1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7, 8, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 2],
            [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],
            [6, 0, 11, 14, 14, 12, 0, 11, 14, 14, 14, 12, 0, 16, 15, 0, 11, 14, 14, 14, 12, 0, 11, 14, 14, 12, 0, 6],
            [6, 0, 16, 0, 0, 15, 0, 16, 0, 0, 0, 15, 0, 16, 15, 0, 16, 0, 0, 0, 15, 0, 16, 0, 0, 15, 0, 6],
            [6, 0, 9, 13, 13, 10, 0, 9, 13, 13, 13, 10, 0, 9, 10, 0, 9, 13, 13, 13, 10, 0, 9, 13, 13, 10, 0, 6],
            [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],
            [6, 0, 11, 14, 14, 12, 0, 11, 12, 0, 11, 14, 14, 14, 14, 14, 14, 12, 0, 11, 12, 0, 11, 14, 14, 12, 0, 6],
            [6, 0, 9, 13, 13, 10, 0, 16, 15, 0, 9, 13, 13, 7, 8, 13, 13, 10, 0, 16, 15, 0, 9, 13, 13, 10, 0, 6],
            [6, 0, 0, 0, 0, 0, 0, 16, 15, 0, 0, 0, 0, 16, 15, 0, 0, 0, 0, 16, 15, 0, 0, 0, 0, 0, 0, 6],
            [],[],[]
        ]

    def draw(self):
        # Tamaño de cada sprite en píxeles
        sprite_size = 8

        # Diccionario que mapea valores de la matriz a coordenadas en el archivo de recursos
        sprites = {
            1: (0, 8),  # Esquina superior izquierda
            2: (8, 8),  # Esquina superior derecha
            3: (0, 16),  # Esquina inferior izquierda
            4: (8, 16),  # Esquina inferior derecha
            5: (16,9),  # Borde superior e inferior
            6: (24, 8),  # Borde laterales
            7: (16, 16),  # Bajada izquierda
            8: (24, 16),  # Bajada derecha
            9: (32, 8),  # U izquierda
            10: (40, 8),  # U derecha
            11: (32, 16),  # U abajo izquierda
            12: (40, 16),  # U abajo derecha
            13: (24, 8),  # Barra abajo 
            14: (24, 8),  # Barra arriba 
            15: (24, 8),  # Barra izquierda 
            16: (24, 8),  # Barra derecha 
            17: (0, 24),  # Celda rosa fantasmas 
            18: (16, 24),  # Subida izquierda 
            19: (32, 24),  # Subida derecha 
            20: (0, 32),  # Giro izquierda arriba 
            21: (8, 32),  # Giro derecha arriba  
            22: (0, 40),  # Giro izquierda abajo  
            23: (8, 40),  # Giro derecha abajo  
        }

        # Dibuja cada celda del mapa en la pantalla
        for y, row in enumerate(self.mapa):
            for x, cell in enumerate(row):
                if cell in sprites:
                    sprite_x, sprite_y = sprites[cell]
                    pyxel.blt(x * sprite_size, y * sprite_size, 0, sprite_x, sprite_y, sprite_size, sprite_size)

class App:
    def __init__(self):
        # Inicializa Pyxel con el tamaño de la ventana
        pyxel.init(224, 224)
        # Establece el título de la ventana
        pyxel.title = "Pacman"
        # Carga los recursos del archivo .pyxres
        pyxel.load("assets/map.pyxres")
        self.mapa = Mapa()
        # Ejecuta el bucle principal
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)  # Limpia la pantalla
        self.mapa.draw()  # Dibuja el mapa

# Inicia la aplicación
App()
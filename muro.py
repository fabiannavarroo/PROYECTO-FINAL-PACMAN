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
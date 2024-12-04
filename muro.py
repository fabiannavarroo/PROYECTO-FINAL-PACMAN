import pyxel
from constantes import MUROS,TEXTO

class Muro:
    def __init__(self, bloque):

        self.bloque = bloque
        

    def colision(self, x, y):
        #Comprueba si hay un muro en la posición (x, y) 
        # Tamaño del sprite de Pac-Man y Fantasmas
        pass
    

    def draw(self):
        #Dibuja los muros en la pantalla
        #for elemento in self.bloque
        pass
    
    def fin(self):
        # Dibujar Game Over
        sprite = TEXTO["GAME OVER"]
        sprite_x, sprite_y = sprite["Coordenadas"]
        sprite_w, sprite_h = sprite["Tamaño"]
        pos_x = 192
        pos_y= 190
        pyxel.blt(pos_x, pos_y, 0, sprite_x, sprite_y, sprite_w, sprite_h, colkey=0)

    
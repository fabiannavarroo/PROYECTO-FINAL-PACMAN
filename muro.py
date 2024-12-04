import pyxel
from bloque import Bloque
from constantes import *

class Muro:
    def __init__(self):

        self.bloque = []
        for elemento in MAPA_1:
            self.bloques.append(Bloque(*elemento))
        

    def colision(self, x, y):
        #Comprueba si hay un muro en las coordenadas (x, y)
        pass
    

    def draw(self):
        #Dibuja los muros en la pantalla
        for elemento in self.bloque:
            pyxel.blt(elemento.x, elemento.y, *elemento.sprite)
            
    
    def fin(self):
        # Dibujar las vidas restantes
        sprite = TEXTO["GAME OVER"]
        sprite_x, sprite_y = sprite["Coordenadas"]
        sprite_w, sprite_h = sprite["Tamaño"]
        pos_x = 192
        pos_y= 190
        pyxel.blt(pos_x, pos_y, 0, sprite_x, sprite_y, sprite_w, sprite_h, colkey=0)

    
from constantes import OBJETOS, REFRESH_REGALOS, TEXTO, NUMEROS
from muro import Muro
import pyxel

class Puntos:
    def __init__(self,muro,sprite):
        self.muro = muro
        self.sprite = sprite
        self.puntos = 0

    def draw(self):

        for y in range (len(self.muro.mapa)):
            for x in range(len(self.muro.mapa[y])):
                if self.muro.mapa[y][x] == 0:
                    sprite = OBJETOS["BASTON"]
                    sprite_x, sprite_y = sprite["Coordenadas"]
                    sprite_w, sprite_h = 16, 16 # Ancho y largo del sprite
                    pyxel.blt(
                        x * self.muro.celda_tamaño, y * self.muro.celda_tamaño,  # Coordenadas donde se dibuja el punto
                        0,  # Banco de imágenes
                        sprite_x, sprite_y,  # Coordenadas del sprite en recursos.pyxres
                        sprite_w, sprite_h,  # Tamaño del sprite
                        colkey=0  # Transparencia
                    )
                if self.muro.mapa[y][x] == 98:
                    if pyxel.frame_count // REFRESH_REGALOS % 2:
                        sprite = OBJETOS["REGALO_BRILLANTE"]
                        sprite_x, sprite_y = sprite["Coordenadas"]
                        sprite_w, sprite_h = 16, 16 # Ancho y largo del sprite
                        
                    else:
                        sprite = OBJETOS["REGALO"]
                        sprite_x, sprite_y = sprite["Coordenadas"]
                        sprite_w, sprite_h = 16, 16 # Ancho y largo del sprite
                    
                    pyxel.blt( # Dibujar los imagenes de los regalos
                            x * self.muro.celda_tamaño, y * self.muro.celda_tamaño,  # Coordenadas donde se dibuja el punto
                            0,  # Banco de imágenes
                            sprite_x, sprite_y,  # Coordenadas del sprite en recursos.pyxres
                            sprite_w, sprite_h,  # Tamaño del sprite
                            colkey=0  # Transparencia
                        )
                if self.muro.mapa[y][x]==97:
                    sprite = NUMEROS["0"]
                    sprite_x,sprite_y = sprite["Coordenadas"]
                    sprite_w,sprite_h = sprite["Tamaño"]
    
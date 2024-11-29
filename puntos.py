from constantes import *
import random
from muro import Muro
import pyxel

class Puntos:
    def __init__(self,muro,sprite,pacman):
        self.muro = muro
        self.sprite = sprite
        self.pacman = pacman
        self.puntos = 0
        self.puntos_alcanzados = 0

    def draw(self):

        # Poner Los puntos en el mapa
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
                
                # Poner los pastillas de Poder, con su animación
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
                    sprite = TEXTO["HIGHSCORE"]
                    sprite_x,sprite_y = sprite["Coordenadas"]
                    sprite_w,sprite_h = sprite["Tamaño"]
                    pyxel.blt( # Dibujar los imagenes de los regalos
                            x * self.muro.celda_tamaño, y * self.muro.celda_tamaño,  # Coordenadas donde se dibuja el punto
                            0,  # Banco de imágenes
                            sprite_x, sprite_y,  # Coordenadas del sprite en recursos.pyxres
                            sprite_w, sprite_h,  # Tamaño del sprite
                            colkey=0  # Transparencia
                        )
                    
                if self.muro.mapa[y][x]==96:
                    sprite = TEXTO["READY!"]
                    sprite_x,sprite_y = sprite["Coordenadas"]
                    sprite_w,sprite_h = sprite["Tamaño"]
                    pyxel.blt( # Dibujar los imagenes de los regalos
                            x * self.muro.celda_tamaño, y * self.muro.celda_tamaño,  # Coordenadas donde se dibuja el punto
                            0,  # Banco de imágenes
                            sprite_x, sprite_y,  # Coordenadas del sprite en recursos.pyxres
                            sprite_w, sprite_h,  # Tamaño del sprite
                            colkey=0  # Transparencia
                        )
                
                if self.muro.mapa[y][x]==87:
                    sprite = TEXTO["GAME OVER"]
                    sprite_x,sprite_y = sprite["Coordenadas"]
                    sprite_w,sprite_h = sprite["Tamaño"]
                    pyxel.blt( # Dibujar los imagenes de los regalos
                            x * self.muro.celda_tamaño, y * self.muro.celda_tamaño,  # Coordenadas donde se dibuja el punto
                            0,  # Banco de imágenes
                            sprite_x, sprite_y,  # Coordenadas del sprite en recursos.pyxres
                            sprite_w, sprite_h,  # Tamaño del sprite
                            colkey=0  # Transparencia
                        )
        self.ver_puntuacion(188, 16)  # Mostrar la puntuación
                    

    def comer_puntos(self):
        pacman_x = self.pacman.x // self.muro.celda_tamaño  # Índice X en el mapa
        pacman_y = self.pacman.y // self.muro.celda_tamaño  # Índice Y en el mapa

        if self.muro.mapa[pacman_y][pacman_x] in [0, 98]:
            # Cuando se tratra de un punto normal
            if self.muro.mapa[pacman_y][pacman_x] == 0:
                tipo_consumible = "BASTON"
            # Cuando es una pastilla de poder
            elif self.muro.mapa[pacman_y][pacman_x] == 98:
                tipo_consumible = "REGALO"

            # Sumar puntos
            self.puntos += OBJETOS[tipo_consumible]["Puntos"]

            # Eliminar el objeto del mapa
            self.muro.mapa[pacman_y][pacman_x] = -1

    def ver_puntuacion(self, x, y):
        # Determina el color de los numero
        colores_dispo = [NUMEROS_BLANCOS,NUMEROS_MORADOS,NUMEROS_NARANJAS,NUMEROS_VERDES]
        color_numeros = NUMEROS_BLANCOS
        # Cambia el color solo cuando se supera un nuevo múltiplo de 500
        if self.puntos // 500 > self.umbral_actual:
            self.umbral_actual = self.puntos // 500  # Actualiza el umbral
            self.color_actual = random.choice(colores_dispo)  # Elige un nuevo color aleatorio
        # Convierte la puntuación en una cadena para obtener los dígitos
        puntuacion_str = str(self.puntos)

        # Coordenada inicial para el primer dígito
        pos_x = x

        for num in puntuacion_str:
            # Convierte el carácter a un entero
            num = int(num)

            # Obtiene el sprite correspondiente al dígito
            sprite = color_numeros[str(num)]
            sprite_x, sprite_y = sprite["Coordenadas"]
            sprite_w, sprite_h = sprite["Tamaño"]

            # Dibuja el número
            pyxel.blt(
                pos_x, y,           # Coordenadas en pantalla
                0,                  # Banco de imágenes
                sprite_x, sprite_y, # Coordenadas del sprite en el banco
                sprite_w, sprite_h, # Tamaño del sprite
                colkey=0            # Color transparente
            )
            # Incrementa la posición x para el siguiente dígito
            pos_x += sprite_w + 1  # Espacio entre los dígitos

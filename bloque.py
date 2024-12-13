import pyxel
from constantes import *
import random


class Bloque:
    def __init__(self):
        self.nivel = 1  # Nivel inicial
        self.celda_tamaño = 16
        self.bloques = []
        self.mapas = MAPA
        self.cargar_mapa()  # Cargar el mapa del nivel inicial
        # Controlar la condición de victoria
        self.victoria = False  
        self.victoria_contador_mapa = 0
        self.victoria_contador_texto = 0
        # Variable para controlar el mensaje READY!
        self.mostrar_ready = True
        self.contador_ready = 0
        # Variables para controlar GAME OVER
        self.contador_game_over = 0
        self.mostrar_fin = False
        # COntrola la musica actual
        self.elegir_cancion = random.random() # elegir la cancion del mapa 2
        self.musica_actual = None


#--------------------------------------------------------------------PROPERTY--------------------------------------------------------------------#

    @property
    def nivel(self):
        return self.__nivel

    @property
    def celda_tamaño(self):
        return self.__celda_tamaño

    @property
    def bloques(self):
        return self.__bloques

    @property
    def mapas(self):
        return self.__mapas
    
    @property
    def victoria(self):
        return self.__victoria
    
    @property
    def victoria_contador_mapa(self):
        return self.__victoria_contador_mapa
    
    @property
    def victoria_contador_texto(self):
        return self.__victoria_contador_texto
    
    @property
    def mostrar_ready(self):
        return self.__mostrar_ready
    
    @property
    def contador_ready(self):
        return self.__contador_ready
    
    @property
    def contador_game_over(self):
        return self.__contador_game_over
        
    @property
    def mostrar_fin(self):
        return self.__mostrar_fin
    
    @property
    def elegir_cancion(self):
        return self.__elegir_cancion
    
    @property
    def musica_actual(self):
        return self.__musica_actual
    
#--------------------------------------------------------------------SETTERS--------------------------------------------------------------------#
    @nivel.setter
    def nivel(self, nuevo_valor):
        self.__nivel = nuevo_valor

    @celda_tamaño.setter
    def celda_tamaño(self, nuevo_valor):
        self.__celda_tamaño = nuevo_valor
    
    @bloques.setter
    def bloques(self, nuevo_valor):
        self._bloques = nuevo_valor

    @mapas.setter
    def mapas(self, nuevo_valor):
        self.__mapas = nuevo_valor

    @victoria.setter
    def victoria(self, nuevo_valor):
        self.__victoria = nuevo_valor

    @victoria_contador_mapa.setter
    def victoria_contador_mapa(self, nuevo_valor):
        self.__victoria_contador_mapa = nuevo_valor

    @victoria_contador_texto.setter
    def victoria_contador_texto(self, nuevo_valor):
        self.__victoria_contador_texto = nuevo_valor

    @mostrar_ready.setter
    def mostrar_ready(self, nuevo_valor):
        self.__mostrar_ready = nuevo_valor

    @contador_ready.setter
    def contador_ready(self, nuevo_valor):
        self.__contador_ready = nuevo_valor

    @contador_game_over.setter
    def contador_game_over(self, nuevo_valor):
        self.__contador_game_over = nuevo_valor

    @mostrar_fin.setter
    def mostrar_fin(self, nuevo_valor):
        self.__mostrar_fin = nuevo_valor

    @elegir_cancion.setter
    def elegir_cancion(self, nuevo_valor):
        self.__elegir_cancion = nuevo_valor

    @musica_actual.setter
    def musica_actual(self, nuevo_valor):
        self.__musica_actual = nuevo_valor
        
#--------------------------------------------------------------------METODOS PROPIOS--------------------------------------------------------------------#    

    def cargar_mapa(self):
        # Cargar los bloques del nivel actual
        self.__bloques = []
        for x, y, tipo in self.__mapas[self.__nivel]:
            sprite = self.obtener_sprite(tipo)  # Obtener el sprite 
            self.bloques.append((x, y, sprite))  # Guardar solo coordenadas y sprite


    def obtener_sprite(self, tipo):
        # Devuelve el sprite correspondiente al tipo
        if self.__nivel == 1:
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
        elif self.__nivel == 2:
            if tipo == 1:
                return SPRITE_BLOQUE_1_1
            elif tipo == 2:
                return SPRITE_BLOQUE_2_1
            elif tipo == 3:
                return SPRITE_BLOQUE_3_1
            elif tipo == 4:
                return SPRITE_BLOQUE_4_1
            elif tipo == 5:
                return SPRITE_BLOQUE_5_1
            elif tipo == 6:
                return SPRITE_BLOQUE_6_1
            elif tipo == 7:
                return SPRITE_BLOQUE_7_1
            elif tipo == 8:
                return SPRITE_BLOQUE_8_1
            elif tipo == 9:
                return SPRITE_BLOQUE_9_1
            elif tipo == 10:
                return SPRITE_BLOQUE_10_1
            elif tipo == 11:
                return SPRITE_BLOQUE_11_1
            elif tipo == 12:
                return SPRITE_BLOQUE_12_1
            elif tipo == 13:
                return SPRITE_BLOQUE_13_1
            elif tipo == 14:
                return SPRITE_BLOQUE_14_1
            elif tipo == 15:
                return SPRITE_BLOQUE_15_1
            elif tipo == 16:
                return SPRITE_BLOQUE_16_1
            elif tipo == 17:
                return SPRITE_BLOQUE_17_1
            elif tipo == 18:
                return SPRITE_BLOQUE_18_1
            elif tipo == 19:
                return SPRITE_BLOQUE_19_1
            elif tipo == 20:
                return SPRITE_BLOQUE_20_1
            elif tipo == 21:
                return SPRITE_BLOQUE_21_1
            elif tipo == 22:
                return SPRITE_BLOQUE_22_1
            elif tipo == 23:
                return SPRITE_BLOQUE_23_1
            else:
                raise ValueError("Tipo de bloque no válido. Debe estar entre 1 y 23.")
        else:
            if tipo == 1:
                return SPRITE_BLOQUE_1_2
            elif tipo == 2:
                return SPRITE_BLOQUE_2_2
            elif tipo == 3:
                return SPRITE_BLOQUE_3_2
            elif tipo == 4:
                return SPRITE_BLOQUE_4_2
            elif tipo == 5:
                return SPRITE_BLOQUE_5_2
            elif tipo == 6:
                return SPRITE_BLOQUE_6_2
            elif tipo == 7:
                return SPRITE_BLOQUE_7_2
            elif tipo == 8:
                return SPRITE_BLOQUE_8_2
            elif tipo == 9:
                return SPRITE_BLOQUE_9_2
            elif tipo == 10:
                return SPRITE_BLOQUE_10_2
            elif tipo == 11:
                return SPRITE_BLOQUE_11_2
            elif tipo == 12:
                return SPRITE_BLOQUE_12_2
            elif tipo == 13:
                return SPRITE_BLOQUE_13_2
            elif tipo == 14:
                return SPRITE_BLOQUE_14_2
            elif tipo == 15:
                return SPRITE_BLOQUE_15_2
            elif tipo == 16:
                return SPRITE_BLOQUE_16_2
            elif tipo == 17:
                return SPRITE_BLOQUE_17_2
            elif tipo == 18:
                return SPRITE_BLOQUE_18_2
            elif tipo == 19:
                return SPRITE_BLOQUE_19_2
            elif tipo == 20:
                return SPRITE_BLOQUE_20_2
            elif tipo == 21:
                return SPRITE_BLOQUE_21_2
            elif tipo == 22:
                return SPRITE_BLOQUE_22_2
            elif tipo == 23:
                return SPRITE_BLOQUE_23_2
            elif tipo == 24:
                return SPRITE_BLOQUE_24_2
            else:
                raise ValueError("Tipo de bloque no válido. Debe estar entre 1 y 23.")


    def colision(self, x, y):
        sprite_tamaño = self.__celda_tamaño  # Tamaño del sprite (16x16 típico)

        # Calcular los puntos clave del sprite
        puntos_a_verificar = [
            (x, y),  # Esquina superior izquierda
            (x + sprite_tamaño - 1, y),  # Esquina superior derecha
            (x, y + sprite_tamaño - 1),  # Esquina inferior izquierda
            (x + sprite_tamaño - 1, y + sprite_tamaño - 1)  # Esquina inferior derecha
        ]

        # Verificar si algún punto clave está dentro de un bloque
        for px, py in puntos_a_verificar:
            for bloque_x, bloque_y, _ in self.__bloques:
                if (
                    bloque_x <= px < bloque_x + sprite_tamaño and
                    bloque_y <= py < bloque_y + sprite_tamaño
                ):
                    return True  # Colisión detectada

        return False  # No hay colisión


    def draw(self):
        # Dibuja todos los bloques
        for bloque in self.__bloques:
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



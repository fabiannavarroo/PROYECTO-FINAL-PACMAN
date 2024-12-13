from constantes import *
import random
import time
import pyxel


class Puntos:
    def __init__(self, sprite):
        self.sprite = sprite
        self.puntos = 0
        self.puntos_alcanzados = 0  # Rango de 500 en 500 de la última meta alcanzada de puntos
        self.color_actual = NUMEROS_BLANCOS  # Color inicial de los números
        self.ultimo_tiempo_fruta = time.time()  # Tiempo de la última fruta generada
        self.fruta_actual = None  # Información de la fruta actual
        self.posicion_fruta = None  # Posición actual de la fruta
        self.animacion_activa = False  # Indica si hay animación activa
        self.animacion_contador = 0  # Contador para animación de aparición
        self.zonas_prohibidas = ZONAS_PROHIBIDAS
        self.regalos = [(16, 304), (368, 304), (16, 80),(368, 80)] # Coordenadas fijas de los regalos
        self.lista_puntos = [] # Lista de puntos generados
        self.lista_frutas = [] # Lista de frutas generadas


#--------------------------------------------------------------------PROPERTY--------------------------------------------------------------------#
        # Solo lectura
        @property
        def sprite(self):
            return self.__sprite
        
        @property
        def puntos(self):
            return self.__puntos

        @property
        def puntos_alcanzados(self):
            return self.__puntos_alcanzados

        @property
        def color_actual(self):
            return self.__color_actual

        @property
        def ultimo_tiempo_fruta(self):
            return self.__ultimo_tiempo_fruta

        @property
        def fruta_actual(self):
            return self.__fruta_actual

        @property
        def posicion_fruta(self):
            return self.__posicion_fruta

        @property
        def animacion_activa(self):
            return self.__animacion_activa

        @property
        def animacion_contador(self):
            return self.__animacion_contador
        
        @property
        def zonas_prohibidas(self):
            return self.__zonas_prohibidas

        @property
        def regalos(self):
            return self.__regalos

        @property
        def lista_puntos(self):
            return self.__lista_puntos

        @property
        def lista_frutas(self):
            return self.__lista_frutas
        
#--------------------------------------------------------------------SETTERS--------------------------------------------------------------------#

        @puntos.setter
        def puntos(self, nuevo_valor):
            self.__puntos = nuevo_valor

        @puntos_alcanzados.setter
        def puntos_alcanzados(self, nuevo_valor):
            self.__puntos_alcanzados = nuevo_valor

        @color_actual.setter
        def color_actual(self, nuevo_valor):
            self.__color_actual = nuevo_valor

        @ultimo_tiempo_fruta.setter
        def ultimo_tiempo_fruta(self, nuevo_valor):
            self.__ultimo_tiempo_fruta = nuevo_valor

        @fruta_actual.setter
        def fruta_actual(self, nuevo_valor):
            self.__fruta_actual = nuevo_valor

        @posicion_fruta.setter
        def posicion_fruta(self, nuevo_valor):
            self.__posicion_fruta = nuevo_valor
        
        @animacion_activa.setter
        def animacion_activa(self, nuevo_valor):
            self.__animacion_activa = nuevo_valor

        @animacion_contador.setter
        def animacion_contador(self, nuevo_valor):
            self.__animacion_contador = nuevo_valor

        @zonas_prohibidas.setter
        def zonas_prohibidas(self, nuevo_valor):
            self.__zonas_prohibidas = nuevo_valor

        @regalos.setter
        def regalos(self, nuevo_valor):
            self.__regalos = nuevo_valor

        @lista_puntos.setter
        def lista_puntos(self, nuevo_valor):
            self.__lista_puntos = nuevo_valor

        @lista_frutas.setter
        def lista_frutas(self, nuevo_valor):
            self.__lista_frutas = nuevo_valor

#--------------------------------------------------------------------METODOS PROPIOS--------------------------------------------------------------------#
    def draw(self):
        # Dibuja los puntos, frutas y regalos en el mapa.
        # Dibujar puntos
        for x, y, tipo in self.lista_puntos:
            sprite = OBJETOS[tipo]["Coordenadas"]
            pyxel.blt(x, y, 0, sprite[0], sprite[1], 16, 16, colkey=0)

        # Dibujar fruta actual
        if self.posicion_fruta and self.fruta_actual:
            if self.animacion_activa and self.animacion_contador < 30:
                # Parpadea cada 5 frames
                if self.animacion_contador// REFRESH % 2 == 0:
                    sprite = OBJETOS[self.fruta_actual]["Coordenadas"]
                    pyxel.blt(self.posicion_fruta[0], self.posicion_fruta[1], 0, sprite[0], sprite[1], 16, 16, colkey=0)
                self.animacion_contador += 1
            else:
                # Detiene la animación y dibuja la fruta
                self.animacion_activa = False
                sprite = OBJETOS[self.fruta_actual]["Coordenadas"]
                pyxel.blt(self.posicion_fruta[0], self.posicion_fruta[1], 0, sprite[0], sprite[1], 16, 16, colkey=0)
            

        # Dibujar regalos
        for x, y in self.regalos:
            if pyxel.frame_count // REFRESH_REGALOS % 2:
                coord = OBJETOS["REGALO_BRILLANTE"]["Coordenadas"]
                pyxel.blt(x, y, 0, coord[0], coord[1], 16, 16, colkey=0)
            else:
                coord = OBJETOS["REGALO"]["Coordenadas"]
                pyxel.blt(x, y, 0, coord[0], coord[1], 16, 16, colkey=0)


    def ver_puntuacion(self, x, y):
        # Cambia el color solo cuando se supera un nuevo múltiplo de 500
        colores_dispo = [NUMEROS_BLANCOS, NUMEROS_MORADOS, NUMEROS_NARANJAS, NUMEROS_VERDES]
        if self.puntos // 500 > self.puntos_alcanzados:
            self.puntos_alcanzados = self.puntos // 500  # Actualiza los puntos alcanzados
            self.color_actual = random.choice(colores_dispo)  # Elige un nuevo color aleatorio

        color_numeros = self.color_actual
        puntuacion_str = str(self.puntos)
        pos_x = x

        for num in puntuacion_str:
            num = int(num)
            sprite = color_numeros[str(num)]
            sprite_x, sprite_y = sprite["Coordenadas"]
            sprite_w, sprite_h = sprite["Tamaño"]

            pyxel.blt(
                pos_x, y,
                0, sprite_x, sprite_y, sprite_w, sprite_h, colkey=0
            )
            pos_x += sprite_w + 1  # Espacio entre los numeros


    def esta_en_zona_prohibida(self, x, y, bloque):
        # Verificar si la posición (x, y) está en una zona prohibida
        for lugar in self.zonas_prohibidas[bloque.nivel]:
            x1, y1, x2, y2 = lugar
            if x1 <= x <= x2 and y1 <= y <= y2:
                return True

        # Comprobar también si hay un muro
        if bloque.colision(x, y):
            return True
        return False


    def encontrar_celdas_vacias(self,bloque):
        # Encuentra celdas vacías donde colocar frutas u otros objetos
        celdas_vacias = []
        for x in range(0, pyxel.width, 16):
            for y in range(0, pyxel.height, 16):
                # Verificar que no haya un punto en esa celda
                punto_encontrado = False
                for p in self.lista_puntos:
                    if (x, y) == (p[0], p[1]):
                        punto_encontrado = True
                
                # Debe no estar en zona prohibida, no ser la fruta actual ni un regalo
                if (not punto_encontrado and
                    not self.esta_en_zona_prohibida(x, y, bloque) and
                    (x, y) != self.posicion_fruta and
                    (x, y) not in self.regalos):
                    celdas_vacias.append((x, y))
        return celdas_vacias
    

    def generar_puntos(self,bloque):
            # Generar los puntos en todas las celdas válidas del mapa
            for x in range(0, pyxel.width, 16):
                for y in range(0, pyxel.height, 16):
                    if not self.esta_en_zona_prohibida(x, y, bloque) and (x, y) not in self.regalos:
                        self.lista_puntos.append((x, y, "BASTON"))


    def generar_fruta(self,bloque):
        # Generar una fruta cada 30 segundos, si es posible
        if time.time() - self.ultimo_tiempo_fruta < 30:
             return False

        objetos_dispo = ["CEREZA", "FRESA", "NARANJA", "MANZANA", "MELON", "PARAGUAS", "CAMPANA", "LLAVE"]
        self.fruta_actual = random.choice(objetos_dispo)

        celdas_vacias = self.encontrar_celdas_vacias(bloque)
        if celdas_vacias:
            self.posicion_fruta = random.choice(celdas_vacias)
            self.animacion_activa = True
            self.animacion_contador = 0
        else:
            self.posicion_fruta = None

        self.ultimo_tiempo_fruta = time.time()


    def comprobar_puntos_restantes(self):
        # Comprueba si ya no quedan puntos ni regalos
        if len(self.lista_puntos) == 0 and len(self.regalos) == 0:
            return True
        return False
    

    def detectar_colision_puntos(self, pacman_x, pacman_y, punto_x, punto_y):
        # Detecta si Pac-Man ha comido un punto
        return abs(pacman_x - punto_x) < 10 and abs(pacman_y - punto_y) < 10
    

    def comer_puntos(self, pacman_x, pacman_y,fantasmas):
        # Comprueba si Pac-Man ha comido puntos o regalos
        puntos_sin_comer = []
        for x, y, tipo in self.lista_puntos:
            if self.detectar_colision_puntos(pacman_x, pacman_y, x, y):
                self.puntos += OBJETOS[tipo]["Puntos"]
            else:
                puntos_sin_comer.append((x, y, tipo))
        self.lista_puntos = puntos_sin_comer

        regalos_sin_comer = []
        for x, y in self.regalos:
            if self.detectar_colision_puntos(pacman_x, pacman_y, x, y):
                # Comer un regalo hace que los fantasmas se pongan asustados
                for fantasma in fantasmas:
                    fantasma.activar_asustado()
                    fantasma.tiempo_asustado = time.time()
                self.puntos += OBJETOS["REGALO"]["Puntos"]
            else:
                regalos_sin_comer.append((x, y))
        self.regalos = regalos_sin_comer


    def comer_fruta(self, pacman_x, pacman_y):
        # Comprueba si Pac-Man ha comido la fruta
        if self.posicion_fruta and self.detectar_colision_puntos(pacman_x, pacman_y, self.posicion_fruta[0], self.posicion_fruta[1]):
            self.puntos += OBJETOS[self.fruta_actual]["Puntos"]
            self.posicion_fruta = None
            self.fruta_actual = None


    def reiniciar_puntos(self,bloque):
        # Reiniciar los puntos, regalos y frutas al cambiar de nivel
        self.regalos = [(16, 304), (368, 304), (16, 80),(368, 80)]
        self.lista_puntos = []
        self.generar_puntos(bloque)
        self.ultimo_tiempo_fruta = time.time()
        self.fruta_actual = None
        self.posicion_fruta = None
        self.animacion_activa = False
        self.animacion_contador = 0





    
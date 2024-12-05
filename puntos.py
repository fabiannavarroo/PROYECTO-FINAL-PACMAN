from constantes import *
import random
import time
import pyxel


class Puntos:
    def __init__(self, sprite, pacman, fantasmas):
        self.sprite = sprite
        self.pacman = pacman
        self.fantasmas = fantasmas
        self.puntos = 0
        self.puntos_alcanzados = 0  # Rango de 500 en 500 de la última meta alcanzada de puntos
        self.color_actual = NUMEROS_BLANCOS  # Color inicial de los números
        self.ultimo_tiempo_fruta = time.time()  # Tiempo de la última fruta generada
        self.fruta_actual = None  # Información de la fruta actual
        self.posicion_actual = None  # Posición actual de la fruta
        self.animacion_activa = False  # Indica si hay animación activa
        self.animacion_contador = 0  # Contador para animación de aparición
        self.zonas_prohibidas = [(0,0,384,16), (112,160,272,256), (0,192,80,224),(304,192,384,224)] # Zonas prohibidas para generar puntos
        self.regalos = [(16, 304), (368, 336), (16, 80),(368, 80)] # Coordenadas fijas de los regalos
        self.lista_puntos = [] # Lista de puntos generados
        self.generar_puntos()
        self.lista_frutas = [] # Lista de frutas generadas


    def generar_puntos(self):
        # Poner los puntos en el mapa
        for x in range(0, pyxel.width, 16):
            for y in range(0, pyxel.height, 16):
                if not self.esta_en_zona_prohibida(x, y):
                    self.lista_puntos.append((x, y, "BASTON")) 


    def esta_en_zona_prohibida(self, x, y):
        # Verifica si una posición está dentro de alguna zona prohibida.
        for lugar in self.zonas_prohibidas:
            x1, y1, x2, y2 = lugar
            if x1 <= x <= x2 and y1 <= y <= y2:
                return True
        return False
    
    def encontrar_celdas_vacias(self):
        # Encuentra celdas vacías en el mapa
        celdas_vacias = []
        for x in range(len(self.lista_puntos)):
            for y in range(len(self.lista_puntos[x])):
                if (self.lista_puntos[x][y][0], self.lista_puntos[x][y][1]) != self.posicion_actual:
                    celdas_vacias.append((self.lista_puntos[x][y][0], self.lista_puntos[x][y][1]))
        return celdas_vacias

    def generar_fruta(self):
        # Genera una fruta en una celda vacía.
        if time.time() - self.ultimo_tiempo_fruta < 30:
            return False  # No generar una nueva fruta si no han pasado 30 segundos

        # Seleccionar un objeto aleatorio sin regalos ni bastones
        objetos_dispo = ["CEREZA", "FRESA", "NARANJA", "MANZANA", "MELON", "PARAGUAS", "CAMPANA", "LLAVE"]
        self.fruta_actual = random.choice(objetos_dispo)

        # Elegir una posición aleatoria en celdas vacías
        celdas_vacias = self.encontrar_celdas_vacias()
        if celdas_vacias:  # Si existen posiciones vacías, genera la fruta y permite que se ejecute la animación
            self.posicion_actual = random.choice(celdas_vacias)
            self.animacion_activa = True  # Activa la animación
            self.animacion_contador = 0  # Reinicia el contador de la animación
        else:
            self.posicion_actual = None  # No hay espacio libre para generar una fruta

        # Actualiza el tiempo de la última fruta generada
        self.ultimo_tiempo_fruta = time.time()


    def comer_puntos(self):
        # Detecta si Pac-Man come un punto y lo elimina.
        nuevos_puntos = []
        for x, y, tipo in self.lista_puntos:
            if not (self.pacman.x <= x < self.pacman.x + 16 and self.pacman.y <= y < self.pacman.y + 16):
                nuevos_puntos.append((x, y, tipo))
            else:
                self.puntos += OBJETOS[tipo]["Puntos"]  # Incrementa los puntos según el tipo
        self.lista_puntos = nuevos_puntos


    def comer_fruta(self):
        # Detecta si Pac-Man come la fruta actual.
        if self.posicion_actual and self.pacman.x <= self.posicion_actual[0] < self.pacman.x + 16 and self.pacman.y <= self.posicion_actual[1] < self.pacman.y + 16:
            self.puntos += OBJETOS[self.fruta_actual]["Puntos"]  # Incrementa los puntos según la fruta
            self.posicion_actual = None  # Elimina la fruta actual
            self.fruta_actual = None


    def draw(self):
        # Dibuja los puntos, frutas y regalos en el mapa.
        # Dibujar puntos
        for x, y, tipo in self.lista_puntos:
            coord = OBJETOS[tipo]["Coordenadas"]
            pyxel.blt(x, y, 0, coord[0], coord[1], 16, 16, colkey=0)

        # Dibujar fruta actual
        if self.posicion_actual and self.fruta_actual:
            coord = OBJETOS[self.fruta_actual]["Coordenadas"]
            pyxel.blt(self.posicion_actual[0], self.posicion_actual[1], 0, coord[0], coord[1], 16, 16, colkey=0)

        # Dibujar regalos
        for x, y in self.regalos:

            coord = OBJETOS["REGALO"]["Coordenadas"]
            pyxel.blt(x, y, 0, coord[0], coord[1], 16, 16, colkey=0)

                    
        # Dibuja las letras
        self.dibujar_letras_mapa(69, "READY!")
        self.dibujar_letras_mapa(70, "HIGHSCORE")

        # Dibuja la fruta si existe
        if self.fruta_actual and self.posicion_actual:
            self.dibujar_fruta()

        # Mostrar la puntuación
        self.ver_puntuacion(195, 16)


    def dibujar_letras_mapa(self, num, sprite):
        pass


    def comer_puntos(self):
        # Detectar si Pac-Man come puntos o regalos
        
                # Activar el estado asustado para todos los fantasmas
            
            # Sumar puntos
        
        # Eliminar el objeto del mapa
        pass

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
            pos_x += sprite_w + 1  # Espacio entre los dígitos



    
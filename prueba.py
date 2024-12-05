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
        
        # Áreas prohibidas para generar puntos
        self.zonas_prohibidas = [
            (50, 50, 100, 100),  # Ejemplo: zona superior izquierda
            (150, 200, 250, 300)  # Ejemplo: zona inferior derecha
        ]

        # Coordenadas fijas de los regalos
        self.regalos = [(80, 80), (160, 160), (240, 240)]

        # Lista de puntos generados
        self.lista_puntos = []
        self.generar_puntos()

        # Lista de frutas generadas
        self.lista_frutas = []

    def generar_puntos(self):
        """
        Genera puntos en el mapa, asegurándose de que no caigan en zonas prohibidas.
        """
        for x in range(0, pyxel.width, 16):
            for y in range(0, pyxel.height, 16):
                if not self.esta_en_zona_prohibida(x, y):
                    self.lista_puntos.append((x, y, "BASTON"))  # Por defecto, se generan bastones

    def esta_en_zona_prohibida(self, x, y):
        """
        Verifica si una posición está dentro de alguna zona prohibida.
        """
        for zona in self.zonas_prohibidas:
            x1, y1, x2, y2 = zona
            if x1 <= x <= x2 and y1 <= y <= y2:
                return True
        return False

    def generar_fruta(self):
        """
        Genera una fruta en un espacio vacío cada 30 segundos.
        """
        tiempo_actual = time.time()
        if tiempo_actual - self.ultimo_tiempo_fruta >= 30:
            espacios_vacios = [(x, y) for x, y, _ in self.lista_puntos if (x, y) not in [(f[0], f[1]) for f in self.lista_frutas]]
            if espacios_vacios:
                fruta = random.choice(espacios_vacios)
                tipo_fruta = random.choice(list(OBJETOS.keys()))  # Seleccionar una fruta aleatoria
                self.lista_frutas.append((fruta[0], fruta[1], tipo_fruta))
            self.ultimo_tiempo_fruta = tiempo_actual

    def comer_puntos(self):
        """
        Detecta si Pac-Man come un punto y lo elimina.
        """
        nuevos_puntos = []
        for x, y, tipo in self.lista_puntos:
            if not (self.pacman.x <= x < self.pacman.x + 16 and self.pacman.y <= y < self.pacman.y + 16):
                nuevos_puntos.append((x, y, tipo))
            else:
                self.puntos += OBJETOS[tipo]["Puntos"]  # Incrementa los puntos según el tipo
        self.lista_puntos = nuevos_puntos

    def comer_fruta(self):
        """
        Detecta si Pac-Man come una fruta y la elimina.
        """
        nuevas_frutas = []
        for x, y, tipo in self.lista_frutas:
            if not (self.pacman.x <= x < self.pacman.x + 16 and self.pacman.y <= y < self.pacman.y + 16):
                nuevas_frutas.append((x, y, tipo))
            else:
                self.puntos += OBJETOS[tipo]["Puntos"]  # Incrementa los puntos según el valor de la fruta
        self.lista_frutas = nuevas_frutas

    def draw(self):
        """
        Dibuja los puntos, frutas y regalos en el mapa.
        """
        # Dibujar puntos
        for x, y, tipo in self.lista_puntos:
            coord = OBJETOS[tipo]["Coordenadas"]
            pyxel.blt(x, y, 0, coord[0], coord[1], 16, 16, colkey=0)

        # Dibujar frutas
        for x, y, tipo in self.lista_frutas:
            coord = OBJETOS[tipo]["Coordenadas"]
            pyxel.blt(x, y, 0, coord[0], coord[1], 16, 16, colkey=0)

        # Dibujar regalos
        for x, y in self.regalos:
            coord = OBJETOS["REGALO"]["Coordenadas"]
            pyxel.blt(x, y, 0, coord[0], coord[1], 16, 16, colkey=0)

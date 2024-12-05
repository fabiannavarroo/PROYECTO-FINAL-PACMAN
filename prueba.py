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

        # Información de fruta actual
        self.fruta_actual = None
        self.posicion_actual = None
        self.animacion_activa = False
        self.animacion_contador = 0

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

    def encontrar_celdas_vacias(self):
        """
        Encuentra celdas vacías donde no haya puntos ni frutas.
        """
        celdas_vacias = []
        for x, y, _ in self.lista_puntos:
            if (x, y) != self.posicion_actual:
                celdas_vacias.append((x, y))
        return celdas_vacias

    def generar_fruta(self):
        """
        Genera una fruta en una celda vacía.
        """
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
        Detecta si Pac-Man come la fruta actual.
        """
        if self.posicion_actual and self.pacman.x <= self.posicion_actual[0] < self.pacman.x + 16 and self.pacman.y <= self.posicion_actual[1] < self.pacman.y + 16:
            self.puntos += OBJETOS[self.fruta_actual]["Puntos"]  # Incrementa los puntos según la fruta
            self.posicion_actual = None  # Elimina la fruta actual
            self.fruta_actual = None

    def draw(self):
        """
        Dibuja los puntos, frutas y regalos en el mapa.
        """
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

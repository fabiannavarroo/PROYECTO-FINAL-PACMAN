from constantes import *
import random
import time
from muro import Muro
import pyxel


class Puntos:
    def __init__(self, muro, sprite, pacman, fantasmas):
        self.muro = muro
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
        self.victoria = False #selbsterklährend

    def draw(self):
        # Poner los puntos en el mapa
        for y in range(len(self.muro.mapa)):
            for x in range(len(self.muro.mapa[y])):
                if self.muro.mapa[y][x] == 0:
                    # Dibuja los puntos
                    sprite = OBJETOS["BASTON"]
                    sprite_x, sprite_y = sprite["Coordenadas"]
                    sprite_w, sprite_h = 16, 16  # Ancho y largo del sprite
                    pyxel.blt(
                        x * self.muro.celda_tamaño, y * self.muro.celda_tamaño,  # Coordenadas donde se dibuja el punto
                        0,  # Banco de imágenes
                        sprite_x, sprite_y,  # Coordenadas del sprite en recursos.pyxres
                        sprite_w, sprite_h,  # Tamaño del sprite
                        colkey=0  # Transparencia
                    )

                # Poner los regalos con su animación
                if self.muro.mapa[y][x] == 98:
                    if pyxel.frame_count // REFRESH_REGALOS % 2:
                        sprite = OBJETOS["REGALO_BRILLANTE"]
                        sprite_x, sprite_y = sprite["Coordenadas"]
                        sprite_w, sprite_h = 16, 16  # Ancho y largo del sprite
                    else:
                        sprite = OBJETOS["REGALO"]
                        sprite_x, sprite_y = sprite["Coordenadas"]
                        sprite_w, sprite_h = 16, 16  # Ancho y largo del sprite
                    # Dibuja el regalo
                    pyxel.blt(
                        x * self.muro.celda_tamaño, y * self.muro.celda_tamaño,
                        0, sprite_x, sprite_y, sprite_w, sprite_h, colkey=0
                    )

        # Dibuja las letras
        self.dibujar_letras_mapa(69, "READY!")
        self.dibujar_letras_mapa(70, "HIGHSCORE")

        # Dibuja la fruta si existe
        if self.fruta_actual and self.posicion_actual:
            self.dibujar_fruta()

        # Mostrar la puntuación
        self.ver_puntuacion(188, 16)


    def dibujar_letras_mapa(self, num, sprite):
        # Dibuja las letras en las posiciones indicadas por el mapa
        for y in range(len(self.muro.mapa)):
            for x in range(len(self.muro.mapa[y])):
                if self.muro.mapa[y][x] == num:
                    sprite = TEXTO[sprite]
                    sprite_x, sprite_y = sprite["Coordenadas"]
                    sprite_w, sprite_h = sprite["Tamaño"]
                    pyxel.blt(
                        x * self.muro.celda_tamaño, y * self.muro.celda_tamaño,
                        0, sprite_x, sprite_y, sprite_w, sprite_h, colkey=0
                    )


    def comer_puntos(self):
        # Detectar si Pac-Man come puntos o regalos
        pacman_x = self.pacman.x // self.muro.celda_tamaño
        pacman_y = self.pacman.y // self.muro.celda_tamaño

        if self.muro.mapa[pacman_y][pacman_x] in [0, 98]:
            if self.muro.mapa[pacman_y][pacman_x] == 0:
                tipo_consumible = "BASTON"
            elif self.muro.mapa[pacman_y][pacman_x] == 98:
                tipo_consumible = "REGALO"
                # Activar el estado asustado para todos los fantasmas
                for fantasma in self.fantasmas:
                    fantasma.activar_asustado()
            # Sumar puntos
            self.puntos += OBJETOS[tipo_consumible]["Puntos"]
            # Eliminar el objeto del mapa
            self.muro.mapa[pacman_y][pacman_x] = -1

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


    def encontrar_celdas_vacias(self):
        # Encuentra celdas vacías en el mapa
        celdas_vacias = []
        for y in range(len(self.muro.mapa)):
            for x in range(len(self.muro.mapa[y])):
                if self.muro.mapa[y][x] == -1:
                    celdas_vacias.append((x, y))
        return celdas_vacias


    def generar_fruta(self):
        # Genera una fruta en una celda vacía
        if time.time() - self.ultimo_tiempo_fruta < 30:
            return False # No generar una nueva fruta si no han pasado 30 segundos

        # Seleccionar un objeto aleatorio sin regalos ni bastones
        objetos_dispo = ["CEREZA", "FRESA", "NARANJA", "MANZANA", "MELON", "PARAGUAS", "CAMPANA", "LLAVE"]
        self.fruta_actual = random.choice(objetos_dispo)

        # Elegir una posición aleatoria en celdas vacías
        celdas_vacias = self.encontrar_celdas_vacias()
        if celdas_vacias: # Si existen posiciones vacias genera la fruta y permite que se ejecute la animacion
            self.posicion_actual = random.choice(celdas_vacias)
            self.animacion_activa = True  # Activa la animacion
            self.animacion_contador = 0  # Reinicia el contador de la animacion
        else:
            self.posicion_actual = None  # No hay espacio libre para generar una fruta

        # Actualiza el tiempo de la última fruta generada
        self.ultimo_tiempo_fruta = time.time()


    def dibujar_fruta(self):
        # Dibuja la fruta con animación al aparecer
        if self.animacion_activa and self.animacion_contador < 30:
            # Parpadea cada 5 frames
            if self.animacion_contador// REFRESH % 2 == 0:
                sprite = OBJETOS[self.fruta_actual]
                sprite_x, sprite_y = sprite["Coordenadas"]
                sprite_w, sprite_h = 16, 16
                x_pixel = self.posicion_actual[0] * self.muro.celda_tamaño
                y_pixel = self.posicion_actual[1] * self.muro.celda_tamaño
                pyxel.blt(
                    x_pixel, y_pixel, 0,
                    sprite_x, sprite_y, sprite_w, sprite_h, colkey=0
                )
            self.animacion_contador += 1
        else:
            # Detiene la animación y dibuja la fruta 
            self.animacion_activa = False
            sprite = OBJETOS[self.fruta_actual]
            sprite_x, sprite_y = sprite["Coordenadas"]
            sprite_w, sprite_h = 16, 16
            x_pixel = self.posicion_actual[0] * self.muro.celda_tamaño
            y_pixel = self.posicion_actual[1] * self.muro.celda_tamaño
            pyxel.blt(
                x_pixel, y_pixel, 0,
                sprite_x, sprite_y, sprite_w, sprite_h, colkey=0
            )


    def comer_fruta(self):
        # Detecta si Pacman está en la posición de la fruta y se la come :)
        pacman_x = self.pacman.x // self.muro.celda_tamaño
        pacman_y = self.pacman.y // self.muro.celda_tamaño
        #Suma los puntos de la fruta/objeto en caso de ser comido
        if self.posicion_actual == (pacman_x, pacman_y):
            self.puntos += OBJETOS[self.fruta_actual]["Puntos"]
            self.fruta_actual = None
            self.posicion_actual = None

    def victoria(self):
        if not (0,98) in self.muro.mapa:
            self.victoria=True

    
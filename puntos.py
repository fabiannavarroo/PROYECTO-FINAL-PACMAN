from constantes import *
import random
import time
import pyxel


class Puntos:
    def __init__(self, sprite, pacman, fantasmas, bloque):
        self.sprite = sprite
        self.pacman = pacman
        self.fantasmas = fantasmas
        self.bloque = bloque
        self.puntos = 0
        self.puntos_alcanzados = 0  # Rango de 500 en 500 de la última meta alcanzada de puntos
        self.color_actual = NUMEROS_BLANCOS  # Color inicial de los números
        self.ultimo_tiempo_fruta = time.time()  # Tiempo de la última fruta generada
        self.fruta_actual = None  # Información de la fruta actual
        self.posicion_actual = None  # Posición actual de la fruta
        self.animacion_activa = False  # Indica si hay animación activa
        self.animacion_contador = 0  # Contador para animación de aparición
        self.zonas_prohibidas = [(0,0,384,16), (112,160,272,256),(32,64,64,96),(96,64,160,96), (224,64,288,96),(320,64,352,96), (0,160,80, 256), (304, 160,384, 256)] # Zonas prohibidas para generar puntos
        self.regalos = [(16, 304), (368, 336), (16, 80),(368, 80)] # Coordenadas fijas de los regalos
        self.lista_puntos = [] # Lista de puntos generados
        self.generar_puntos()
        self.lista_frutas = [] # Lista de frutas generadas


    def draw(self):
        # Dibuja los puntos, frutas y regalos en el mapa.
        # Dibujar puntos
        for x, y, tipo in self.lista_puntos:
            sprite = OBJETOS[tipo]["Coordenadas"]
            pyxel.blt(x, y, 0, sprite[0], sprite[1], 16, 16, colkey=0)

        # Dibujar fruta actual
        if self.posicion_actual and self.fruta_actual:
            if self.animacion_activa and self.animacion_contador < 30:
                # Parpadea cada 5 frames
                if self.animacion_contador// REFRESH % 2 == 0:
                    sprite = OBJETOS[self.fruta_actual]["Coordenadas"]
                    pyxel.blt(self.posicion_actual[0], self.posicion_actual[1], 0, sprite[0], sprite[1], 16, 16, colkey=0)
                self.animacion_contador += 1
            else:
                # Detiene la animación y dibuja la fruta
                self.animacion_activa = False
                sprite = OBJETOS[self.fruta_actual]["Coordenadas"]
                pyxel.blt(self.posicion_actual[0], self.posicion_actual[1], 0, sprite[0], sprite[1], 16, 16, colkey=0)
            

        # Dibujar regalos
        for x, y in self.regalos:
            if pyxel.frame_count // REFRESH_REGALOS % 2:
                coord = OBJETOS["REGALO_BRILLANTE"]["Coordenadas"]
                pyxel.blt(x, y, 0, coord[0], coord[1], 16, 16, colkey=0)
            else:
                coord = OBJETOS["REGALO"]["Coordenadas"]
                pyxel.blt(x, y, 0, coord[0], coord[1], 16, 16, colkey=0)

        # Dibuja las letras
        self.dibujar_letras_mapa(180,240, "READY!")
        self.dibujar_letras_mapa(120,16, "HIGHSCORE")

        # Mostrar la puntuación
        self.ver_puntuacion(195, 16)


    def generar_puntos(self):
        # Poner los puntos en el mapa
        for x in range(0, pyxel.width, 16):
            for y in range(0, pyxel.height, 16):
                if not self.esta_en_zona_prohibida(x, y) and (x, y) not in self.regalos:
                    self.lista_puntos.append((x, y, "BASTON"))


    def esta_en_zona_prohibida(self, x, y):
        # Verificar si está en una zona prohibida
        for lugar in self.zonas_prohibidas:
            x1, y1, x2, y2 = lugar
            if x1 <= x <= x2 and y1 <= y <= y2:  
                return True

        # Verificar si hay un muro
        if self.bloque.colision(x, y):
            return True

        return False
    

    def encontrar_celdas_vacias(self):
        # Encuentra celdas vacías donde no haya puntos, frutas, regalos ni muros
        celdas_vacias = []
        x = 0
        while x < pyxel.width:
            y = 0
            while y < pyxel.height:
                # Verificar si la celda está vacía
                if not self.esta_en_zona_prohibida(x, y) and (x, y) not in [(p[0], p[1]) for p in self.lista_puntos] and (x, y) != self.posicion_actual and (x, y) not in self.regalos:
                    celdas_vacias.append((x, y))
                y += 16
            x += 16
        return celdas_vacias



    def generar_fruta(self):
        # Genera una fruta en una celda vacía
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
        # Detectar si Pac-Man come puntos
        puntos_sin_comer = []
        for x, y, tipo in self.lista_puntos:
            if self.pacman.x <= x < self.pacman.x + 16 and self.pacman.y <= y < self.pacman.y + 16:
                # Incrementar puntos según el tipo
                self.puntos += OBJETOS[tipo]["Puntos"]
            else:
                puntos_sin_comer.append((x, y, tipo))
        self.lista_puntos = puntos_sin_comer

        # Detectar si Pac-Man come un regalo
        regalos_sin_comer = []
        for x, y in self.regalos:
            if self.pacman.x <= x < self.pacman.x + 16 and self.pacman.y <= y < self.pacman.y + 16:
                # Activar estado asustado para los fantasmas
                for fantasma in self.fantasmas:
                    fantasma.activar_asustado()
                self.puntos += OBJETOS["REGALO"]["Puntos"]  # Incrementar los puntos por el regalo
            else:
                regalos_sin_comer.append((x, y))
        self.regalos = regalos_sin_comer


    def comer_fruta(self):
        # Detecta si Pac-Man come la fruta actual.
        if self.posicion_actual and self.pacman.x <= self.posicion_actual[0] < self.pacman.x + 16 and self.pacman.y <= self.posicion_actual[1] < self.pacman.y + 16:
            self.puntos += OBJETOS[self.fruta_actual]["Puntos"]  # Incrementa los puntos según la fruta
            self.posicion_actual = None  # Elimina la fruta actual
            self.fruta_actual = None


    def dibujar_letras_mapa(self, x , y, sprite):
        # Dibuja las letras en el mapa
        sprite=TEXTO[sprite]
        pyxel.blt(x, y, 0, sprite["Coordenadas"][0], sprite["Coordenadas"][1], sprite["Tamaño"][0], sprite["Tamaño"][1], colkey=0)


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



    
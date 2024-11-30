from constantes import *
from muro import MUROS
import pyxel

class Pacman:
    def __init__(self, x, y, muro):
        self.x = x
        self.y = y
        self.velocidad = 2  # Velocidad de movimiento
        self.muro = muro  # Mapa de muros
        self.direccion_actual = PACMAN  # Dirección inicial
        self.direccion_pendiente = None  # Dirección elegida por el jugador
        self.vidas = 3  # Pac-Man empieza con 3 vidas
        self.animacion_frame = 0
        self.en_muerte = False  # Indica si Pac-Man está en animación de muerte

    def mover(self):
        if self.vidas <= 0:  # Si no hay vidas, no se mueve
            return False

        nueva_x, nueva_y = self.x, self.y

        # Detectar entrada del jugador para cambiar dirección
        if pyxel.btnp(pyxel.KEY_UP):
            self.direccion_pendiente = PACMAN_ARRIBA
        elif pyxel.btnp(pyxel.KEY_DOWN):
            self.direccion_pendiente = PACMAN_ABAJO
        elif pyxel.btnp(pyxel.KEY_LEFT):
            self.direccion_pendiente = PACMAN_IZQUIERDA
        elif pyxel.btnp(pyxel.KEY_RIGHT):
            self.direccion_pendiente = PACMAN_DERECHA

        # Verificar si la dirección pendiente es válida
        if self.direccion_pendiente:
            if self.direccion_pendiente == PACMAN_ARRIBA and not self.muro.colision(self.x, self.y - self.velocidad):
                self.direccion_actual = self.direccion_pendiente
            elif self.direccion_pendiente == PACMAN_ABAJO and not self.muro.colision(self.x, self.y + self.velocidad):
                self.direccion_actual = self.direccion_pendiente
            elif self.direccion_pendiente == PACMAN_IZQUIERDA and not self.muro.colision(self.x - self.velocidad, self.y):
                self.direccion_actual = self.direccion_pendiente
            elif self.direccion_pendiente == PACMAN_DERECHA and not self.muro.colision(self.x + self.velocidad, self.y):
                self.direccion_actual = self.direccion_pendiente

        # Mover en la dirección actual
        if self.direccion_actual == PACMAN_ARRIBA:
            nueva_y -= self.velocidad
        elif self.direccion_actual == PACMAN_ABAJO:
            nueva_y += self.velocidad
        elif self.direccion_actual == PACMAN_IZQUIERDA:
            nueva_x -= self.velocidad
        elif self.direccion_actual == PACMAN_DERECHA:
            nueva_x += self.velocidad

        # Verificar colisiones
        if not self.muro.colision(nueva_x, self.y):
            self.x = nueva_x
        if not self.muro.colision(self.x, nueva_y):
            self.y = nueva_y

        # Manejar portales
        if (self.x, self.y) in PORTALES:
            self.x, self.y = PORTALES[(self.x, self.y)]

    def colision_fantasmas(self, fantasmas):
        if self.en_muerte or self.vidas <= 0:  # Si está muerto o sin vidas, no verifica colisiones
            return False

        pacman_x = self.x // self.muro.celda_tamaño
        pacman_y = self.y // self.muro.celda_tamaño

        for fantasma in fantasmas:
            fantasma_x = fantasma.x // self.muro.celda_tamaño
            fantasma_y = fantasma.y // self.muro.celda_tamaño

            if pacman_x == fantasma_x and pacman_y == fantasma_y:
                if fantasma.asustado:
                    fantasma.volver_a_trampa()  # Enviar fantasma a la trampa
                else:
                    self.perder_vida()  # Pac-Man pierde una vida

    def perder_vida(self):
        self.vidas -= 1
        self.en_muerte = True
        self.animacion_frame = 0

    def animar_muerte(self):
        if not self.en_muerte:
            return False

        if self.animacion_frame < len(ANIMACION_MUERTE):
            sprite_x, sprite_y = ANIMACION_MUERTE[self.animacion_frame]
            pyxel.blt(self.x, self.y, 0, sprite_x, sprite_y, 16, 16, colkey=0)
            if pyxel.frame_count % 5 == 0:  # Cambiar cada 5 frames
                self.animacion_frame += 1
        else:
            self.en_muerte = False  # Finaliza animación de muerte

    def draw(self):
        if self.vidas <= 0:  # Si no hay vidas, no se dibuja
            return False 

        if self.en_muerte:
            self.animar_muerte()
        else:
            if pyxel.frame_count // REFRESH % 2 == 0:
                sprite_x, sprite_y = self.direccion_actual
            else:
                sprite_x, sprite_y = PACMAN
            pyxel.blt(self.x, self.y, 0, sprite_x, sprite_y, 16, 16, colkey=0)
            self.ver_vidas(10, 10)

    def ver_vidas(self, x, y):
        # Dibujar las vidas restantes
        sprite_x, sprite_y = PACMAN
        sprite_w, sprite_h = 16, 16
        pos_x = x
        for i in range(self.vidas):
            pyxel.blt(pos_x, y, 0, sprite_x, sprite_y, sprite_w, sprite_h, colkey=0)
            pos_x += sprite_w + 2
from constantes import *
from muro import MUROS
import time
import pyxel

class Pacman:
    def __init__(self, x, y, muro):
        self.x = x
        self.y = y
        self.velocidad = 2
        self.muro = muro
        self.direccion_actual = PACMAN
        self.direccion_pendiente = None
        self.vidas = 3
        self.animacion_muerte = True
        self.animacion_frame = 0
        self.en_muerte = False

    def mover(self):
        nueva_x, nueva_y = self.x, self.y

        if pyxel.btnp(pyxel.KEY_UP):
            self.direccion_pendiente = PACMAN_ARRIBA
        elif pyxel.btnp(pyxel.KEY_DOWN):
            self.direccion_pendiente = PACMAN_ABAJO
        elif pyxel.btnp(pyxel.KEY_LEFT):
            self.direccion_pendiente = PACMAN_IZQUIERDA
        elif pyxel.btnp(pyxel.KEY_RIGHT):
            self.direccion_pendiente = PACMAN_DERECHA

        if self.direccion_pendiente:
            if self.direccion_pendiente == PACMAN_ARRIBA and not self.muro.colision(self.x, self.y - self.velocidad):
                self.direccion_actual = self.direccion_pendiente
            elif self.direccion_pendiente == PACMAN_ABAJO and not self.muro.colision(self.x, self.y + self.velocidad):
                self.direccion_actual = self.direccion_pendiente
            elif self.direccion_pendiente == PACMAN_IZQUIERDA and not self.muro.colision(self.x - self.velocidad, self.y):
                self.direccion_actual = self.direccion_pendiente
            elif self.direccion_pendiente == PACMAN_DERECHA and not self.muro.colision(self.x + self.velocidad, self.y):
                self.direccion_actual = self.direccion_pendiente

        if self.direccion_actual == PACMAN_ARRIBA:
            nueva_y -= self.velocidad
        elif self.direccion_actual == PACMAN_ABAJO:
            nueva_y += self.velocidad
        elif self.direccion_actual == PACMAN_IZQUIERDA:
            nueva_x -= self.velocidad
        elif self.direccion_actual == PACMAN_DERECHA:
            nueva_x += self.velocidad

        if not self.muro.colision(nueva_x, self.y):
            self.x = nueva_x
        if not self.muro.colision(self.x, nueva_y):
            self.y = nueva_y

        if (self.x, self.y) in PORTALES:
            self.x, self.y = PORTALES[(self.x, self.y)]

    def colision_fantasmas(self, fantasmas):
        if self.en_muerte:
            return

        pacman_x = self.x // self.muro.celda_tamaño
        pacman_y = self.y // self.muro.celda_tamaño

        for fantasma in fantasmas:
            fantasma_x = fantasma.x // self.muro.celda_tamaño
            fantasma_y = fantasma.y // self.muro.celda_tamaño

            if pacman_x == fantasma_x and pacman_y == fantasma_y:
                if fantasma.asustado:
                    fantasma.volver_a_trampa()
                else:
                    self.perder_vida()

    def perder_vida(self):
        self.vidas -= 1
        self.en_muerte = True
        self.animacion_frame = 0

    def reiniciar_posicion(self):
        self.x, self.y = 208, 288

    def animar_muerte(self):
        if self.en_muerte:
            frames = ANIMACION_MUERTE
            if self.animacion_frame < len(frames):
                sprite_x, sprite_y = frames[self.animacion_frame]
                pyxel.blt(self.x, self.y, 0, sprite_x, sprite_y, 16, 16, colkey=0)
                self.animacion_frame += 1
            else:
                self.en_muerte = False
                if self.vidas > 0:
                    self.reiniciar_posicion()
                else:
                    self.game_over()

    def draw(self):
        if self.en_muerte:
            self.animar_muerte()
        else:
            if pyxel.frame_count // REFRESH % 2 == 0:
                sprite_x, sprite_y = self.direccion_actual
            else:
                if self.direccion_actual == PACMAN_ARRIBA:
                    sprite_x, sprite_y = PACMAN_ARRIBA_CERRADA
                elif self.direccion_actual == PACMAN_ABAJO:
                    sprite_x, sprite_y = PACMAN_ABAJO_CERRADA
                elif self.direccion_actual == PACMAN_IZQUIERDA:
                    sprite_x, sprite_y = PACMAN_IZQUIERDA_CERRADA
                elif self.direccion_actual == PACMAN_DERECHA:
                    sprite_x, sprite_y = PACMAN_DERECHA_CERRADA
                else:
                    sprite_x, sprite_y = PACMAN

            pyxel.blt(self.x, self.y, 0, sprite_x, sprite_y, 16, 16, colkey=0)
            self.ver_vidas(10, 10)

    def ver_vidas(self, x, y):
        sprite_x, sprite_y = PACMAN
        sprite_w, sprite_h = 16, 16
        pos_x = x
        for i in range(self.vidas):
            pyxel.blt(pos_x, y, 0, sprite_x, sprite_y, sprite_w, sprite_h, colkey=0)
            pos_x += sprite_w + 2

    def game_over(self):
        for y in range(len(self.muro.mapa)):
            for x in range(len(self.muro.mapa[y])):
                if self.muro.mapa[y][x] not in OBJETOS_MURO:
                    self.muro.mapa[y][x] = -1

        self.muro.mapa[12][13] = 71  # Mostrar "GAME OVER"
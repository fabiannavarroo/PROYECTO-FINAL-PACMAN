from constantes import *
import pyxel
import time

class Pacman:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidad = 2  # Velocidad de movimiento
        self.direccion_actual = PACMAN  # Dirección inicial
        self.direccion_pendiente = None  # Dirección elegida por el jugador
        self.vidas = 3  # Pac-Man empieza con 3 vidas
        self.animacion_frame = 0
        self.en_muerte = False  # Indica si Pac-Man está en animación de muerte
        self.reiniciando = False  # Estado para evitar colisiones durante el reinicio
        self.fantasmas_comido = False
        self.mostrar_puntos = False
        self.texto_tiempo_inicio = 0
        self.posicion_fantasma_comido_x,self.posicion_fantasma_comido_y = 0,0
         



    def draw(self):
        if self.vidas <= 0:  # Si no hay vidas, no se dibuja
            return

        if self.en_muerte:
            
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
            # Dibujar Pac-Man
            pyxel.blt(self.x, self.y, 0, sprite_x, sprite_y, 16, 16, colkey=0)

            # Dibujar vidas
            self.ver_vidas(10, 10)

    def perder_vida(self):
        self.vidas -= 1
        self.en_muerte = True
        self.animacion_frame = 0
        self.reiniciando = True  # Activar estado de reinicio


    def ver_vidas(self, x, y):
        # Dibujar las vidas restantes
        sprite_x, sprite_y = PACMAN
        sprite_w, sprite_h = 16, 16
        pos_x = x
        for i in range(self.vidas):
            pyxel.blt(pos_x, y, 0, sprite_x, sprite_y, sprite_w, sprite_h, colkey=0)
            pos_x += sprite_w + 2


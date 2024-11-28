from constantes import PACMAN, PACMAN_ARRIBA, PACMAN_ABAJO, PACMAN_IZQUIERDA, PACMAN_DERECHA,PORTALES, REFRESH, TEXTO_MUERTE
import pyxel

class Pacman:
    def __init__(self, x, y, muro):
        self.x = x
        self.y = y
        self.velocidad = 2 # Velocidad
        self.muro = muro  # Referencia a la clase Muro
        self.direccion_actual = PACMAN  # Dirección inicial
        self.direccion_pendiente = None  # Dirección seleccionada por el jugador

    def mover(self):
        nueva_x, nueva_y = self.x, self.y

        # Detectar entrada del jugador para cambiar dirección pendiente
        if pyxel.btnp(pyxel.KEY_UP):
            self.direccion_pendiente = PACMAN_ARRIBA
        elif pyxel.btnp(pyxel.KEY_DOWN):
            self.direccion_pendiente = PACMAN_ABAJO
        elif pyxel.btnp(pyxel.KEY_LEFT):
            self.direccion_pendiente = PACMAN_IZQUIERDA
        elif pyxel.btnp(pyxel.KEY_RIGHT):
            self.direccion_pendiente = PACMAN_DERECHA
        if pyxel.btnp(pyxel.KEY_W):
            self.direccion_pendiente = PACMAN_ARRIBA
        elif pyxel.btnp(pyxel.KEY_S):
            self.direccion_pendiente = PACMAN_ABAJO
        elif pyxel.btnp(pyxel.KEY_A):
            self.direccion_pendiente = PACMAN_IZQUIERDA
        elif pyxel.btnp(pyxel.KEY_D):
            self.direccion_pendiente = PACMAN_DERECHA

        # Verificar si la dirección pendiente no tiene colisión
        if self.direccion_pendiente:
            if self.direccion_pendiente == PACMAN_ARRIBA and not self.muro.colision(self.x, self.y - self.velocidad):
                self.direccion_actual = self.direccion_pendiente
                self.direccion_pendiente = None
            elif self.direccion_pendiente == PACMAN_ABAJO and not self.muro.colision(self.x, self.y + self.velocidad):
                self.direccion_actual = self.direccion_pendiente
                self.direccion_pendiente = None
            elif self.direccion_pendiente == PACMAN_IZQUIERDA and not self.muro.colision(self.x - self.velocidad, self.y):
                self.direccion_actual = self.direccion_pendiente
                self.direccion_pendiente = None
            elif self.direccion_pendiente == PACMAN_DERECHA and not self.muro.colision(self.x + self.velocidad, self.y):
                self.direccion_actual = self.direccion_pendiente
                self.direccion_pendiente = None

        # Mover en la dirección actual
        if self.direccion_actual == PACMAN_ARRIBA:
            nueva_y -= self.velocidad
        elif self.direccion_actual == PACMAN_ABAJO:
            nueva_y += self.velocidad
        elif self.direccion_actual == PACMAN_IZQUIERDA:
            nueva_x -= self.velocidad
        elif self.direccion_actual == PACMAN_DERECHA:
            nueva_x += self.velocidad

        # Verificar colisión antes de actualizar la posición
        if not self.muro.colision(nueva_x, self.y):
            self.x = nueva_x
        if not self.muro.colision(self.x, nueva_y):
            self.y = nueva_y

        # Portal
        if (self.x, self.y) in PORTALES:
            self.x, self.y = PORTALES[(self.x, self.y)]

        #Ver las coordenadas del PacMan en la consola
        print("Pacman:", self.x, self.y, end="\n")

    def draw(self):
        # Alternar entre sprites para la animación
        if pyxel.frame_count // REFRESH % 2 == 0:
            # Dibujar Pac-Man con la boca cerrada
            sprite_x, sprite_y = PACMAN
        else:
            # Dibujar Pac-Man con la boca abierta en la dirección actual
            sprite_x, sprite_y = self.direccion_actual

        # Dibujar el sprite de PacMan
        pyxel.blt(self.x, self.y, 0, sprite_x, sprite_y, 16, 16, colkey=0)
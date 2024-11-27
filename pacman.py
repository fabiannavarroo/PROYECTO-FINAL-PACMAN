from constantes import PACMAN, PACMAN_ARRIBA, PACMAN_ABAJO, PACMAN_IZQUIERDA, PACMAN_DERECHA,PORTALES
import pyxel

class Pacman:
    def __init__(self, x, y, muro):
        self.x = x
        self.y = y
        self.velocidad = 2
        self.muro = muro  # Referencia a la clase Muro
        self.direccion_actual = PACMAN  # Dirección inicial
    

    def mover(self):
        nueva_x, nueva_y = self.x, self.y

        # Control de movimiento usando teclas
        if pyxel.btn(pyxel.KEY_UP):
            nueva_y -= self.velocidad
            self.direccion_actual = PACMAN_ARRIBA
        if pyxel.btn(pyxel.KEY_DOWN):
            nueva_y += self.velocidad
            self.direccion_actual = PACMAN_ABAJO
        if pyxel.btn(pyxel.KEY_LEFT):
            nueva_x -= self.velocidad
            self.direccion_actual = PACMAN_IZQUIERDA
        if pyxel.btn(pyxel.KEY_RIGHT):
            nueva_x += self.velocidad
            self.direccion_actual = PACMAN_DERECHA
        if pyxel.btn(pyxel.KEY_W):
            nueva_y -= self.velocidad
            self.direccion_actual = PACMAN_ARRIBA
        if pyxel.btn(pyxel.KEY_S):
            nueva_y += self.velocidad
            self.direccion_actual = PACMAN_ABAJO
        if pyxel.btn(pyxel.KEY_A):
            nueva_x -= self.velocidad
            self.direccion_actual = PACMAN_IZQUIERDA
        if pyxel.btn(pyxel.KEY_D):
            nueva_x += self.velocidad
            self.direccion_actual = PACMAN_DERECHA

        # Verificar colisión antes de actualizar la posición
        if not self.muro.colision(nueva_x, self.y):
            self.x = nueva_x
        if not self.muro.colision(self.x, nueva_y):
            self.y = nueva_y

        #Portal
        if (self.x,self.y)in PORTALES:
            self.x,self.y = PORTALES[(self.x,self.y)]
        print("Pacman:",self.x,self.y,end="\n")

    def draw(self):
        sprite_x, sprite_y = self.direccion_actual
        pyxel.blt(self.x, self.y, 0, sprite_x, sprite_y, 16, 16, colkey=0)
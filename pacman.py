from constantes import PACMAN, PACMAN_ARRIBA, PACMAN_ABAJO, PACMAN_IZQUIERDA, PACMAN_DERECHA,PORTALES, TEXTO_M, REFRESH
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
        # Alternar entre sprites para la animación
        if pyxel.frame_count // REFRESH % 5 == 0:
            # Dibujar Pac-Man con la boca cerrada
            sprite_x, sprite_y = PACMAN
        else:
            # Dibujar Pac-Man con la boca abierta en la dirección actual
            sprite_x, sprite_y = self.direccion_actual

        # Dibujar el sprite correspondiente
        pyxel.blt(self.x, self.y, 0, sprite_x, sprite_y, 16, 16, colkey=0)

    def draw_death(self):
        
        pyxel.cls(col=0)
        display_text = TEXTO_M
        #display_text.insert(1, f"{self.score:04}")
        for i, text in enumerate(display_text):
            y_offset = (pyxel.FONT_HEIGHT + 2) * i
            text_x = self.center_text(text, 430)
            pyxel.text(text_x, y_offset, text,15)
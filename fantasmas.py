import pyxel

class Fantasma:
    def __init__(self, x, y, sprites, muro):
        self.x = x
        self.y = y
        self.sprites = sprites  # Diccionario con las direcciones del sprite
        self.direccion_actual = self.sprites["DERECHA"]
        self.velocidad = 1
        self.muro = muro  # Referencia al mapa para las colisiones
        self.en_trampa = True  # Indica si el fantasma está en la trampa
        self.salida_trampa = False  # Si el fantasma puede salir de la trampa

    def puede_salir(self):
        #Determina si el fantasma puede salir de la trampa.
        if self.x == 112 and self.y == 120:  # Coordenadas específicas de la puerta
            self.salida_trampa = True

    def mover(self):
        nueva_x, nueva_y = self.x, self.y

        if self.en_trampa:
            self.puede_salir()
            if self.salida_trampa:
                # Movimiento hacia la salida de la trampa
                nueva_y -= self.velocidad
                if nueva_y < 104:  # Coordenada fuera de la trampa
                    self.en_trampa = False
        else:
            # Movimiento normal después de salir de la trampa
            nueva_x += self.velocidad

            # Cambiar de dirección si se encuentra con un muro
            if self.muro.colision(nueva_x, self.y):
                self.velocidad *= -1
                self.direccion_actual = self.sprites["IZQUIERDA"] if self.velocidad < 0 else self.sprites["DERECHA"]
            else:
                self.x = nueva_x
                self.y = nueva_y

    def draw(self):
        sprite_x, sprite_y = self.direccion_actual
        pyxel.blt(self.x, self.y, 0, sprite_x, sprite_y, 16, 16, colkey=0)
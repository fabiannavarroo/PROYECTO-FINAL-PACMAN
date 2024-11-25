import pyxel

class Fantasma:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color  # Identifica al fantasma (rojo, rosa, azul, naranja)
        self.direccion = 1  # Dirección inicial: 1 (derecha), -1 (izquierda)
        self.velocidad = 1

    def mover(self):
        # Movimiento horizontal básico
        self.x += self.direccion * self.velocidad

        # Cambiar de dirección si alcanza los bordes
        if self.x < 0 or self.x > pyxel.width - 16:
            self.direccion *= -1

    def dibujar(self):
        # Coordenadas del sprite según el color
        sprite_coords = {
            "rojo": (0, 64),
            "rosa": (0, 96),
            "azul": (0, 48),
            "naranja": (0, 80)
        }
        sprite_x, sprite_y = sprite_coords[self.color]
        sprite_w = 16  # Ancho del sprite
        sprite_h = 16  # Alto del sprite

        # Dibuja el fantasma sin reducir el tamaño
        pyxel.blt(
            self.x, self.y, 
            0,  # Banco de imágenes
            sprite_x, sprite_y, 
            sprite_w, sprite_h, 
            colkey=0  # Transparencia
        )

# Subclases para cada fantasma
class FantasmaRojo(Fantasma):
    def __init__(self, x, y):
        super().__init__(x, y, "rojo")

class FantasmaRosa(Fantasma):
    def __init__(self, x, y):
        super().__init__(x, y, "rosa")

class FantasmaAzul(Fantasma):
    def __init__(self, x, y):
        super().__init__(x, y, "azul")

class FantasmaNaranja(Fantasma):
    def __init__(self, x, y):
        super().__init__(x, y, "naranja")
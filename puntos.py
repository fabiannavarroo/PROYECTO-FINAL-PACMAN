from constantes import MINI_PUNTOS
from muro import MURO

class Puntos:
    def __init__(self,muro,sprite):
        self.muro = muro
        self.sprite = sprite

    def pintar_puntos(self):
        self.muro.mapa
        for y in range(self.muro.mapa):
            for x in range(self.muro.mapa[y]):
                if 
from muro import Muro
from pacman import Pacman
from fantasmas import FantasmaRojo, FantasmaRosa, FantasmaAzul, FantasmaNaranja
from puntos import Puntos
from constantes import *
import pyxel

class Tablero:
    def __init__(self):
        pyxel.init(430, 415, title="Pacman")  # Tamaño de la Pantalla
        pyxel.load("assets/recursos.pyxres")

        self.muro = Muro()
        self.pacman = Pacman(208, 288, self.muro,display_scale=26)  # Coordenadas iniciales del Pacman
        self.puntos= Puntos(self.muro, OBJETOS)
        self.fantasmas = [
            FantasmaRojo(160, 190, self.muro),  # Coordenadas iniciales en la trampa
            FantasmaRosa(176, 190, self.muro),
            FantasmaAzul(192, 190, self.muro),
            FantasmaNaranja(208, 190, self.muro)
        ]

        pyxel.run(self.update, self.draw)

    def update(self):
        self.pacman.mover()
        for fantasma in self.fantasmas:
            fantasma.mover()

    def draw(self):
        pyxel.cls(0)
        self.puntos.draw()
        self.muro.draw()
        self.pacman.draw()
        for fantasma in self.fantasmas:
            fantasma.draw()
        
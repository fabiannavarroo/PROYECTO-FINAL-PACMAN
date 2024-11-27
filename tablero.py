from muro import Muro
from pacman import Pacman
from fantasmas import FantasmaRojo, FantasmaRosa, FantasmaAzul, FantasmaNaranja
import pyxel

class Tablero:
    def __init__(self):
        pyxel.init(430, 415, title="Pacman")
        pyxel.load("assets/recursos.pyxres")

        self.muro = Muro()
        self.pacman = Pacman(208, 226, self.muro)

        self.fantasmas = [
            FantasmaRojo(160, 115, self.muro),  # Coordenadas iniciales en la trampa
            FantasmaRosa(58, 192, self.muro),
            FantasmaAzul(192, 145, self.muro),
            FantasmaNaranja(208, 145, self.muro)
        ]

        pyxel.run(self.update, self.draw)

    def update(self):
        self.pacman.mover()
        for fantasma in self.fantasmas:
            fantasma.mover()

    def draw(self):
        pyxel.cls(0)
        self.muro.draw()
        self.pacman.draw()
        for fantasma in self.fantasmas:
            fantasma.draw()
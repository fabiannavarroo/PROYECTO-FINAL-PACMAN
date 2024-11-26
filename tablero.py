

from muro import Muro
from pacman import Pacman
from fantasmas import FantasmaRojo, FantasmaRosa, FantasmaAzul, FantasmaNaranja
import pyxel

class Tablero:
    def __init__(self):
        pyxel.init(432, 432, title="Pacman")
        pyxel.load("assets/recursos.pyxres")
        self.muro = Muro()
        self.pacman = Pacman(208, 240, self.muro)
        self.fantasmas = [
            FantasmaRojo(208, 224, self.muro),
            FantasmaRosa(224, 224, self.muro),
            FantasmaAzul(240, 224, self.muro),
            FantasmaNaranja(256, 224, self.muro)
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


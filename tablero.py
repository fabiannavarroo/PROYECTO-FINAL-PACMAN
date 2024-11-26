from muro import Muro
from pacman import Pacman
from fantasmas import FantasmaRojo, FantasmaRosa, FantasmaAzul, FantasmaNaranja
import pyxel

class Tablero:
    def __init__(self):
        pyxel.init(430, 333, title="Pacman")
        pyxel.load("assets/recursos.pyxres")

        self.muro = Muro()
        self.pacman = Pacman(112, 200, self.muro)

        self.fantasmas = [
            FantasmaRojo(112, 160, self.muro),
            FantasmaRosa(128, 160, self.muro),
            FantasmaAzul(144, 160, self.muro),
            FantasmaNaranja(160, 160, self.muro),
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
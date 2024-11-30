from muro import Muro
from pacman import Pacman
from fantasmas import *
from puntos import Puntos
from constantes import *
import pyxel

class Tablero:
    def __init__(self):
        pyxel.init(430, 415, title="Pacman", display_scale=1, fps=30)
        pyxel.load("assets/recursos.pyxres")

        self.muro = Muro()
        self.pacman = Pacman(208, 288, self.muro)
        self.fantasmas = [
            FantasmaRojo(200, 160, self.muro),
            FantasmaRosa(176, 190, self.muro),
            FantasmaAzul(192, 190, self.muro),
            FantasmaNaranja(208, 190, self.muro)
        ]
        self.puntos = Puntos(self.muro, OBJETOS, self.pacman, self.fantasmas)

        pyxel.run(self.update, self.draw)

    def update(self):
        if self.pacman.vidas > 0:
            if self.pacman.en_muerte:
                self.pacman.animar_muerte()
            else:
                self.pacman.mover()
                self.puntos.comer_puntos()
                self.puntos.comer_fruta()
                for fantasma in self.fantasmas:
                    fantasma.actualizar_estado()
                self.pacman.colision_fantasmas(self.fantasmas)
        else:
            self.reiniciar_tablero()

    def draw(self):
        pyxel.cls(0)
        self.puntos.draw()
        self.muro.draw()
        self.pacman.draw()
        for fantasma in self.fantasmas:
            fantasma.draw()

    def reiniciar_tablero(self):
        self.pacman.reiniciar_posicion()
        self.pacman.en_muerte = False
        self.pacman.animacion_frame = 0
        for fantasma in self.fantasmas:
            fantasma.volver_a_trampa()
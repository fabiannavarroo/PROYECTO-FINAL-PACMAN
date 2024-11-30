from muro import Muro
from pacman import Pacman
from fantasmas import FantasmaRojo, FantasmaRosa, FantasmaAzul, FantasmaNaranja
from puntos import Puntos
from constantes import *
import pyxel

class Tablero:
    def __init__(self):
        pyxel.init(430, 415, title="Pacman",display_scale=2)  # Tamaño de la Pantalla
        pyxel.load("assets/recursos.pyxres")

        self.muro = Muro()
        self.pacman = Pacman(208, 288, self.muro)  # Coordenadas iniciales del Pacman
        self.puntos= Puntos(self.muro, OBJETOS, self.pacman)
        self.fantasmas = [
            FantasmaRojo(160, 160, self.muro),  # Coordenadas iniciales en la trampa
            FantasmaRosa(176, 190, self.muro),
            FantasmaAzul(192, 190, self.muro),
            FantasmaNaranja(208, 190, self.muro)
        ]

        pyxel.run(self.update, self.draw)

    def update(self):
        self.pacman.mover()
        self.puntos.comer_puntos()   # Verificar si Pacman comio un punto
        self.puntos.generar_fruta()  # Generar frutas cada 30 segundos.
        self.puntos.comer_fruta()    # Verificar si Pacman comio la fruta.


    def draw(self):
        pyxel.cls(0)
        self.puntos.draw()
        self.muro.draw()
        self.pacman.draw()
        for fantasma in self.fantasmas:
            fantasma.draw()

        
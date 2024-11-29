from muro import Muro
from pacman import Pacman
from fantasmas import FantasmaRojo, FantasmaRosa, FantasmaAzul, FantasmaNaranja
from puntos import Puntos
from constantes import *
import pyxel

class Tablero:
    def __init__(self):
        pyxel.init(430, 415, title="Pacman",display_scale=1)  # Tamaño de la Pantalla
        pyxel.load("assets/recursos.pyxres")

        self.muro = Muro()
        self.pacman = Pacman(208, 288, self.muro)  # Coordenadas iniciales del Pacman
        self.puntos= Puntos(self.muro, OBJETOS)
        self.fantasmas = [
            FantasmaRojo(160, 158, self.muro),  # Coordenadas iniciales en la trampa
            FantasmaRosa(176, 190, self.muro),
            FantasmaAzul(192, 190, self.muro),
            FantasmaNaranja(208, 190, self.muro)
        ]
        # Verificar la posición inicial del fantasma rojo
        print(f"Posición inicial del Fantasma Rojo: x=160, y=158, transitabilidad={not self.muro.colision(160, 158)}")

        pyxel.run(self.update, self.draw)

    def update(self):
        self.pacman.mover()
        self.fantasmas[0].mover(self.pacman.x, self.pacman.y)

    def draw(self):
        pyxel.cls(0)
        self.puntos.draw()
        self.muro.draw()
        self.pacman.draw()
        for fantasma in self.fantasmas:
            fantasma.draw()
        
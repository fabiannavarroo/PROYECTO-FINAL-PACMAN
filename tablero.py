


from muro import Muro
from pacman import Pacman
from fantasmas import FantasmaRojo, FantasmaRosa, FantasmaAzul, FantasmaNaranja
import pyxel


class Tablero:
    def __init__(self):
        pyxel.init(430, 333, title="Pacman")  # Dimensiones ajustadas al mapa 
        pyxel.load("assets/recursos.pyxres")

        # Inicializar el mapa (muros)
        self.muro = Muro()

        # Inicializar a Pac-Man
        self.pacman = Pacman(208, 240, self.muro)

        # Inicializar los fantasmas
        self.fantasmas = [
            FantasmaRojo(160, 130, self.muro),  # Coordenadas iniciales en la trampa
            FantasmaRosa(224, 184, self.muro),
            FantasmaAzul(240, 184, self.muro),
        FantasmaNaranja(256, 184, self.muro)
        ]

        pyxel.run(self.update, self.draw)

    def update(self):
        self.pacman.mover()
        for fantasma in self.fantasmas:
            fantasma.mover()

    def draw(self):
        pyxel.cls(0)
        self.muro.draw()  # Dibujar los muros
        self.pacman.draw()  # Dibujar Pac-Man
        for fantasma in self.fantasmas:
            fantasma.draw()  # Dibujar fantasmas

# Ejecutar la aplicación
Tablero()
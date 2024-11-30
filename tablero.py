from muro import Muro
from pacman import Pacman
from fantasmas import FantasmaRojo, FantasmaRosa, FantasmaAzul, FantasmaNaranja
from puntos import Puntos
from constantes import *
import pyxel

class Tablero:
    def __init__(self):
        pyxel.init(430, 415, title="Pacman", display_scale=1, fps=30)  # Tamaño de la Pantalla
        pyxel.load("assets/recursos.pyxres")

        self.muro = Muro()
        self.pacman = Pacman(208, 288, self.muro)  # Coordenadas iniciales del Pacman
        
        # Inicializar los fantasmas primero
        self.fantasmas = [
            FantasmaRojo(200, 160, self.muro),  # Coordenadas iniciales en la trampa
            FantasmaRosa(176, 190, self.muro),
            FantasmaAzul(192, 190, self.muro),
            FantasmaNaranja(208, 190, self.muro)
        ]

        # Luego inicializar Puntos, ahora con acceso a fantasmas
        self.puntos = Puntos(self.muro, OBJETOS, self.pacman, self.fantasmas)

        pyxel.run(self.update, self.draw)

    def update(self):
        self.pacman.mover()
        self.puntos.actualizar_modo_diablo()
        self.puntos.comer_puntos()   # Verificar si Pacman comió un punto
        self.puntos.generar_fruta()  # Generar frutas cada 30 segundos
        self.puntos.comer_fruta()    # Verificar si Pacman comió la fruta

    def draw(self):
        pyxel.cls(0)
        self.puntos.draw()
        self.muro.draw()
        self.pacman.draw()
        for fantasma in self.fantasmas:
            fantasma.draw()
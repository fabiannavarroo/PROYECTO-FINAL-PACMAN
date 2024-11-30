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

        # Iniciar el Mapa
        self.muro = Muro()

        # Iniciar el Pacman
        self.pacman = Pacman(208, 288, self.muro)

        # Iniciar los fantasmas
        self.fantasmas = [
            FantasmaRojo(200, 160, self.muro),
            FantasmaRosa(176, 190, self.muro),
            FantasmaAzul(192, 190, self.muro),
            FantasmaNaranja(208, 190, self.muro)
        ]

        # Iniciar los puntos
        self.puntos = Puntos(self.muro, OBJETOS, self.pacman, self.fantasmas)

        pyxel.run(self.update, self.draw)

    def update(self):
        # Actualiza el estado del juego
        if self.pacman.vidas > 0 and not self.pacman.en_muerte:
            self.pacman.mover()
            self.puntos.comer_puntos()  # Verificar si Pac-Man comió un punto
            self.puntos.comer_fruta()  # Verificar si Pac-Man comió una fruta

            # Actualizar estado de fantasmas
            for fantasma in self.fantasmas:
                fantasma.actualizar_estado()  # Actualizar su estado (asustado, normal)

            self.pacman.colision_fantasmas(self.fantasmas)  # Verificar colisiones con fantasmas
        elif self.pacman.en_muerte:
            self.pacman.animar_muerte()  # Ejecutar la animación de muerte
        else:
            self.reiniciar_tablero()  # Reiniciar tablero si se acaban las vidas

    def draw(self):
        # Dibuja todos los elementos del juego
        pyxel.cls(0)
        self.puntos.draw()
        self.muro.draw()
        self.pacman.draw()
        for fantasma in self.fantasmas:
            fantasma.draw()

    def reiniciar_tablero(self):
        # Reinicia las posiciones del juego
        self.pacman.reiniciar_posicion()
        for fantasma in self.fantasmas:
            fantasma.volver_a_trampa()
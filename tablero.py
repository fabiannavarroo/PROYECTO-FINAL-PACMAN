from muro import Muro
from pacman import Pacman
from fantasmas import *
from puntos import Puntos
from constantes import *
import pyxel

class Tablero:
    def __init__(self):
        pyxel.init(430, 415, title="Pacman", display_scale=1, fps=30)  # Tamaño de la Pantalla
        pyxel.load("assets/recursos.pyxres")

        # Iniciar el Mapa
        self.muro = Muro()
        # Iniciar el Pacman
        self.pacman = Pacman(208, 288, self.muro)  # Coordenadas iniciales del PacMan
        
        # Iniciar los fantasmas
        self.fantasmas = [
            FantasmaRojo(200, 160, self.muro),  # Coordenadas iniciales en la trampa
            FantasmaRosa(176, 190, self.muro),
            FantasmaAzul(192, 190, self.muro),
            FantasmaNaranja(208, 190, self.muro)
        ]

        # Iniciar los puntos
        self.puntos = Puntos(self.muro, OBJETOS, self.pacman, self.fantasmas) 

        pyxel.run(self.update, self.draw)

    def update(self):
        if self.pacman.vidas>0:
            self.pacman.mover()
            self.puntos.comer_puntos()   # Verificar si Pacman comio un punto
            self.puntos.generar_fruta()  # Generar frutas cada 30 segundos
            self.puntos.comer_fruta()    # Verificar si Pacman comio la fruta
            for fantasma in self.fantasmas:
                fantasma.trampa()
                fantasma.actualizar_estado()
            self.pacman.colision_fantasmas(self.fantasmas)
        else:
            # Mostrar Game Over
            self.pacman.game_over()

    def draw(self):
        pyxel.cls(0)
        self.puntos.draw()
        self.muro.draw()
        self.pacman.draw()
        for fantasma in self.fantasmas:
            fantasma.draw()
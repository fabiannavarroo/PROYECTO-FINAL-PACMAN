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
        if self.pacman.vidas > 0 and not self.pacman.en_muerte: # En caso de que el pacman tenga vidas y no este en la animacion de muerte
            self.pacman.mover()
            self.puntos.comer_puntos()   # Verificar si Pacman comio un punto
            self.puntos.generar_fruta()  # Generar frutas cada 30 segundos
            self.puntos.comer_fruta()    # Verificar si Pacman comio la fruta
            for fantasma in self.fantasmas:
                fantasma.mover() # Va actulizando si los fantamas se encuentran en la trampa
                fantasma.actualizar_estado() # Verifica si los fantasmas estas asustados o normal
            self.pacman.colision_fantasmas(self.fantasmas)  # Verifica la colision de pacman con los fantasmas

        elif self.pacman.en_muerte: # Si el pacman se encuentra en una animación de muerte
            self.pacman.animar_muerte()

        else: # Cuando el Pacman haya muerto y no esta en una animacion
            self.pacman.game_over()

    def draw(self):
        pyxel.cls(0)
        self.puntos.draw()
        self.muro.draw()
        self.pacman.draw()
        for fantasma in self.fantasmas:
            fantasma.draw()
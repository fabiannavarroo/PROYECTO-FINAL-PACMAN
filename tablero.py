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

        # Inicializar elementos del juego
        self.muro = Muro()
        self.pacman = Pacman(208, 288, self.muro)
        self.fantasmas = [
            FantasmaRojo(200, 160, self.muro),
            FantasmaRosa(176, 190, self.muro),
            FantasmaAzul(192, 190, self.muro),
            FantasmaNaranja(208, 190, self.muro)
        ]
        self.puntos = Puntos(self.muro, OBJETOS, self.pacman, self.fantasmas)

        # Iniciar el bucle principal
        pyxel.run(self.update, self.draw)

    def update(self):
        # Actualizar estado del juego
        if self.pacman.vidas > 0:
            if self.pacman.en_muerte:
                self.pacman.animar_muerte()  # Ejecutar animación de muerte
            else:
                self.pacman.mover()
                self.puntos.comer_puntos()
                self.puntos.comer_fruta()
                for fantasma in self.fantasmas:
                    fantasma.actualizar_estado()
                self.pacman.colision_fantasmas(self.fantasmas)
        else:
            self.mostrar_game_over()  # Mostrar Game Over si se acaban las vidas

    def draw(self):
        # Dibujar todos los elementos del juego
        pyxel.cls(0)
        self.muro.draw()
        self.puntos.draw()
        self.pacman.draw()
        for fantasma in self.fantasmas:
            fantasma.draw()

    def reiniciar_tablero(self):
        # Reiniciar posiciones de todos los elementos
        self.pacman.reiniciar_posicion()
        self.pacman.en_muerte = False
        self.pacman.animacion_frame = 0
        for fantasma in self.fantasmas:
            fantasma.volver_a_trampa()

    def mostrar_game_over(self):
        # Mostrar Game Over en el mapa
        self.pacman.game_over()
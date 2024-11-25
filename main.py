

from mapa import Mapa
from pacman import Pacman
from fantasmas import FantasmaRojo, FantasmaRosa, FantasmaAzul, FantasmaNaranja
import pyxel

class App:
    def __init__(self):
        # Inicializa Pyxel
        pyxel.init(224, 248)  # Tamaño de la ventana
        pyxel.title = "Pacman"
        
        # Carga los recursos desde recursos.pyxres
        pyxel.load("assets/recursos.pyxres")

        # Inicializa los objetos
        self.mapa = Mapa()
        self.pacman = Pacman(112, 184)  # Coordenadas iniciales de Pacman
        self.fantasmas = [
            FantasmaRojo(0, 56),
            FantasmaRosa(0, 96),
            FantasmaAzul(0, 48),
            FantasmaNaranja(0, 80)
        ]

        # Inicia el bucle principal
        pyxel.run(self.update, self.draw)

    def update(self):
        # Actualiza los movimientos
        self.pacman.mover()
        for fantasma in self.fantasmas:
            fantasma.mover()

    def draw(self):
        pyxel.cls(0)  # Limpia la pantalla

        # Dibuja el mapa (página 1)
        self.mapa.draw()

        # Dibuja Pacman y los fantasmas (página 0)
        self.pacman.dibujar()
        for fantasma in self.fantasmas:
            fantasma.dibujar()

# Ejecuta la aplicación
if __name__ == "__main__":
    App()
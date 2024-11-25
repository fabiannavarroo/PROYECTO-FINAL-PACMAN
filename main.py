from mapa import Mapa
import pyxel

class App:
    def __init__(self):
        # Inicializa Pyxel con el tamaño de la ventana
        pyxel.init(224, 248)  # Dimensiones basadas en tu matriz del mapa (28x31 celdas de 8px)
        # Establece el título de la ventana
        pyxel.title = "Pacman"
        # Carga los recursos del archivo .pyxres
        pyxel.load("assets/map.pyxres")
        # Inicializa la clase del mapa
        self.mapa = Mapa()
        # Ejecuta el bucle principal
        pyxel.run(self.update, self.draw)

    def update(self):
        # Aquí podrías manejar eventos de teclado u otras actualizaciones
        pass

    def draw(self):
        # Limpia la pantalla con el color de fondo
        pyxel.cls(0)
        # Dibuja el mapa
        self.mapa.draw()

# Inicia la aplicación
App()
from muro import Muro
from pacman import Pacman
from fantasmas import *
from puntos import Puntos
from constantes import *
import pyxel

class Tablero:
    def __init__(self):
        # Inicializar la ventana del juego con Pyxel
        pyxel.init(430, 415, title="Pacman", display_scale=1, fps=30)  # Crear la pantalla
        pyxel.load("assets/recursos.pyxres")  # Cargar recursos gráficos

        # Inicializar elementos del juego
        self.muro = Muro()  # Mapa del juego
        self.pacman = Pacman(208, 288, self.muro)  # Pacman y su posición inicial
        self.fantasmas = [  # Lista de fantasmas con sus posiciones iniciales
            FantasmaRojo(200, 160, self.muro),
            FantasmaRosa(176, 190, self.muro),
            FantasmaAzul(192, 190, self.muro),
            FantasmaNaranja(208, 190, self.muro),
        ]
        self.puntos = Puntos(self.muro, OBJETOS, self.pacman, self.fantasmas)  # Controlador de puntos y frutas

        # Iniciar el bucle principal del juego
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.pacman.vidas > 0:  # Mientras Pacman tenga vidas
            if self.pacman.en_muerte:
                # Ejecutar animación de muerte
                self.pacman.animar_muerte(self.fantasmas)
            else:
                # Actualizar elementos del juego
                self.pacman.mover()  # Mover Pacman
                self.puntos.comer_puntos()  # Detectar puntos comidos
                self.puntos.comer_fruta()  # Detectar frutas comidas
                self.puntos.generar_fruta()  # Generar frutas cada 30s
                for fantasma in self.fantasmas:
                    fantasma.actualizar_estado()  # Actualizar estado de los fantasmas
                self.pacman.colision_fantasmas(self.fantasmas, self.puntos)  # Colisiones con fantasmas


    
    def draw(self):
        pyxel.cls(0)  # Limpiar pantalla
        if self.pacman.vidas > 0:
            self.muro.draw()  # Dibujar el mapa
            self.puntos.draw()  # Dibujar puntos, frutas y puntuación
            self.pacman.ver_vidas(10, 10)  # Ver las vidas restantes
            if not self.pacman.en_muerte:  # Dibujar personajes si no está en animación de muerte
                self.pacman.draw(self.fantasmas)  # Dibujar Pacman
                for fantasma in self.fantasmas:
                    fantasma.draw()  # Dibujar fantasmas
            else:
                self.pacman.draw(self.fantasmas)  # Dibujar solo Pacman durante la animación de muerte
        if self.puntos.victoria:
            pyxel.text(10,12,"Has ganado",8)
        else:
            # Limpiar pantalla si las vidas llegan a 0 y muestra solo el mapa
            pyxel.cls(0)
            self.muro.draw()
            self.muro.fin()

    def reiniciar_tablero(self):
        # Reinicia las posiciones iniciales de los personajes y termina la animación de muerte.
        self.pacman.reiniciar_posicion()  # Reiniciar posición de Pacman
        self.pacman.en_muerte = False  # Finalizar estado de muerte
        self.pacman.animacion_frame = 0  # Reiniciar animación de muerte
        for fantasma in self.fantasmas:
            fantasma.volver_a_posicion_inicial()  # Reiniciar posición de los fantasmas
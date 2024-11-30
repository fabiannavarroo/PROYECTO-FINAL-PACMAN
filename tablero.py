from muro import Muro
from pacman import Pacman
from fantasmas import *
from puntos import Puntos
from constantes import *
import pyxel
import time

class Tablero:
    def __init__(self):
        
        pyxel.init(430, 415, title="Pacman", display_scale=1, fps=30)  # Crear la pantalla
        pyxel.load("assets/recursos.pyxres")  # Cargar recursos gráficos

        
        self.muro = Muro()  # Mapa del juego
        self.pacman = Pacman(208, 288, self.muro)  # Pacman y su posición inicial
        self.fantasmas = [  # Lista de fantasmas con sus posiciones iniciales
            FantasmaRojo(200, 160, self.muro),
            FantasmaRosa(176, 190, self.muro),
            FantasmaAzul(192, 190, self.muro),
            FantasmaNaranja(208, 190, self.muro),
        ]
        self.puntos = Puntos(self.muro, OBJETOS, self.pacman, self.fantasmas)  # Controlador de puntos y frutas

        # Mostrar "Game Over"
        self.game_over_mostrado = False

        # Temporizador para reinicio después de animación de muerte
        self.reiniciar_en = None

        # Iniciar el bucle principal del juego
        pyxel.run(self.update, self.draw)

    def update(self):
        #Actualizar el estado del juego en cada frame.
        if self.pacman.vidas > 0:  # Mientras Pacman tenga vidas
            if self.pacman.en_muerte:
                # Ejecutar animación de muerte
                self.pacman.animar_muerte(self.fantasmas)
                # Manejar temporizador para reiniciar tras la animación
                if not self.pacman.en_muerte and self.reiniciar_en is None:
                    self.reiniciar_en = time.time() + 2  # Esperar 2 segundos para reiniciar
                elif self.reiniciar_en and time.time() >= self.reiniciar_en:
                    self.reiniciar_tablero()  # Reiniciar posiciones del tablero
                    self.reiniciar_en = None
            else:
                # Actualizar elementos 
                self.pacman.mover()  # Mover Pacman
                self.puntos.comer_puntos()  # Detectar  puntos comidos
                self.puntos.comer_fruta()  # Detectar  frutas comidas
                self.puntos.generar_fruta()  # Generar frutas periódicamente
                for fantasma in self.fantasmas:
                    fantasma.actualizar_estado()  # Actualizar estado de los fantasmas
                self.pacman.colision_fantasmas(self.fantasmas)  # Manejar colisiones con fantasmas
        else:
            self.mostrar_game_over()  # Mostrar "Game Over" si se acaban las vidas

    def draw(self):
        Dibujar todos los elementos del juego.
        pyxel.cls(0)  # Limpiar pantalla
        if self.pacman.vidas > 0:
            self.muro.draw()  # Dibujar el mapa
            self.puntos.draw()  # Dibujar puntos, frutas y puntuación
            if not self.pacman.en_muerte:  # Ocultar fantasmas durante animación de muerte
                self.pacman.draw(self.fantasmas)  # Dibujar Pacman
                for fantasma in self.fantasmas:
                    fantasma.draw()  # Dibujar fantasmas
        elif self.game_over_mostrado:
            self.muro.draw()  # Mostrar solo el mapa limpio con "GAME OVER"

    def reiniciar_tablero(self):
        Reiniciar posiciones de todos los elementos del juego.
        self.pacman.reiniciar_posicion()  # Reiniciar posición de Pacman
        self.pacman.en_muerte = False  # Finalizar estado de muerte
        self.pacman.animacion_frame = 0  # Reiniciar animación de muerte
        for fantasma in self.fantasmas:
            fantasma.volver_a_posicion_inicial()  # Reiniciar posición de los fantasmas

    def limpiar_tablero(self):
        Eliminar todos los puntos y fantasmas del tablero.
        for y in range(len(self.muro.mapa)):
            for x in range(len(self.muro.mapa[y])):
                if self.muro.mapa[y][x] not in [MUROS, TEXTO]:  # Mantener muros y texto
                    self.muro.mapa[y][x] = -1  # Celda vacía

    def mostrar_game_over(self):
        Mostrar el mensaje de 'Game Over' en el mapa.
        if not self.game_over_mostrado:
            self.limpiar_tablero()  # Limpiar puntos y fantasmas del mapa
            self.muro.mapa[12][13] = 71  # Dibujar "GAME OVER" en la posición indicada
            self.game_over_mostrado = True
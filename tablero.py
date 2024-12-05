from pacman import Pacman
from fantasmas import *
from puntos import Puntos
from bloque import Bloque
from constantes import *
import pyxel


class Tablero:
    def __init__(self):
        # Inicializar la ventana del juego con Pyxel
        pyxel.init(400, 400, title="Pacman", fps=30)  # Crear la pantalla
        pyxel.load("assets/recursos.pyxres")  # Cargar recursos gráficos

        # Inicializar elementos del juego
        self.bloque = Bloque()  # Mapa del juego
        self.pacman = Pacman(192, 304, self.bloque)  # Pacman y su posición inicial
        self.fantasmas = [  # Lista de fantasmas con sus posiciones iniciales
            FantasmaRojo(196, 176),
            FantasmaRosa(181, 208),
            FantasmaAzul(203, 208),
            FantasmaNaranja(226, 208),
        ]
        self.puntos = Puntos(OBJETOS, self.pacman, self.fantasmas, self.bloque)  # Puntos y frutas

        # Variables de estado
        self.mostrar_ready = True  # Indica si se muestra el mensaje READY!
        self.contador_ready = 90  # Duración del mensaje READY!

        # Iniciar el bucle principal del juego
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.pacman.vidas > 0:  # Mientras Pacman tenga vidas
            if self.contador_ready > 0:
                self.contador_ready -= 1 
                if self.contador_ready == 0:
                    self.mostrar_ready = False  # Ocultar READY! después de 3 segundos

            if not self.pacman.en_muerte:
                # Actualizar elementos del juego
                self.pacman.mover()  # Mover Pacman
                self.puntos.comer_puntos()  # Detectar puntos comidos
                self.puntos.comer_fruta()  # Detectar frutas comidas
                self.puntos.generar_fruta()  # Generar frutas cada 30s
                for fantasma in self.fantasmas:
                    fantasma.actualizar_estado()  # Actualizar estado de los fantasmas
                self.pacman.colision_fantasmas(self.fantasmas, self.puntos)  # Colisiones con fantasmas
            else:
                # Ejecutar animación de muerte
                self.pacman.animar_muerte(self.fantasmas)
                if not self.pacman.en_muerte:  # Cuando termina la animación de muerte
                    self.reiniciar_tablero()

    def draw(self):
        pyxel.cls(0)  # Limpiar pantalla

        if self.pacman.vidas > 0:
            # Dibujar todos los elementos del juego
            self.bloque.draw()  # Dibujar el mapa
            self.puntos.draw()  # Dibujar puntos, frutas y puntuación
            self.pacman.ver_vidas(10, 10)  # Mostrar vidas restantes
            self.pacman.draw(self.fantasmas)  # Dibujar Pac-Man
            for fantasma in self.fantasmas:
                fantasma.draw()  # Dibujar fantasmas

            # Dibujar READY! si está activo
            if self.mostrar_ready:
                self.dibujar_ready()
        else:
            # Mostrar GAME OVER si no hay vidas
            pyxel.cls(0)
            self.bloque.draw()
            self.fin()

    def dibujar_ready(self):
        # Dibuja el mensaje READY! 
        if pyxel.frame_count % 13 == 0:
            sprite = TEXTO["READY!"]
            sprite_x, sprite_y = sprite["Coordenadas"]
            sprite_w, sprite_h = sprite["Tamaño"]
            pos_x = 180
            pos_y = 245
            pyxel.blt(pos_x, pos_y, 0, sprite_x, sprite_y, sprite_w, sprite_h, colkey=0)

    def fin(self):
        # Dibujar Game Over
        sprite = TEXTO["GAME OVER"]
        sprite_x, sprite_y = sprite["Coordenadas"]
        sprite_w, sprite_h = sprite["Tamaño"]
        pos_x = 185
        pos_y = 208
        pyxel.blt(pos_x, pos_y, 0, sprite_x, sprite_y, sprite_w, sprite_h, colkey=0)

    def reiniciar_tablero(self):
        # Reinicia las posiciones iniciales de los personajes y termina la animación de muerte.
        self.mostrar_ready = True  # Volver a mostrar READY!
        self.contador_ready = 90  # Restablecer duración del mensaje READY!
        self.pacman.reiniciar_posiciones(self.fantasmas)  # Reiniciar posición de Pacman
        self.pacman.en_muerte = False  # Finalizar estado de muerte
        self.pacman.animacion_frame = 0  # Reiniciar animación de muerte
        for fantasma in self.fantasmas:
            fantasma.volver_a_posicion_inicial()  # Reiniciar posición de los fantasmas


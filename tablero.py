from pacman import Pacman
from fantasmas import *
from puntos import Puntos
from bloque import Bloque
from constantes import *
import time
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
            FantasmaRojo(80, 176, self.pacman, self.bloque),
            FantasmaRosa(181, 208, self.pacman, self.bloque),
            FantasmaAzul(203, 208, self.pacman, self.bloque),
            FantasmaNaranja(225, 208, self.pacman, self.bloque),
        ]
        self.puntos = Puntos(OBJETOS, self.pacman, self.fantasmas, self.bloque)  # Puntos y frutas

        # Controlar el mensaje READY!
        self.mostrar_ready = True  # Indica si se muestra el mensaje READY!
        self.contador_ready = 0

        # Controlar el mensaje GAME OVER
        self.contador_game_over = 0
        self.mostrar_fin = False

        # Controlar la victoria
        self.victoria = False

        # Iniciar el bucle principal del juego
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.pacman.vidas > 0:  # Mientras Pacman tenga vidas
            if self.contador_ready < 90:
                self.contador_ready += 1 
                if self.contador_ready == 90:
                    self.mostrar_ready = False  # Ocultar READY! después de 3 segundos

            if not self.pacman.en_muerte:
                # Actualizar elementos del juego
                self.pacman.mover()  # Mover Pacman
                self.puntos.comer_puntos()  # Detectar puntos comidos
                self.puntos.comer_fruta()  # Detectar frutas comidas
                self.puntos.generar_fruta()  # Generar frutas cada 30s
                
                tiempo_actual = time.time()
                for num, fantasma in enumerate(self.fantasmas):
                    if isinstance(fantasma, FantasmaRojo):
                        # Fantasma rojo se mueve desde el principio
                        fantasma.mover()
                    elif fantasma.en_trampa:
                        # Salida escalonada de fantasmas de la trampa
                        if tiempo_actual - fantasma.tiempo_trampa >= num * 2:
                            fantasma.salir_de_trampa()
                    else:
                        # Movimiento normal de los fantasmas fuera de la trampa
                        fantasma.mover()
                    fantasma.actualizar_estado()  # Actualizar estado de los fantasmas

                self.pacman.colision_fantasmas(self.fantasmas, self.puntos)  # Colisiones con fantasmas

                # Comprobar si no quedan puntos ni regalos y sino quedan pues subimos de nivel
                if self.puntos.comprobar_puntos_restantes():
                    if self.bloque.nivel + 1 in self.bloque.mapas:
                        self.bloque.nivel += 1 # Subir de nivel
                        self.bloque.cargar_mapa() # Cargar el mapa del nuevo nivel
                        self.puntos.reiniciar_puntos() # Reiniciar los puntos
                        self.reiniciar_tablero() # Reiniciar el tablero
                    else:
                        self.victoria = True
                        
            else:
                # Ejecutar animación de muerte
                self.pacman.animar_muerte(self.fantasmas)
                if not self.pacman.en_muerte:  # Cuando termina la animación de muerte
                    self.reiniciar_tablero()
                
        else:
            if not self.mostrar_fin:
                self.mostrar_fin = True
                self.contador_game_over = 0  # Reiniciar el contador al inicio
            self.contador_game_over += 1
        

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
                self.animar_ready()
            
            # Dibujar la victoria
            if self.victoria:
                pyxel.cls(0)
                self.bloque.draw()
        else:
            # Mostrar GAME OVER si no hay vidas
            pyxel.cls(0)
            self.bloque.draw()
            self.pacman.animar_muerte(self.fantasmas)
            self.animar_fin()

    def dibujar_ready(self):
        # Dibuja el mensaje READY! 
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
        

    def reiniciar_fantasmas(self):
        for fantasma in self.fantasmas:
            fantasma.volver_a_posicion_inicial()
            fantasma.siguiente_celda = None  # Limpiar la ruta almacenada
            fantasma.tiempo_trampa = time.time()  # Reiniciar temporizador

    def reiniciar_tablero(self):
        # Reinicia las posiciones iniciales de los personajes y termina la animación de muerte.
        self.mostrar_ready = True  # Volver a mostrar READY!
        self.contador_ready = 0  # Restablecer duración del mensaje READY!
        self.bloque.cargar_mapa()  # Recargar el mapa del nivel actual
        self.pacman.reiniciar_posiciones(self.fantasmas)  # Reiniciar posición de Pacman
        self.pacman.en_muerte = False  # Finalizar estado de muerte
        self.pacman.animacion_frame = 0  # Reiniciar animación de muerte
        self.reiniciar_fantasmas()  # Reiniciar posición de los fantasmas

    def animar_ready(self):
        # Animación del mensaje READY!
        if self.contador_ready < 90:  # Duración de la animación
            if (self.contador_ready // 10) % 2 == 0:
                self.dibujar_ready()  # Mostrar el texto "READY!"
            else:
                pyxel.blt(180, 245, 2, 0, 0, 0, 0, colkey=0) # dibujar un vacio
        else:
            # Mantener el texto visible 
            pyxel.blt(180, 245, 2, 0, 0, 0, 0, colkey=0)
        

    def animar_fin(self):
        # Animación de GAME OVER
        if self.contador_game_over < 70:  # Duración de la animación
            if (self.contador_game_over // 10) % 2 == 0:
                self.fin()  # Mostrar el texto "GAME OVER"
            else:
                pyxel.blt(180, 245, 2, 0, 0, 0, 0, colkey=0) # dibujar un vacio
        else:
            # Mantener el texto visible 
            self.fin()


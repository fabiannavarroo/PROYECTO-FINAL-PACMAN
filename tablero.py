from pacman import Pacman
from fantasmas import *
from puntos import Puntos
from bloque import Bloque
from constantes import *
import pyxel


class Tablero:
    def __init__(self):
        # Inicializar la ventana del juego
        pyxel.init(400, 400, title="Pacman", fps=30)
        # Cargar los recursos del archivo .pyxres
        pyxel.load("assets/recursos.pyxres")
        #menu pincipal del juego
        self.estado_juego = "menu"

        # Iniciar la música para el mapa 1
        pyxel.playm(0, 0, True)

        # Crear el objeto bloque, que representa el mapa
        self.bloque = Bloque()  
        # Crear el objeto Pacman, en la posición 192, 304
        self.pacman = Pacman(192, 304)
        # Crear la lista de fantasmas con sus posiciones iniciales
        self.fantasmas = [
            FantasmaRojo(160, 208),
            FantasmaRosa(180, 208),
            FantasmaAzul(202, 208),
            FantasmaNaranja(224, 208),
        ]
        # Crear el objeto Puntos, que sera el encargado los puntos, frutas y regalos
        self.puntos = Puntos(OBJETOS)

        # Generar puntos por todo el mapa
        self.puntos.generar_puntos(self.bloque)

        # Iniciar el bucle principal de Pyxel
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Z):
            self.bloque.nivel += 1
            self.reiniciar_tablero()
            self.puntos.reiniciar_puntos(self.bloque)
            

        if pyxel.btnp(pyxel.KEY_X):
            self.bloque.victoria = True

        if pyxel.btnp(pyxel.KEY_C):
            self.pacman.vidas = 0

            

        if self.estado_juego == "menu":
            if pyxel.btnp(pyxel.KEY_P):  # Modo normal
                self.estado_juego = "jugando"
                for fantasma in self.fantasmas:
                    fantasma.tiempo_trampa = time.time()
            elif pyxel.btnp(pyxel.KEY_N):  # Modo visión reducida
                self.estado_juego = "vision_reducida"
                for fantasma in self.fantasmas:
                    fantasma.tiempo_trampa = time.time()
            elif pyxel.btnp(pyxel.KEY_ESCAPE):  # Salir
                pyxel.quit()
        elif self.estado_juego == "jugando":
            self.modo_juego_update()
        elif self.estado_juego == "vision_reducida":
            self.modo_juego_update()
            
            

    def draw(self):
        if self.estado_juego == "menu":
            pyxel.cls(0)
            pyxel.bltm(10, -60, 0, 0, 360, 390, 150, colkey=0)
            pyxel.bltm(120, 50, 1, 0, 0, 120, 120, colkey=0)  # Dibuja lo fantsams y al pamcan
            pyxel.blt(155, 170, 0, 88, 160, 56, 8, colkey=0)  # P: Jugar
            pyxel.blt(155, 190, 0, 88, 168, 150, 8, colkey=0)  # N: Vision reducida
            pyxel.blt(155, 210, 0, 88, 176, 100, 8, colkey=0)  # N: Vision reducida

        elif self.estado_juego == "jugando":
            self.modo_juego_normal_dibujo()

        elif self.estado_juego == "vision_reducida":
            self.modo_vision_reducida_dibujo()

    #--------------------------------------------------------------------REINICIO--------------------------------------------------------------------#

    def reiniciar_fantasmas(self):
        # Reiniciar fantasmas a su posición original después de una muerte o cambio de nivel
        for fantasma in self.fantasmas:
            fantasma.volver_a_posicion_inicial()
            fantasma.ultima_direccion = None
            fantasma.tiempo_trampa = time.time()

    def reiniciar_tablero(self):
        # Reinicia las condiciones iniciales después de la animación de muerte o al cambiar de nivel
        self.bloque.mostrar_ready = True
        self.bloque.contador_ready = 0
        self.bloque.cargar_mapa()
        self.reiniciar_posiciones()
        self.pacman.en_muerte = False
        self.pacman.animacion_frame = 0
        self.pacman.direccion_actual = PACMAN

    def reiniciar_posiciones(self):
        # Reiniciar las posiciones de Pac-Man y fantasmas a sus posiciones iniciales
        self.pacman.x, self.pacman.y = 192, 304
        self.reiniciar_fantasmas()
        self.pacman.reiniciando = False

    
    def reinicar_juego(self):
        # Reinicia las condiciones del tablero y los estados generales
        self.bloque.nivel = 1
        self.pacman.vidas = 3
        self.bloque.victoria = False
        self.bloque.contador_ready = 0
        self.bloque.contador_game_over = 0
        self.bloque.victoria_contador_corona = 0
        self.bloque.victoria_contador_texto = 0
        self.pacman.en_muerte = False
        self.pacman.animacion_frame = 0
        self.pacman.mostrar_puntos = False
        self.reiniciar_tablero()
        self.puntos.reiniciar_puntos(self.bloque)
        self.estado_juego = "menu"


    #--------------------------------------------------------------------ANIMACIONES--------------------------------------------------------------------#

    def animar_ready(self):
        # Animación del mensaje READY! durante los primeros segundos del nivel
        if self.bloque.contador_ready < 90:
            # Alternar el mensaje cada cierto tiempo para parpadear
            if (self.bloque.contador_ready // 10) % 2 == 0:
                self.dibujar_letras_mapa(180,240,"READY!")
            else:
                pyxel.blt(180, 245, 2, 0, 0, 0, 0, colkey=0)
        else:
            # Mantener un vacio después del tiempo
            pyxel.blt(180, 245, 2, 0, 0, 0, 0, colkey=0)

    def animar_fin(self):
        # Animación del mensaje GAME OVER cuando se acaban las vidas de Pac-Man
        pyxel.cls(0)

        if self.bloque.contador_game_over < 70:
            if (self.bloque.contador_game_over // 5) % 2 == 0:
                pass
            else:
                pyxel.bltm(pyxel.width/4,pyxel.height/4, 0, 0, 0, 200, 200)
                self.dibujar_letras_mapa(185,300,"GAME OVER")
                pyxel.text(155, 320, "PULSE R PARA REINICIAR", pyxel.COLOR_WHITE)
                pyxel.text(160, 340, "PULSE ESC PARA SALIR", pyxel.COLOR_RED)
        else:
            # Mantener el texto "GAME OVER" visible
            pyxel.bltm(pyxel.width/4,pyxel.height/4, 0, 0, 0, 200, 200)  # LAPIDA DE MUERTE
            self.dibujar_letras_mapa(185,300,"GAME OVER")

            pyxel.text(155, 320, "PULSE R PARA REINICIAR", pyxel.COLOR_WHITE)
            pyxel.text(160, 340, "PULSE ESC PARA SALIR", pyxel.COLOR_RED)


    def animar_win(self):
        pyxel.cls(0)
        if self.bloque.victoria_contador_texto <=10: 
            self.dibujar_letras_mapa(185,250,"VICTORIA_1")
            self.bloque.victoria_contador_texto += 1
        elif self.bloque.victoria_contador_texto <=20: 
            self.dibujar_letras_mapa(185,250,"VICTORIA_2")
            self.bloque.victoria_contador_texto += 1
        else:
            self.dibujar_letras_mapa(185,250,"VICTORIA_3")
            self.bloque.victoria_contador_texto += 1
        # Para que la animacion este en continuo funcionamiento
        if self.bloque.victoria_contador_texto == 40:
            self.bloque.victoria_contador_texto = 0 
        # Animacion de la corona 
        if self.bloque.victoria_contador_corona < 10:
            if pyxel.frame_count % 2 == 0:  
                pyxel.blt(pyxel.width/4,pyxel.height/4, 1, 16, 120, 208, 144, colkey=0)
                self.bloque.victoria_contador_corona += 1
                pyxel.text(155, 280, "PULSE R PARA REINICIAR", pyxel.COLOR_WHITE)
                pyxel.text(160, 300, "PULSE ESC PARA SALIR", pyxel.COLOR_RED)
            else: 
                pyxel.blt(0, 0, 2, 0, 0, 0, 0, colkey=0)
        else:
            pyxel.blt(pyxel.width/4,pyxel.height/4, 1, 16, 120, 208, 144, colkey=0)
            pyxel.text(155, 280, "PULSE R PARA REINICIAR", pyxel.COLOR_WHITE)
            pyxel.text(160, 300, "PULSE ESC PARA SALIR", pyxel.COLOR_RED)


    def animar_muerte(self):
        # Animación de la muerte de Pac-Man
        if self.pacman.animacion_frame < len(ANIMACION_MUERTE):
            sprite_x, sprite_y = ANIMACION_MUERTE[self.pacman.animacion_frame]
            pyxel.cls(0)
            self.bloque.draw()
            pyxel.blt(self.pacman.x, self.pacman.y, 0, sprite_x, sprite_y, 16, 16, colkey=0)
            
            # Cambiar de frame cada cierto número de frames
            if pyxel.frame_count % 5 == 0:
                self.pacman.animacion_frame += 1
        else:
            # Una vez terminada la animación, reiniciar el tablero o marcar el fin del juego
            if self.pacman.vidas > 0:
                self.reiniciar_tablero()
            else:
                self.animacion_muerte_finalizada = True
                self.pacman.en_muerte = False


#--------------------------------------------------------------------MUSICA--------------------------------------------------------------------#

    def actualizar_musica(self):
        # Variable para ver la música actual
        musica_actual = None

        # Determinar qué música debería sonar
        if self.bloque.victoria:
            musica_actual = 1  # Música de victoria
        elif self.pacman.en_muerte:
            musica_actual = 3  # Música de muerte de Pac-Man
        elif any(fantasma.asustado for fantasma in self.fantasmas):
            musica_actual = 2  # Música de fantasmas asustados
        elif self.bloque.nivel == 1:
            musica_actual = 0  # Música del mapa 1
        elif self.bloque.nivel == 2: # Música del mapa 2
            
            if self.bloque.elegir_cancion < 0.5:
                musica_actual = 5  
            else:
                musica_actual = 7
        elif self.bloque.nivel == 3:
            musica_actual = 4  # Música del mapa 3

        # Cambiar la música solo si es diferente a la actual
        if musica_actual is not None and musica_actual != self.bloque.musica_actual:
            pyxel.playm(musica_actual, 0, True)
            self.bloque.musica_actual = musica_actual

    #--------------------------------------------------------------------MAPA--------------------------------------------------------------------#

    def dibujar_letras_mapa(self, x, y, sprite):
        # Dibuja textos como READY!, GAME OVER o HIGHSCORE, usando los datos en TEXTO
        sprite = TEXTO[sprite]
        pyxel.blt(x, y, 0, sprite["Coordenadas"][0], sprite["Coordenadas"][1], sprite["Tamaño"][0], sprite["Tamaño"][1], colkey=0)

#--------------------------------------------------------------------COLISION--------------------------------------------------------------------#

    def comprobar_colision_pacman_fantasmas(self):
        pacman_centro_x = self.pacman.x + 8  # Coordenada central de Pac-Man
        pacman_centro_y = self.pacman.y + 8
        colision_detectada = False  # Nos dicesi Pac-Man ha sido comido

        for fantasma in self.fantasmas:
            fantasma_centro_x = fantasma.x + 8  # Coordenada central del fantasma
            fantasma_centro_y = fantasma.y + 8

            # Comprobar si están lo suficientemente cerca
            if abs(pacman_centro_x - fantasma_centro_x) < 16 and abs(pacman_centro_y - fantasma_centro_y) < 16:
                if fantasma.asustado:
                    # Pac-Man come al fantasma
                    self.puntos.puntos += 200  # Incrementar puntos por comer al fantasma
                    fantasma.volver_a_posicion_inicial()  # Reiniciar al fantasma
                    self.pacman.mostrar_puntos = True
                    self.pacman.texto_tiempo_inicio = time.time()
                    self.pacman.posicion_fantasma_comido_x = self.pacman.x
                    self.pacman.posicion_fantasma_comido_y =  self.pacman.y
                else:
                    # Fantasma come a Pac-Man
                    colision_detectada = True # Hay colsion

        # Si hubo colisión y los fantasmas no estan asustado, Pac-Man pierde una vida
        if colision_detectada:
            self.pacman.perder_vida()
            self.pacman.en_muerte = True

    #--------------------------------------------------------------------MODOS--------------------------------------------------------------------#

    def modo_juego_normal_dibujo(self):
        pyxel.cls(0)  # Limpiar la pantalla
        self.dibujar_letras_mapa(120,16,"HIGHSCORE")
        self.puntos.ver_puntuacion(195,16)
        if self.pacman.vidas > 0:
            # Mientras Pac-Man tenga vidas, dibujar el mapa y los objetos
            self.bloque.draw()  # Dibujar el mapa
            if self.pacman.en_muerte:
                # Si Pac-Man está en animación de muerte, dibujar solo la animación
                self.animar_muerte()
            else:
                # Dibujar puntos, frutas, puntuación
                self.puntos.draw()
                # Dibujar las vidas de Pac-Man
                self.pacman.ver_vidas(10, 10)
                # Dibujar a Pac-Man
                self.pacman.draw()
                # Dibujar los fantasmas
                for fantasma in self.fantasmas:
                    fantasma.draw()

                # Dibujar el mensaje READY!
                if self.bloque.mostrar_ready:
                    self.animar_ready()

                # Si Pac-Man ha comido un fantasma, mostrar los puntos que ganó
                if self.pacman.mostrar_puntos and time.time() - self.pacman.texto_tiempo_inicio < 1.5:
                    pyxel.text(self.pacman.posicion_fantasma_comido_x, self.pacman.posicion_fantasma_comido_y, "+200 puntos", pyxel.COLOR_RED)
                else:
                    self.pacman.mostrar_puntos = False
            # Si se ganó la partida, limpiar pantalla y dibuja la animacion de la victoria
            if self.bloque.victoria:
                self.animar_win()
                if pyxel.btnp(pyxel.KEY_R):
                    self.estado_juego = "menu"
                    self.reinicar_juego()
        else:
            # Si Pac-Man no tiene vidas, mostrar GAME OVER
            pyxel.cls(0)
            self.bloque.draw()
            self.animar_muerte()
            self.animar_fin()
            if pyxel.btnp(pyxel.KEY_R):
                self.estado_juego = "menu"
                self.reinicar_juego()

    def modo_juego_update(self):
        # Actualizar musica para las distintas situaciones
        self.actualizar_musica()

        if self.pacman.vidas > 0:
            # Mientras Pac-Man tenga vidas
            if self.bloque.contador_ready < 90:
                # Mostrar el mensaje READY! por un tiempo
                self.bloque.contador_ready += 1
                if self.bloque.contador_ready == 90:
                    self.bloque.mostrar_ready = False  # Ocultar READY! después de un tiempo

            if not self.pacman.en_muerte:
                # Actualizar el juego si Pac-Man no está en estado de muerte
                # Mover Pac-Man según la dirección del jugador
                self.pacman.movimineto_pacman(self.bloque)
                # Comprobar si Pac-Man come puntos
                self.puntos.comer_puntos(self.pacman.x, self.pacman.y, self.fantasmas)
                # Comprobar si Pac-Man come fruta
                self.puntos.comer_fruta(self.pacman.x, self.pacman.y)
                # Intentar generar una fruta cada cierto tiempo
                self.puntos.generar_fruta(self.bloque)
                # Comprobar colisiones entre fantasmas y Pac-Man
                self.comprobar_colision_pacman_fantasmas()

                # Actualizar cada fantasma
                for index, fantasma in enumerate(self.fantasmas):
                    # Actualizar el estado del fantasma
                    fantasma.actualizar_estado()
                    # Revisar si el fantasma está en la posición inicial
                    if fantasma.en_trampa:
                        # Comprobar si el fantasma está en modo asustado
                        if not fantasma.asustado:
                            # Esperar un tiempo antes de moverlo a la salida
                            tiempo_espera = (index + 1) * 2
                            if time.time() - fantasma.tiempo_trampa >= tiempo_espera:
                                fantasma.en_salida = True
                                fantasma.mover_a_salida()
                    else:
                        # Actualizar movimiento normal si no está en la trampa
                        fantasma.mover(self.bloque, self.pacman)

                # Comprobar si se han comido todos los puntos y regalos
                if self.puntos.comprobar_puntos_restantes():
                    # Si hay un siguiente nivel, pasar al siguiente
                    if self.bloque.nivel + 1 in self.bloque.mapas:
                        self.bloque.nivel += 1
                        self.reiniciar_tablero()
                    else:
                        # Si no hay más niveles, ganar el juego
                        self.bloque.victoria = True
                        
            else:
                # Si Pac-Man está en muerte, ejecutar la animación de muerte
                self.animar_muerte()

        else:
            # Pac-Man no tiene vidas
            if not self.pacman.animacion_muerte_finalizada:
                # Ejecutar la animación de muerte final de Pac-Man
                self.animar_muerte()
                if self.pacman.animacion_frame >= len(ANIMACION_MUERTE):
                    self.pacman.animacion_muerte_finalizada = True
            else:
                # Después de la animación de muerte final, esperar antes de mostrar GAME OVER fijo
                self.bloque.contador_game_over += 1

                
    def modo_vision_reducida_dibujo(self):
        pyxel.cls(0)  # Limpiar la pantalla
        radio_vision = 80  # Radio de visión

        if self.pacman.en_muerte:
            # Si Pac-Man está en animación de muerte, mostrar todo el mapa y la animación
            self.bloque.draw()  # Dibujar todo el mapa
            self.puntos.draw()  # Dibujar todos los puntos
            for fantasma in self.fantasmas:
                fantasma.draw()  # Dibujar todos los fantasmas
            self.pacman.draw()  # Dibujar Pac-Man
            self.animar_muerte()  # Ejecutar la animación de muerte
            return False  # No hacer nada más mientras se ejecuta la animación

        if self.bloque.victoria or self.pacman.vidas <= 0:
            # Si estamos en pantalla de victoria o Game Over, dibujar todo normalmente
            self.bloque.draw()  # Dibujar todo el mapa
            self.puntos.draw()  # Dibujar todos los puntos
            for fantasma in self.fantasmas:
                fantasma.draw()  # Dibujar todos los fantasmas
            self.pacman.draw()  # Dibujar Pac-Man

            if self.bloque.victoria:
                self.animar_win()
            else:
                self.animar_fin()

            # Interfaz de vidas y puntos
            self.dibujar_letras_mapa(120, 16, "HIGHSCORE")
            self.puntos.ver_puntuacion(195, 16)
            self.pacman.ver_vidas(10, 10)

            # Reinicio desde las pantallas finales
            if pyxel.btnp(pyxel.KEY_R):
                self.estado_juego = "menu"
                self.reinicar_juego()
            return  # No aplicar visión reducida en estas pantallas

        # Mientras Pac-Man tenga vidas y no esté en Game Over o Victoria
        self.bloque.draw()  # Dibujar el mapa completo

        # Dibujar puntos visibles
        self.puntos.draw()

        # Dibujar fantasmas dentro del radio
        for fantasma in self.fantasmas:
            if self.esta_dentro_radio(fantasma.x + 8, fantasma.y + 8, self.pacman.x + 8, self.pacman.y + 8, radio_vision):
                fantasma.draw()

        # Dibujar a Pac-Man
        self.pacman.draw()

        # Dibujar el mensaje READY!
        if self.bloque.mostrar_ready:
            self.animar_ready()

        # Si Pac-Man ha comido un fantasma, mostrar los puntos que ganó
        if self.pacman.mostrar_puntos and time.time() - self.pacman.texto_tiempo_inicio < 1.5:
            pyxel.text(self.pacman.posicion_fantasma_comido_x, self.pacman.posicion_fantasma_comido_y, "+200 puntos", pyxel.COLOR_RED)
        else:
            self.pacman.mostrar_puntos = False

        # Oscurecer el área fuera del radio de visión
        for x in range(pyxel.width):
            for y in range(pyxel.height):
                if not self.esta_dentro_radio(x, y, self.pacman.x + 8, self.pacman.y + 8, radio_vision):
                    pyxel.pset(x, y, 0)  # Pintar fuera del radio en negro

        # Interfaz de vidas y puntos
        self.dibujar_letras_mapa(120, 16, "HIGHSCORE")
        self.puntos.ver_puntuacion(195, 16)
        self.pacman.ver_vidas(10, 10)


    def esta_dentro_radio(self, x1, y1, x2, y2, radio):
        # Calcula si un punto está dentro del radio
        distancia = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        return distancia <= radio


    



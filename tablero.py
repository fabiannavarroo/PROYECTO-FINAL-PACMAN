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
        pyxel.playm(0,0,True)

        # Inicializar elementos del juego
        self.bloque = Bloque()  # Mapa del juego
        self.pacman = Pacman(192, 304)  # Pacman y su posición inicial
        self.fantasmas = [  # Lista de fantasmas con sus posiciones iniciales
            FantasmaRojo(196, 176),
            FantasmaRosa(181, 208),
            FantasmaAzul(203, 208),
            FantasmaNaranja(225, 208),
        ]
        self.puntos = Puntos(OBJETOS)  # Puntos y frutas

        # Generar los puntos en el mapa
        self.generar_puntos()

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
                self.movimineto_pacman()  # Mover Pacman
                self.comer_puntos()  # Detectar puntos comidos
                self.comer_fruta()  # Detectar frutas comidas
                self.generar_fruta()  # Generar frutas cada 30s
                
                tiempo_actual = time.time()
                for index, fantasma in enumerate(self.fantasmas):
                    if isinstance(fantasma, FantasmaRojo):
                        # Fantasma rojo se mueve normalmente desde el principio
                        fantasma.mover()
                    elif fantasma.en_trampa():
                        # Salida escalonada de fantasmas de la trampa
                        if tiempo_actual - fantasma.tiempo_trampa >= index * 2:
                            fantasma.salir_de_trampa()
                    else:
                        # Movimiento normal de los fantasmas fuera de la trampa
                        fantasma.mover()
                    fantasma.actualizar_estado()  # Actualizar estado de los fantasmas

                self.colision_fantasmas_con_pacman()  # Colisiones con fantasmas

                # Comprobar si no quedan puntos ni regalos y sino quedan pues subimos de nivel
                if self.comprobar_puntos_restantes():
                    if self.bloque.nivel + 1 in self.bloque.mapas:
                        self.bloque.nivel += 1 # Subir de nivel
                        self.bloque.cargar_mapa() # Cargar el mapa del nuevo nivel
                        self.reiniciar_puntos() # Reiniciar los puntos
                        self.reiniciar_tablero() # Reiniciar el tablero
                    else:
                        self.victoria = True
                        
            else:
                # Ejecutar animación de muerte
                self.animar_muerte()

        else:
            if not self.mostrar_fin:
                self.mostrar_fin = True
                self.contador_game_over = 0  # Reiniciar el contador al inicio
            self.contador_game_over += 1
        

    def draw(self):
        pyxel.cls(0)  # Limpiar pantalla
        self.dibujar_letras_mapa(120,16, "HIGHSCORE")
        self.puntos.ver_puntuacion(195,16)
        if self.pacman.vidas > 0:
            # Dibujar todos los elementos del juego
            self.bloque.draw()  # Dibujar el mapa
            if self.pacman.en_muerte:
                # Dibujar la animación de muerte
                self.animar_muerte()
            else:
                self.puntos.draw()  # Dibujar puntos, frutas y puntuación
                self.pacman.ver_vidas(10, 10)  # Mostrar vidas restantes
                self.pacman.draw()  # Dibujar Pac-Man
                for fantasma in self.fantasmas:
                    fantasma.draw()  # Dibujar fantasmas
                
                 # Dibujar READY! si está activo
                if self.mostrar_ready:
                    self.animar_ready()

                # Mostrar puntos cuando come fantasmas
                if self.pacman.mostrar_puntos and time.time() - self.pacman.texto_tiempo_inicio < 1.5:  # Mostrar por 1.5 segundos
                    pyxel.text(self.pacman.posicion_fantasma_comido_x, self.pacman.posicion_fantasma_comido_y, "+200 puntos", pyxel.COLOR_RED)
                else:
                    self.pacman.mostrar_puntos = False

            # Dibujar la victoria
            if self.victoria:
                pyxel.cls(0)
                self.bloque.draw()
        else:
            # Mostrar GAME OVER si no hay vidas
            pyxel.cls(0)
            self.bloque.draw()
            self.animar_muerte()
            self.animar_fin()


######################################################################

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
        self.reiniciar_posiciones()  # Reiniciar posición de Pacman y Fantasmas
        self.pacman.en_muerte = False  # Finalizar estado de muerte
        self.pacman.animacion_frame = 0  # Reiniciar animación de muerte




######################################################################
    def animar_ready(self):
        # Animación del mensaje READY!
        if self.contador_ready < 90:  # Duración de la animación
            if (self.contador_ready // 10) % 2 == 0:
                self.dibujar_letras_mapa(180,240,"READY!")  # Mostrar el texto "READY!"
            else:
                pyxel.blt(180, 245, 2, 0, 0, 0, 0, colkey=0) # dibujar un vacio
        else:
            # Mantener el texto visible 
            pyxel.blt(180, 245, 2, 0, 0, 0, 0, colkey=0)
        

    def animar_fin(self):
        # Animación de GAME OVER
        if self.contador_game_over < 70:  # Duración de la animación
            if (self.contador_game_over // 10) % 2 == 0:
                self.dibujar_letras_mapa(185,208,"GAME OVER")  # Mostrar el texto "GAME OVER"
            else:
                pyxel.blt(180, 245, 2, 0, 0, 0, 0, colkey=0) # dibujar un vacio
        else:
            # Mantener el texto visible 
            self.dibujar_letras_mapa(185,208,"GAME OVER")

########################################################################
##Muros

    def dibujar_letras_mapa(self, x, y, sprite):
        # Dibuja las letras en el mapa
        sprite = TEXTO[sprite]
        pyxel.blt(x, y, 0, sprite["Coordenadas"][0], sprite["Coordenadas"][1], sprite["Tamaño"][0], sprite["Tamaño"][1], colkey=0)


######################################################################
##PUntos
    def generar_puntos(self):
        # Poner los puntos en el mapa
        for x in range(0, pyxel.width, 16):
            for y in range(0, pyxel.height, 16):
                if not self.esta_en_zona_prohibida(x, y) and (x, y) not in self.puntos.regalos:
                    self.puntos.lista_puntos.append((x, y, "BASTON"))


    def esta_en_zona_prohibida(self, x, y):
        # Verificar si está en una zona prohibida
        for lugar in self.puntos.zonas_prohibidas[self.bloque.nivel]:
            x1, y1, x2, y2 = lugar
            if x1 <= x <= x2 and y1 <= y <= y2:  
                return True

        # Verificar si hay un muro
        if self.bloque.colision(x, y):
            return True
        return False
    

    def encontrar_celdas_vacias(self):
    # Encuentra celdas vacías donde no haya puntos, frutas, regalos ni muros
        celdas_vacias = [
            (x, y) 
            for x in range(0, pyxel.width, 16) 
            for y in range(0, pyxel.height, 16) 
            if not self.esta_en_zona_prohibida(x, y) and 
            (x, y) not in [(p[0], p[1]) for p in self.puntos.lista_puntos] and 
            (x, y) != self.puntos.posicion_fruta and 
            (x, y) not in self.puntos.regalos
        ]
        return celdas_vacias



    def generar_fruta(self):
        # Genera una fruta en una celda vacía
        if time.time() - self.puntos.ultimo_tiempo_fruta < 30:
            return False  # No generar una nueva fruta si no han pasado 30 segundos

        # Seleccionar un objeto aleatorio sin regalos ni bastones
        objetos_dispo = ["CEREZA", "FRESA", "NARANJA", "MANZANA", "MELON", "PARAGUAS", "CAMPANA", "LLAVE"]
        self.puntos.fruta_actual = random.choice(objetos_dispo)

        # Elegir una posición aleatoria en celdas vacías
        celdas_vacias = self.encontrar_celdas_vacias()
        if celdas_vacias:  # Si existen posiciones vacías, genera la fruta y permite que se ejecute la animación
            self.puntos.posicion_fruta = random.choice(celdas_vacias)
            self.puntos.animacion_activa = True  # Activa la animación
            self.puntos.animacion_contador = 0  # Reinicia el contador de la animación
        else:
            self.puntos.posicion_fruta = None  # No hay espacio libre para generar una fruta

        # Actualiza el tiempo de la última fruta generada
        self.puntos.ultimo_tiempo_fruta = time.time()


    def comer_puntos(self):
        # Detectar si Pac-Man come puntos
        puntos_sin_comer = []
        for x, y, tipo in self.puntos.lista_puntos:
            if self.detectar_colision_puntos(self.pacman.x, self.pacman.y, x, y):
                # Incrementar puntos según el tipo
                self.puntos.puntos += OBJETOS[tipo]["Puntos"]
            else:
                puntos_sin_comer.append((x, y, tipo))
        self.puntos.lista_puntos = puntos_sin_comer

        # Detectar si Pac-Man come un regalo
        regalos_sin_comer = []
        for x, y in self.puntos.regalos:
            if self.detectar_colision_puntos(self.pacman.x, self.pacman.y, x, y):
                # Activar estado asustado para los fantasmas
                for fantasma in self.fantasmas:
                    fantasma.activar_asustado()
                self.puntos.puntos += OBJETOS["REGALO"]["Puntos"]  # Incrementar los puntos por el regalo
            else:
                regalos_sin_comer.append((x, y))
        self.puntos.regalos = regalos_sin_comer

    def detectar_colision_puntos(self, pacman_x, pacman_y, punto_x, punto_y):
        # Detecta si Pac-Man ha comido un punto
        return abs(pacman_x - punto_x) < 10 and abs(pacman_y - punto_y) < 10


    def comer_fruta(self):
        # Detecta si Pac-Man come la fruta actual.
        if self.puntos.posicion_fruta and self.detectar_colision_puntos(self.pacman.x, self.pacman.y, self.puntos.posicion_fruta[0], self.puntos.posicion_fruta[1]):
            self.puntos.puntos += OBJETOS[self.puntos.fruta_actual]["Puntos"]  # Incrementa los puntos según la fruta
            self.puntos.posicion_fruta = None  # Elimina la fruta actual
            self.puntos.fruta_actual = None


    def comprobar_puntos_restantes(self):
        # Verifica si no quedan puntos ni regalos
        if len(self.puntos.lista_puntos) == 0 and len(self.puntos.regalos) == 0:
            return True
        return False


    def reiniciar_puntos(self):
        # Reinica los puntos
        self.puntos.regalos = [(16, 304), (368, 304), (16, 80),(368, 80)] # Coordenadas de los regalos
        self.puntos.lista_puntos = [] # Lista de puntos generados
        self.generar_puntos()
        self.puntos.ultimo_tiempo_fruta = time.time()  # Tiempo de la última fruta generada
        self.puntos.fruta_actual = None  # Información de la fruta actual
        self.puntos.posicion_fruta = None  # Posición actual de la fruta
        self.puntos.animacion_activa = False  # Indica si hay animación activa
        self.puntos.animacion_contador = 0



###############################################################################################################################
                #Fantasmas


    def colision_fantsmas(self, x, y):
        # Verifica si hay colisión, quitando la región de la puerta de salida
        puerta_x, puerta_y = PUERTA_SALIDA
        sprite_tamaño = self.bloque.celda_tamaño

        # Quita la región de la puerta de salida
        if puerta_x <= x < puerta_x + sprite_tamaño and puerta_y <= y < puerta_y + sprite_tamaño:
            return False  # No hay colisión en la puerta de salida

        # Verificar  normales en los bloques del mapa
        return self.bloque.colision(x, y)

    
    def seguir_a_pacman(self):
        # Persigue a Pac-Man utilizando rutas simples y movimientos paso a paso.
        if self.fantasmas.siguiente_celda is None or (self.fantasmas.x == self.fantasmas.siguiente_celda[0] and self.fantasmas.y == self.fantasmas.siguiente_celda[1]):
            inicio = (self.fantasmas.x // 16 * 16, self.fantasmas.y // 16 * 16)
            objetivo = (self.pacman.x // 16 * 16, self.pacman.y // 16 * 16)
            ruta = self.buscar_ruta_simple(inicio, objetivo)

            if ruta and len(ruta) > 1:
                self.fantasmas.siguiente_celda = ruta[1]
            else:
                self.siguiente_celda = None

        self.mover_hacia_siguiente_celda()


    def alejarse_de_pacman(self):
        # Se aleja de Pac-Man utilizando celdas que aumentan la distancia entre ambos.
        if self.siguiente_celda is None or (self.x == self.siguiente_celda[0] and self.y == self.siguiente_celda[1]):
            inicio = (self.fantasmas.x // 16 * 16, self.fantasmas.y // 16 * 16)
            pacman_pos = (self.pacman.x // 16 * 16, self.pacman.y // 16 * 16)

            # Evaluar todas las celdas adyacentes y elegir la que maximiza la distancia a Pac-Man
            opciones = []
            for dx, dy in [(-16, 0), (16, 0), (0, -16), (0, 16)]:
                vecino = (inicio[0] + dx, inicio[1] + dy)
                if not self.colision_fantasmas(vecino[0], vecino[1]):  # Solo considerar celdas sin colisión
                    distancia = abs(vecino[0] - pacman_pos[0]) + abs(vecino[1] - pacman_pos[1])
                    opciones.append((distancia, vecino))

            # Ordenar por mayor distancia y seleccionar la mejor opción
            if opciones:
                mayor_distancia = -1
                mejor_celda = None

                # Encontrar la celda con la mayor distancia
                for distancia, celda in opciones:
                    if distancia > mayor_distancia:
                        mayor_distancia = distancia
                        mejor_celda = celda

                self.fantasmas.siguiente_celda = mejor_celda  # Asignar la mejor celda
            else:
                self.fantasmas.siguiente_celda = None  # No hay celdas válidas  # No hay celdas válidas

        # Movimiento paso a paso hacia la siguiente celda
        self.mover_hacia_siguiente_celda()


    def mover_hacia_siguiente_celda(self):
        # Mueve al fantasma hacia la celda calculada.
        if self.fantasmas.siguiente_celda:
            dx = self.fantasmas.siguiente_celda[0] - self.fantasmas.x
            dy = self.fantasmas.siguiente_celda[1] - self.fantasmas.y

            if dx > 0:
                self.fantasmas.x += min(self.fantasmas.velocidad, dx)
                self.fantasmas.direccion_actual_fantasma = "DERECHA"
            elif dx < 0:
                self.fantasmas.x += max(-self.fantasmas.velocidad, dx)
                self.fantasmas.direccion_actual_fantasma = "IZQUIERDA"
            elif dy > 0:
                self.fantasmas.y += min(self.fantasmas.velocidad, dy)
                self.fantasmas.direccion_actual_fantasma = "ABAJO"
            elif dy < 0:
                self.fantasmas.y += max(-self.fantasmas.velocidad, dy)
                self.fantasmas.direccion_actual_fantasma = "ARRIBA"

    def buscar_ruta_simple(self, inicio, objetivo):
        # Encuentra una ruta básica hacia el objetivo utilizando búsqueda en anchura (BFS).
        cola = deque([inicio])
        visitados = {inicio: None}

        while cola:
            actual = cola.popleft()

            if actual == objetivo:
                ruta = []
                while actual is not None:
                    ruta.append(actual)
                    actual = visitados[actual]
                ruta.reverse()
                return ruta

            for dx, dy in [(-16, 0), (16, 0), (0, -16), (0, 16)]:
                vecino = (actual[0] + dx, actual[1] + dy)
                if vecino not in visitados and not self.colision_fantasmas(vecino[0], vecino[1]):
                    visitados[vecino] = actual
                    cola.append(vecino)

        return None


#######################################################################################################

                    #PACMAN


    def movimineto_pacman(self,):
        if self.pacman.vidas <= 0 or self.pacman.en_muerte or self.pacman.reiniciando:  # Si no hay vidas, está en muerte o reiniciando, no se mueve
            return False

        nueva_x, nueva_y = self.pacman.x, self.pacman.y

        # Detectar entrada del jugador para cambiar dirección
        if pyxel.btnp(pyxel.KEY_UP):
            self.pacman.direccion_pendiente = PACMAN_ARRIBA
        elif pyxel.btnp(pyxel.KEY_DOWN):
            self.pacman.direccion_pendiente = PACMAN_ABAJO
        elif pyxel.btnp(pyxel.KEY_LEFT):
            self.pacman.direccion_pendiente = PACMAN_IZQUIERDA
        elif pyxel.btnp(pyxel.KEY_RIGHT):
            self.pacman.direccion_pendiente = PACMAN_DERECHA
        elif pyxel.btnp(pyxel.KEY_W):
            self.pacman.direccion_pendiente = PACMAN_ARRIBA
        elif pyxel.btnp(pyxel.KEY_S):
            self.pacman.direccion_pendiente = PACMAN_ABAJO
        elif pyxel.btnp(pyxel.KEY_A):
            self.pacman.direccion_pendiente = PACMAN_IZQUIERDA
        elif pyxel.btnp(pyxel.KEY_D):
            self.pacman.direccion_pendiente = PACMAN_DERECHA

        # Verificar si la dirección pendiente es válida
        if self.pacman.direccion_pendiente:
            if self.pacman.direccion_pendiente == PACMAN_ARRIBA and not self.bloque.colision(self.pacman.x, self.pacman.y - self.pacman.velocidad):
                self.pacman.direccion_actual = self.pacman.direccion_pendiente
            elif self.pacman.direccion_pendiente == PACMAN_ABAJO and not self.bloque.colision(self.pacman.x, self.pacman.y + self.pacman.velocidad):
                self.pacman.direccion_actual = self.pacman.direccion_pendiente
            elif self.pacman.direccion_pendiente == PACMAN_IZQUIERDA and not self.bloque.colision(self.pacman.x - self.pacman.velocidad, self.pacman.y):
                self.pacman.direccion_actual = self.pacman.direccion_pendiente
            elif self.pacman.direccion_pendiente == PACMAN_DERECHA and not self.bloque.colision(self.pacman.x + self.pacman.velocidad, self.pacman.y):
                self.pacman.direccion_actual = self.pacman.direccion_pendiente

        # Mover en la dirección actual
        if self.pacman.direccion_actual == PACMAN_ARRIBA:
            nueva_y -= self.pacman.velocidad
        elif self.pacman.direccion_actual == PACMAN_ABAJO:
            nueva_y += self.pacman.velocidad
        elif self.pacman.direccion_actual == PACMAN_IZQUIERDA:
            nueva_x -= self.pacman.velocidad
        elif self.pacman.direccion_actual == PACMAN_DERECHA:
            nueva_x += self.pacman.velocidad

        # Verificar colisiones
        if not self.bloque.colision(nueva_x, self.pacman.y):
            self.pacman.x = nueva_x
        if not self.bloque.colision(self.pacman.x, nueva_y):
            self.pacman.y = nueva_y

        #  Portales
        if (self.pacman.x, self.pacman.y) in PORTALES:
            self.pacman.x, self.pacman.y = PORTALES[(self.pacman.x, self.pacman.y)]

        print("Pacman", self.pacman.x, self.pacman.y)

    def animar_muerte(self):
        if self.pacman.animacion_frame < len(ANIMACION_MUERTE):
            # Dibuja solo la animación de muerte de Pac-Man
            sprite_x, sprite_y = ANIMACION_MUERTE[self.pacman.animacion_frame]
            pyxel.cls(0)  # Limpia la pantalla
            self.bloque.draw()  # Dibuja el mapa
            pyxel.blt(self.pacman.x, self.pacman.y, 0, sprite_x, sprite_y, 16, 16, colkey=0)
            
            # Actualizar frame de la animación
            if pyxel.frame_count % 5 == 0:  # Cambiar cada 5 frames
                self.pacman.animacion_frame += 1
        else:
            # Finaliza la animación de muerte
            self.pacman.en_muerte = False
            self.reiniciar_tablero()  # Reiniciar posiciones de Pac-Man y fantasmas


    def reiniciar_posiciones(self):
        # Reiniciar posiciones de Pac-Man y fantasmas después de la animación
        self.pacman.x, self.pacman.y = 192, 304  # Posición inicial de Pac-Man
        for fantasma in self.fantasmas:
            fantasma.volver_a_posicion_inicial()
        self.pacman.reiniciando = False 


    
    def colision_fantasmas_con_pacman(self):
        if self.pacman.en_muerte or self.pacman.reiniciando or self.pacman.vidas <= 0:  # Si está muerto, reiniciando o sin vidas, no revisa colisiones
            return False

        # Calcular las posiciones centrales de Pac-Man y los fantasmas
        pacman_x = self.pacman.x + 8  # Centrar la posición de Pac-Man
        pacman_y = self.pacman.y + 8

        for fantasma in self.fantasmas:
            fantasma_x = fantasma.x + 8  # Centrar la posicion del fantasma
            fantasma_y = fantasma.y + 8

            # Detectar si hay colisión 
            if abs(pacman_x - fantasma_x) < 16 and abs(pacman_y - fantasma_y) < 16:
                if fantasma.asustado:
                    self.puntos.puntos += 200  # Añade puntos por comer un fantasma
                    self.fantasmas_comido = True
                    self.pacman.mostrar_puntos = True  # Poder mostrar puntos
                    self.pacman.texto_tiempo_inicio = time.time()  # Guarda el tiempo actual
                    self.pacman.posicion_fantasma_comido_x, self.pacman.posicion_fantasma_comido_y = self.pacman.x, self.pacman.y
                    fantasma.volver_a_trampa()  # Enviar fantasma a la trampa
                    return True
                else:
                    self.pacman.perder_vida()  # Pac-Man pierde una vida
                    return True
        return False  # No hay colision

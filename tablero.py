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
        self.celda_tamaño = 16
        self.bloque = Bloque()  # Mapa del juego
        self.pacman = Pacman(192, 304, self.bloque)  # Pacman y su posición inicial
        self.fantasmas = [  # Lista de fantasmas con sus posiciones iniciales
            FantasmaRojo(196, 176, self.pacman, self.bloque),
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
        self.dibujar_letras_mapa(120,16, "HIGHSCORE")
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
                self.dibujar_letras_mapa(180,245, "READY!")  # Mostrar el texto "READY!"
            else:
                pyxel.blt(180, 245, 2, 0, 0, 0, 0, colkey=0) # dibujar un vacio
        else:
            # Mantener el texto visible 
            pyxel.blt(180, 245, 2, 0, 0, 0, 0, colkey=0)
        

    def animar_fin(self):
        # Animación de GAME OVER
        if self.contador_game_over < 70:  # Duración de la animación
            if (self.contador_game_over // 10) % 2 == 0:
                self.dibujar_letras_mapa(185,208, "GAME OMVER")  # Mostrar el texto "GAME OVER"
            else:
                pyxel.blt(180, 245, 2, 0, 0, 0, 0, colkey=0) # dibujar un vacio
        else:
            # Mantener el texto visible 
            self.dibujar_letras_mapa(185,208, "GAME OMVER")

    def colision_pacman(self, x, y):
        sprite_tamaño = self.celda_tamaño
        puntos_a_verificar = [
            (x, y),  # Esquina superior izquierda
            (x + sprite_tamaño - 1, y),  # Esquina superior derecha
            (x, y + sprite_tamaño - 1),  # Esquina inferior izquierda
            (x + sprite_tamaño - 1, y + sprite_tamaño - 1),  # Esquina inferior derecha
        ]
        for px, py in puntos_a_verificar:
            for bloque_x, bloque_y, _ in self.bloque.bloques:
                if (PUERTA_SALIDA[0] <= px < PUERTA_SALIDA[0] + sprite_tamaño and
                        PUERTA_SALIDA[1] <= py < PUERTA_SALIDA[1] + sprite_tamaño):
                    continue  # Ignorar colisión en la puerta de salida
                if bloque_x <= px < bloque_x + sprite_tamaño and bloque_y <= py < bloque_y + sprite_tamaño:
                    return True  # Colisión detectada
        return False  # No hay colisión
    
    def colision_fantasmas_y_pacman(self, fantasmas, puntos):
        if self.pacman.en_muerte or self.pacman.reiniciando or self.pacman.vidas <= 0:  # Si está muerto, reiniciando o sin vidas, no revisa colisiones
            return False

        # Calcular las posiciones centrales de Pac-Man y los fantasmas
        pacman_x = self.x + 8  # Centrar la posición de Pac-Man
        pacman_y = self.y + 8

        for fantasma in fantasmas:
            fantasma_x = fantasma.x + 8  # Centrar la posicion del fantasma
            fantasma_y = fantasma.y + 8

            # Detectar si hay colisión 
            if abs(pacman_x - fantasma_x) < 16 and abs(pacman_y - fantasma_y) < 16:
                if fantasma.asustado:
                    puntos.puntos += 200  # Añade puntos por comer un fantasma
                    self.fantasmas_comido = True
                    self.mostrar_puntos = True  # Poder mostrar puntos
                    self.texto_tiempo_inicio = time.time()  # Guarda el tiempo actual
                    self.posicion_fantasma_comido_x, self.posicion_fantasma_comido_y = self.x, self.y
                    fantasma.volver_a_trampa()  # Enviar fantasma a la trampa
                    return True
                else:
                    self.perder_vida()  # Pac-Man pierde una vida
                    return True

        return False  # No hay colision
    

    def dibujar_letras_mapa(self, x, y, sprite):
        # Dibuja las letras en el mapa
        sprite = TEXTO[sprite]
        pyxel.blt(x, y, 0, sprite["Coordenadas"][0], sprite["Coordenadas"][1], sprite["Tamaño"][0], sprite["Tamaño"][1], colkey=0)


    def generar_puntos(self):
        # Poner los puntos en el mapa
        for x in range(0, pyxel.width, 16):
            for y in range(0, pyxel.height, 16):
                if not self.esta_en_zona_prohibida(x, y) and (x, y) not in self.regalos:
                    self.lista_puntos.append((x, y, "BASTON"))


    def esta_en_zona_prohibida(self, x, y):
        # Verificar si está en una zona prohibida
        for lugar in self.zonas_prohibidas[self.bloque.nivel]:
            x1, y1, x2, y2 = lugar
            if x1 <= x <= x2 and y1 <= y <= y2:  
                return True

        # Verificar si hay un muro
        if self.bloque.colision(x, y):
            return True
        return False
    

    def encontrar_celdas_vacias(self):
        # Encuentra celdas vacías donde no haya puntos, frutas, regalos ni muros
        celdas_vacias = []
        x = 0
        while x < pyxel.width:
            y = 0
            while y < pyxel.height:
                # Verificar si la celda está vacía
                if not self.esta_en_zona_prohibida(x, y) and (x, y) not in [(p[0], p[1]) for p in self.lista_puntos] and (x, y) != self.posicion_fruta and (x, y) not in self.regalos:
                    celdas_vacias.append((x, y))
                y += 16
            x += 16
        return celdas_vacias



    def generar_fruta(self):
        # Genera una fruta en una celda vacía
        if time.time() - self.ultimo_tiempo_fruta < 30:
            return False  # No generar una nueva fruta si no han pasado 30 segundos

        # Seleccionar un objeto aleatorio sin regalos ni bastones
        objetos_dispo = ["CEREZA", "FRESA", "NARANJA", "MANZANA", "MELON", "PARAGUAS", "CAMPANA", "LLAVE"]
        self.fruta_actual = random.choice(objetos_dispo)

        # Elegir una posición aleatoria en celdas vacías
        celdas_vacias = self.encontrar_celdas_vacias()
        if celdas_vacias:  # Si existen posiciones vacías, genera la fruta y permite que se ejecute la animación
            self.posicion_fruta = random.choice(celdas_vacias)
            self.animacion_activa = True  # Activa la animación
            self.animacion_contador = 0  # Reinicia el contador de la animación
        else:
            self.posicion_fruta = None  # No hay espacio libre para generar una fruta

        # Actualiza el tiempo de la última fruta generada
        self.ultimo_tiempo_fruta = time.time()


    def comer_puntos(self):
        # Detectar si Pac-Man come puntos
        puntos_sin_comer = []
        for x, y, tipo in self.lista_puntos:
            if self.detectar_colision(self.pacman.x, self.pacman.y, x, y):
                # Incrementar puntos según el tipo
                self.puntos += OBJETOS[tipo]["Puntos"]
            else:
                puntos_sin_comer.append((x, y, tipo))
        self.lista_puntos = puntos_sin_comer

        # Detectar si Pac-Man come un regalo
        regalos_sin_comer = []
        for x, y in self.regalos:
            if self.detectar_colision(self.pacman.x, self.pacman.y, x, y):
                # Activar estado asustado para los fantasmas
                for fantasma in self.fantasmas:
                    fantasma.activar_asustado()
                self.puntos += OBJETOS["REGALO"]["Puntos"]  # Incrementar los puntos por el regalo
            else:
                regalos_sin_comer.append((x, y))
        self.regalos = regalos_sin_comer

    def detectar_colision(self, pacman_x, pacman_y, punto_x, punto_y):
        # Detecta si Pac-Man ha comido un punto
        return abs(pacman_x - punto_x) < 10 and abs(pacman_y - punto_y) < 10


    def comer_fruta(self):
        # Detecta si Pac-Man come la fruta actual.
        if self.posicion_fruta and self.detectar_colision(self.pacman.x, self.pacman.y, self.posicion_fruta[0], self.posicion_fruta[1]):
            self.puntos += OBJETOS[self.fruta_actual]["Puntos"]  # Incrementa los puntos según la fruta
            self.posicion_fruta = None  # Elimina la fruta actual
            self.fruta_actual = None


    def comprobar_puntos_restantes(self):
        # Verifica si no quedan puntos ni regalos
        if len(self.lista_puntos) == 0 and len(self.regalos) == 0:
            return True
        return False


    def ver_puntuacion(self, x, y):
        # Cambia el color solo cuando se supera un nuevo múltiplo de 500
        colores_dispo = [NUMEROS_BLANCOS, NUMEROS_MORADOS, NUMEROS_NARANJAS, NUMEROS_VERDES]
        if self.puntos // 500 > self.puntos_alcanzados:
            self.puntos_alcanzados = self.puntos // 500  # Actualiza los puntos alcanzados
            self.color_actual = random.choice(colores_dispo)  # Elige un nuevo color aleatorio

        color_numeros = self.color_actual
        puntuacion_str = str(self.puntos)
        pos_x = x

        for num in puntuacion_str:
            num = int(num)
            sprite = color_numeros[str(num)]
            sprite_x, sprite_y = sprite["Coordenadas"]
            sprite_w, sprite_h = sprite["Tamaño"]

            pyxel.blt(
                pos_x, y,
                0, sprite_x, sprite_y, sprite_w, sprite_h, colkey=0
            )
            pos_x += sprite_w + 1  # Espacio entre los numeros


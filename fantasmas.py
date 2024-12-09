import pyxel
from constantes import *
from collections import deque
import time
import random

class Fantasma:
    def __init__(self, x, y, sprites, pacman, bloque):
        self.x = x
        self.y = y
        self.velocidad = 2
        self.x_inicial = x  # Guardar posición inicial
        self.y_inicial = y  # Guardar posición inicial
        self.sprites = sprites
        self.pacman = pacman
        self.bloque = bloque
        self.direccion_actual = "DERECHA"
        self.asustado = False  # Indica si está en estado asustado
        self.tiempo_asustado = 0  # Temporizador para estado asustado
        self.tiempo_para_ser_comido = 10  # Duración por defecto del estado asustado
        self.tiempo_trampa = time.time()  # Temporizador para controlar salida
        self.salida_coordenadas = (196, 176)  # Punto fuera de la trampa
        self.puerta_salida_coordenadas = (192, 192) # Punto de la puerta de salida de la trampa para colision
        self.trampa_coordenadas = ((144, 192), (240, 224))  # Región de la trampa
        self.siguiente_celda = None  # Almacena la próxima celda hacia la que se mueve el fantasma


    def en_trampa(self):
        # Verifica si el fantasma está dentro de la región de la trampa.
        if self.trampa_coordenadas[0][0] <= self.x <= self.trampa_coordenadas[1][0] and \
            self.trampa_coordenadas[0][1] <= self.y <= self.trampa_coordenadas[1][1]:
            return True
        return False



    def activar_asustado(self):
        #Activa el estado asustado
        self.asustado = True
        self.velocidad = 1
        self.tiempo_asustado = time.time()


    def volver_a_trampa(self):
        # Envía al fantasma a la trampa
        if isinstance(self, FantasmaRojo):
            self.x, self.y = 158, 208
        elif isinstance(self, FantasmaRosa):
            self.x, self.y = 181, 208
        elif isinstance(self, FantasmaAzul):
            self.x, self.y = 203, 208
        elif isinstance(self, FantasmaNaranja):
            self.x, self.y = 225, 208
        self.asustado = False  # Sale del estado asustado
        self.velocidad = 2

    def salir_de_trampa(self):
        if self.en_trampa():
            if (self.x, self.y) == self.puerta_salida:
                # Moverse hacia la salida final
                dx, dy = self.salida_final[0] - self.x, self.salida_final[1] - self.y
            else:
                # Moverse hacia la puerta
                dx, dy = self.puerta_salida[0] - self.x, self.puerta_salida[1] - self.y

            if dx > 0:
                self.x += min(self.velocidad, dx)
            elif dx < 0:
                self.x -= min(self.velocidad, abs(dx))
            elif dy > 0:
                self.y += min(self.velocidad, dy)
            elif dy < 0:
                self.y -= min(self.velocidad, abs(dy))

    def colision(self, x, y):
        # Verifica si hay una colisión, ignorando las coordenadas de salida
        if self.en_trampa() and (x, y) == self.puerta_salida_coordenadas:
            return False  # Ignorar la colisión en la puerta de salida y el punto fuera de la trampa
        return self.bloque.colision(x, y)  # Usar colisión normal fuera de la trampa


    def volver_a_posicion_inicial(self):
        self.x = self.x_inicial // 16 * 16  # Alinear con la cuadrícula
        self.y = self.y_inicial // 16 * 16  # Alinear con la cuadrícula
        self.siguiente_celda = None  # Limpiar la ruta almacenada
        self.asustado = False
        self.tiempo_trampa = time.time()
        


    def actualizar_estado(self):
        #Verifica y actualiza el estado asustado
        if self.asustado:
            tiempo_restante = self.tiempo_para_ser_comido - (time.time() - self.tiempo_asustado)
            if tiempo_restante <= 0:
                self.asustado = False  # Finaliza el estado asustado
                self.velocidad = 2



    def mover_en_direccion(self, direccion):    
        # Mueve al fantasma en la dirección especificada si es posible.
        if direccion == "ARRIBA" and not self.bloque.colision(self.x, self.y - self.velocidad):
            self.y -= self.velocidad
            self.direccion_actual = "ARRIBA"
            return True
        elif direccion == "ABAJO" and not self.bloque.colision(self.x, self.y + self.velocidad):
            self.y += self.velocidad
            self.direccion_actual = "ABAJO"
            return True
        elif direccion == "IZQUIERDA" and not self.bloque.colision(self.x - self.velocidad, self.y):
            self.x -= self.velocidad
            self.direccion_actual = "IZQUIERDA"
            return True
        elif direccion == "DERECHA" and not self.bloque.colision(self.x + self.velocidad, self.y):
            self.x += self.velocidad
            self.direccion_actual = "DERECHA"
            return True
        return False
    

    def seguir_a_pacman(self):
        # Persigue a Pac-Man utilizando rutas simples y movimientos paso a paso.
        if self.siguiente_celda is None or (self.x == self.siguiente_celda[0] and self.y == self.siguiente_celda[1]):
            inicio = (self.x // 16 * 16, self.y // 16 * 16)
            objetivo = (self.pacman.x // 16 * 16, self.pacman.y // 16 * 16)
            ruta = self.buscar_ruta_simple(inicio, objetivo)

            if ruta and len(ruta) > 1:
                self.siguiente_celda = ruta[1]
            else:
                self.siguiente_celda = None

        self.mover_hacia_siguiente_celda()


    def alejarse_de_pacman(self):
        # Se aleja de Pac-Man utilizando celdas que aumentan la distancia entre ambos.
        if self.siguiente_celda is None or (self.x == self.siguiente_celda[0] and self.y == self.siguiente_celda[1]):
            inicio = (self.x // 16 * 16, self.y // 16 * 16)
            pacman_pos = (self.pacman.x // 16 * 16, self.pacman.y // 16 * 16)

            # Evaluar todas las celdas adyacentes y elegir la que maximiza la distancia a Pac-Man
            opciones = []
            for dx, dy in [(-16, 0), (16, 0), (0, -16), (0, 16)]:
                vecino = (inicio[0] + dx, inicio[1] + dy)
                if not self.bloque.colision(vecino[0], vecino[1]):  # Solo considerar celdas sin colisión
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

                self.siguiente_celda = mejor_celda  # Asignar la mejor celda
            else:
                self.siguiente_celda = None  # No hay celdas válidas  # No hay celdas válidas

        # Movimiento paso a paso hacia la siguiente celda
        self.mover_hacia_siguiente_celda()


    def mover_hacia_siguiente_celda(self):
        # Mueve al fantasma hacia la celda calculada.
        if self.siguiente_celda:
            dx = self.siguiente_celda[0] - self.x
            dy = self.siguiente_celda[1] - self.y

            if dx > 0:
                self.x += min(self.velocidad, dx)
                self.direccion_actual = "DERECHA"
            elif dx < 0:
                self.x += max(-self.velocidad, dx)
                self.direccion_actual = "IZQUIERDA"
            elif dy > 0:
                self.y += min(self.velocidad, dy)
                self.direccion_actual = "ABAJO"
            elif dy < 0:
                self.y += max(-self.velocidad, dy)
                self.direccion_actual = "ARRIBA"

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
                if vecino not in visitados and not self.bloque.colision(vecino[0], vecino[1]):
                    visitados[vecino] = actual
                    cola.append(vecino)

        return None


    def draw(self):
        #Dibuja el fantasma en su estado actual.
        if self.asustado:
            # Alternar entre azul y blanco si está asustado
            if pyxel.frame_count // REFRESH % 2 == 0:
                sprite = FANTASMAS_ASUSTADOS["AZUL"]["Coordenadas"]
            else:
                sprite = FANTASMAS_ASUSTADOS["BLANCO"]["Coordenadas"]
        else:
            sprite = self.sprites[self.direccion_actual]  # Usar sprite según dirección

        # Dibuja el fantasma
        pyxel.blt(self.x, self.y, 0, sprite[0], sprite[1], 16, 16, colkey=0)


# Subclases de Fantasma
class FantasmaRojo(Fantasma):
    def __init__(self, x, y, pacman, bloque):
        super().__init__(x, y, FANTASMA_ROJO, pacman, bloque)
        self.siguiente_celda = None  # Almacena la próxima celda hacia la que se mueve el fantasma

    def mover(self):
        if not self.en_trampa():
            # Movimiento normal fuera de la trampa
            if not self.asustado:
                self.seguir_a_pacman()
            else:
                self.alejarse_de_pacman()
        else:
            # Si por error detecta que esta en la trampa, se mueve hacia la salida
            self.salir_de_trampa()

class FantasmaRosa(Fantasma):
    def __init__(self, x, y, pacman, bloque):
        # Inicializa al Fantasma Rosa con su sprite.
        super().__init__(x, y, FANTASMA_ROSA, pacman, bloque)

    def mover(self):
        pass

class FantasmaAzul(Fantasma):
    def __init__(self, x, y, pacman, bloque):
        # Inicializa al Fantasma Azul con su sprite.
        super().__init__(x, y, FANTASMA_AZUL, pacman, bloque)

    def mover(self):
        pass

class FantasmaNaranja(Fantasma):
    def __init__(self, x, y, pacman, bloque):
        # Inicializa al Fantasma Naranja con su sprite.
        super().__init__(x, y, FANTASMA_NARANJA, pacman, bloque)

    def mover(self):
        pass
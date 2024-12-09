import pyxel
from constantes import *
from collections import deque
import time

class Fantasma:
    def __init__(self, x, y, sprites,pacman,bloque):
        self.x = x
        self.y = y
        self.velocidad = 1
        self.x_inicial = x  # Guardar posición inicial
        self.y_inicial = y  # Guardar posición inicial
        self.sprites = sprites
        self.pacman = pacman
        self.bloque = bloque
        self.direccion_actual = "DERECHA"  # Dirección inicial
        self.asustado = False  # Indica si está en estado asustado
        self.tiempo_asustado = 0  # Temporizador para estado asustado
        self.tiempo_para_ser_comido = 10  # Duración por defecto del estado asustado
        self.en_trampa = False  # Indica si el fantasma está en la trampa


    def activar_asustado(self):
        #Activa el estado asustado
        self.asustado = True
        self.velocidad = 1
        self.tiempo_asustado = time.time()


    def volver_a_trampa(self):
        # Envía al fantasma a la trampa
        self.en_trampa = True
        if isinstance(self, FantasmaRojo):
            self.x, self.y = 158, 208
        elif isinstance(self, FantasmaRosa):
            self.x, self.y = 181, 208
        elif isinstance(self, FantasmaAzul):
            self.x, self.y = 203, 208
        elif isinstance(self, FantasmaNaranja):
            self.x, self.y = 226, 208
        self.asustado = False  # Sale del estado asustado
        self.velocidad = 2


    def volver_a_posicion_inicial(self):
        #Restaura la posición inicial del fantasma
        self.x = self.x_inicial
        self.y = self.y_inicial
        self.asustado = False
        self.en_trampa = False


    def actualizar_estado(self):
        #Verifica y actualiza el estado asustado
        if self.asustado:
            tiempo_restante = self.tiempo_para_ser_comido - (time.time() - self.tiempo_asustado)
            if tiempo_restante <= 0:
                self.asustado = False  # Finaliza el estado asustado
                self.velocidad = 2

    def mover_en_direccion(self, direccion):
        #Mueve al fantasma en la dirección indicada si es posible.
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
        # Mueve al fantasma hacia Pac-Man 
        if self.siguiente_celda is None or (self.x == self.siguiente_celda[0] and self.y == self.siguiente_celda[1]):
            # Si no hay una celda objetivo o ya llegamos a la celda objetivo, buscar una nueva ruta
            inicio = (self.x // 16 * 16, self.y // 16 * 16)  # Redondear posición a la celda más cercana
            objetivo = (self.pacman.x // 16 * 16, self.pacman.y // 16 * 16)  # Redondear posición de Pac-Man a la celda más cercana
            ruta = self.buscar_ruta_simple(inicio, objetivo)

            if ruta and len(ruta) > 1:
                self.siguiente_celda = ruta[1]  # Próxima celda en la ruta
            else:
                self.siguiente_celda = None  # No hay ruta disponible

        # Movimiento paso a paso hacia la siguiente celda
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
        cola = deque([inicio])  # Posiciones a explorar
        visitados = {inicio: None}  # Rastro de posiciones visitadas

        while cola:
            actual = cola.popleft()

            # Si llegamos al objetivo, reconstruimos la ruta
            if actual == objetivo:
                ruta = []
                while actual is not None:
                    ruta.append(actual)
                    actual = visitados[actual]
                ruta.reverse()
                return ruta

            # Evaluar vecinos (ARRIBA, ABAJO, IZQUIERDA, DERECHA)
            for dx, dy in [(-16, 0), (16, 0), (0, -16), (0, 16)]:
                vecino = (actual[0] + dx, actual[1] + dy)
                if vecino not in visitados and not self.bloque.colision(vecino[0], vecino[1]):
                    visitados[vecino] = actual
                    cola.append(vecino)

        return None  # No hay ruta disponible

class FantasmaRosa(Fantasma):
    def __init__(self, x, y, pacman, bloque):
        super().__init__(x, y, FANTASMA_ROSA, pacman, bloque)

    def mover(self):
        pass

class FantasmaAzul(Fantasma):
    def __init__(self, x, y, pacman, bloque):
        super().__init__(x, y, FANTASMA_AZUL, pacman, bloque)
    
    def mover(self):
        pass

class FantasmaNaranja(Fantasma):
    def __init__(self, x, y, pacman, bloque):
        super().__init__(x, y, FANTASMA_NARANJA, pacman, bloque)

    def mover(self):
        pass
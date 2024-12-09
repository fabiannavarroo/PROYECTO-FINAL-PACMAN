import pyxel
from constantes import *
from collections import deque
import time

class Fantasma:
    def __init__(self, x, y, sprites,pacman,bloque):
        self.x = x
        self.y = y
        self.velocidad = 0.1
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
        self.tiempo_trampa = 0  # Tiempo que el fantasma lleva en la trampa
        self.ultimo_movimiento = time.time()  # Temporizador para controlar la velocidad de movimiento



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
        self.velocidad = 0.1


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
                self.velocidad = 0.1

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
    
    def salir_de_trampa(self):
        if self.en_trampa and time.time() - self.tiempo_trampa >= 3:
            self.en_trampa = False


    def mover(self,):
        if time.time() - self.ultimo_movimiento >= 0.2:  # Limitar movimiento a cada 0.2 segundos
            self.ultimo_movimiento = time.time()
            # Implementar la lógica de movimiento de cada fantasma en subclases
            pass

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
        if not self.en_trampa:
            inicio = (self.x // 16 * 16, self.y // 16 * 16)
            objetivo = (self.pacman.x // 16 * 16, self.pacman.y // 16 * 16)
            ruta = self.buscar_ruta_simple(inicio, objetivo)
            if ruta and len(ruta) > 1:
                siguiente_celda = ruta[1]
                dx, dy = siguiente_celda[0] - self.x, siguiente_celda[1] - self.y
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
        cola = deque([inicio])
        visitados = {inicio: None}
        while cola:
            actual = cola.popleft()
            if actual == objetivo:
                ruta = []
                while actual:
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
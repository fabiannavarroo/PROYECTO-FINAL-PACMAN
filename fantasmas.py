import pyxel
from constantes import *
import time


class Fantasma:
    def __init__(self, x, y, sprites):
        self.x = x
        self.y = y
        self.velocidad = 2
        self.x_inicial = x  # Guardar posición inicial
        self.y_inicial = y  # Guardar posición inicial
        self.sprites = sprites
        self.direccion_actual = "DERECHA"
        self.asustado = False  # Indica si está en estado asustado
        self.tiempo_asustado = 0  # Temporizador para estado asustado
        self.tiempo_para_ser_comido = 10  # Duración por defecto del estado asustado
        self.tiempo_trampa = time.time()  # Temporizador para controlar salida
        self.siguiente_celda = None  # Almacena la próxima celda hacia la que se mueve el fantasma
        self.salida_final = (192, 176)  # Punto fuera de la trampa
        self.puerta_salida = (192, 192) # Punto de la puerta de salida de la trampa para colision
        self.trampa_coordenadas = ((144, 10), (240, 224))  # Región de la trampa


    def activar_asustado(self):
        #Activa el estado asustado
        self.asustado = True
        self.velocidad = 1
        self.tiempo_asustado = time.time()


    def en_posicion_inicial(self):
        return self.x == self.x_inicial and self.y == self.y_inicial


    def salir_de_inicial(self):
        self.en_salida = True


    def en_camino_salida(self):
        return self.en_salida


    def mover_a_salida_final(self):
        dx = 192 - self.x
        dy = 176 - self.y
        if abs(dx) > 0:
            self.x += self.velocidad if dx > 0 else -self.velocidad
        elif abs(dy) > 0:
            self.y += self.velocidad if dy > 0 else -self.velocidad
        else:
            self.en_salida = False


    def volver_a_posicion_inicial(self):
        self.x, self.y = self.x_inicial, self.y_inicial
        self.en_salida = False
        self.tiempo_espera = time.time()
        

    def actualizar_estado(self):
        #Verifica y actualiza el estado asustado
        if self.asustado:
            tiempo_restante = self.tiempo_para_ser_comido - (time.time() - self.tiempo_asustado)
            if tiempo_restante <= 0:
                self.asustado = False  # Finaliza el estado asustado
                self.velocidad = 2
    

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
    def __init__(self, x, y):
        super().__init__(x, y, FANTASMA_ROJO)
       
class FantasmaRosa(Fantasma):
    def __init__(self, x, y):
        # Inicializa al Fantasma Rosa
        super().__init__(x, y, FANTASMA_ROSA)


class FantasmaAzul(Fantasma):
    def __init__(self, x, y):
        # Inicializa al Fantasma Azul
        super().__init__(x, y, FANTASMA_AZUL)


class FantasmaNaranja(Fantasma):
    def __init__(self, x, y):
        # Inicializa al Fantasma Naranja
        super().__init__(x, y, FANTASMA_NARANJA)

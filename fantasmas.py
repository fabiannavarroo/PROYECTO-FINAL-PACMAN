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
        self.tiempo_trampa = time.time()  
        self.en_salida = False
        self.en_trampa = True  # Indica si está en la trampa
        self.posicion_salida = (192, 176)
        self.siguiente_celda = None


    def activar_asustado(self):
        #Activa el estado asustado
        self.asustado = True
        self.velocidad = 1
        self.tiempo_asustado = time.time()

    def volver_a_posicion_inicial(self):
        # Reinicia la posición del fantasma a la inicial
        self.x, self.y = self.x_inicial, self.y_inicial
        self.en_trampa = True
        self.en_salida = False
        self.asustado = False
        self.velocidad = 2
        self.tiempo_trampa = time.time()

    def mover_a_salida(self):
        # Movimiento hacia las coordenadas de salida
        dx = self.posicion_salida[0] - self.x
        dy = self.posicion_salida[1] - self.y
        if abs(dx) > 0:
            if dx > 0:  
                self.x += self.velocidad 
                self.direccion_actual = "DERECHA" 
            else:
                self.x -= self.velocidad
                self.direccion_actual = "IZQUIERDA" 
        elif abs(dy) > 0:
            if dy > 0:
                self.y += self.velocidad 
                self.direccion_actual = "ABAJO" 
            else:
                self.y -= self.velocidad
                self.direccion_actual = "ARRIBA" 
        else:
            self.en_salida = False
            self.en_trampa = False  # Marcamos que ha salido de la trampa
        

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

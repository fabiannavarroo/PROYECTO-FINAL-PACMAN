import pyxel
from constantes import *
from collections import deque
import time
import random

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
        self.salida_final = SALIDA_FINAL  # Punto fuera de la trampa
        self.puerta_salida = PUERTA_SALIDA # Punto de la puerta de salida de la trampa para colision
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
        # Reubicar al fantasma en la trampa y reiniciar estado
        self.x, self.y = self.x_inicial, self.y_inicial
        self.siguiente_celda = None
        self.asustado = False # Sale del estado asustado
        self.direccion_actual = "DERECHA"
        self.tiempo_trampa = time.time()
        self.velocidad = 2
        
        # Coordenadas de la trampa de cada fantasma
        if isinstance(self, FantasmaRojo):
            self.x, self.y = 158, 208
        elif isinstance(self, FantasmaRosa):
            self.x, self.y = 181, 208
        elif isinstance(self, FantasmaAzul):
            self.x, self.y = 203, 208
        elif isinstance(self, FantasmaNaranja):
            self.x, self.y = 225, 208
        

    def salir_de_trampa(self):
        if self.en_trampa():
            if (self.x, self.y) == self.puerta_salida:
                # Mover hacia la salida final
                dx, dy = self.salida_final[0] - self.x, self.salida_final[1] - self.y
            else:
                # Mover hacia la puerta de salida
                dx, dy = self.puerta_salida[0] - self.x, self.puerta_salida[1] - self.y

            if dx != 0:
                self.x += self.velocidad if dx > 0 else -self.velocidad
            elif dy != 0:
                self.y += self.velocidad if dy > 0 else -self.velocidad
        
            if self.en_trampa():
                if abs(self.x - PUERTA_SALIDA[0]) <= 1 and abs(self.y - PUERTA_SALIDA[1]) <= 1:
                    # Mover hacia la salida final una vez alcanzada la puerta
                    dx, dy = SALIDA_FINAL[0] - self.x, SALIDA_FINAL[1] - self.y
                else:
                    # Mover hacia la puerta de salida
                    dx, dy = PUERTA_SALIDA[0] - self.x, PUERTA_SALIDA[1] - self.y

                if dx > 0:
                    self.x += min(self.velocidad, dx)
                elif dx < 0:
                    self.x -= min(self.velocidad, abs(dx))
                elif dy > 0:
                    self.y += min(self.velocidad, dy)
                elif dy < 0:
                    self.y -= min(self.velocidad, abs(dy))


    def volver_a_posicion_inicial(self):
        self.x = self.x_inicial
        self.y = self.y_inicial  
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
        self.x, self.y = 158, 208  # Coordenadas dentro de la trampa
        self.tiempo_trampa = time.time()  # Asegurar tiempo correcto
       
class FantasmaRosa(Fantasma):
    def __init__(self, x, y):
        # Inicializa al Fantasma Rosa con su sprite.
        super().__init__(x, y, FANTASMA_ROSA)


class FantasmaAzul(Fantasma):
    def __init__(self, x, y):
        # Inicializa al Fantasma Azul con su sprite.
        super().__init__(x, y, FANTASMA_AZUL)


class FantasmaNaranja(Fantasma):
    def __init__(self, x, y):
        # Inicializa al Fantasma Naranja con su sprite.
        super().__init__(x, y, FANTASMA_NARANJA)

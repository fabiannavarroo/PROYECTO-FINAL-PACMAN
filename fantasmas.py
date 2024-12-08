import pyxel
from constantes import *
import random  
import time

class Fantasma:
    def __init__(self, x, y, sprites):
        self.x = x
        self.y = y
        self.velocidad = 1.5
        self.x_inicial = x  # Guardar posición inicial
        self.y_inicial = y  # Guardar posición inicial
        self.sprites = sprites
        self.direccion_actual = "DERECHA"  # Dirección inicial
        self.asustado = False  # Indica si está en estado asustado
        self.tiempo_asustado = 0  # Temporizador para estado asustado
        self.tiempo_para_ser_comido = 10  # Duración por defecto del estado asustado
        self.en_trampa = True  # Inicia en la trampa
        self.tiempo_salida_trampa = time.time()  # Temporizador para salir de la trampa

    def activar_asustado(self):
        self.asustado = True
        self.tiempo_asustado = time.time()


    def volver_a_trampa(self):
        # Volver a la trampa cuando Pac-Man lo coma
        self.en_trampa = True
        self.x, self.y = self.x_inicial, self.y_inicial
        self.tiempo_salida_trampa = time.time()
        self.asustado = False


    def actualizar_estado(self):
        # Si está en la trampa, verifica si puede salir después de 3 segundos
        if self.en_trampa:
            if time.time() - self.tiempo_salida_trampa >= 3:
                self.en_trampa = False

        # Verifica si se termina el estado asustado
        if self.asustado:
            self.velocidad = 1
            tiempo_restante = self.tiempo_para_ser_comido - (time.time() - self.tiempo_asustado)
            if tiempo_restante <= 0:
                self.asustado = False


    def obtener_direcciones_validas(self, bloque):
        # Calcula las direcciones posibles desde la posición actual
        direcciones = []
        if not bloque.colision(self.x + self.velocidad, self.y):
            direcciones.append("DERECHA")
        if not bloque.colision(self.x - self.velocidad, self.y):
            direcciones.append("IZQUIERDA")
        if not bloque.colision(self.x, self.y + self.velocidad):
            direcciones.append("ABAJO")
        if not bloque.colision(self.x, self.y - self.velocidad):
            direcciones.append("ARRIBA")
        return direcciones
   
   
    def volver_a_posicion_inicial(self):
        #Restaura la posición inicial del fantasma
        self.x = self.x_inicial
        self.y = self.y_inicial
        self.asustado = False
        self.en_trampa = False



    def mover(self, pacman, bloque):
        if self.en_trampa:  # No se mueve si está en la trampa
            return

        # Obtener dirección hacia Pac-Man o aleatoria si no puede avanzar
        direcciones_validas = self.obtener_direcciones_validas(bloque)
        if direcciones_validas:
            if pacman.x > self.x and "DERECHA" in direcciones_validas:
                self.x += self.velocidad
                self.direccion_actual = "DERECHA"
            elif pacman.x < self.x and "IZQUIERDA" in direcciones_validas:
                self.x -= self.velocidad
                self.direccion_actual = "IZQUIERDA"
            elif pacman.y > self.y and "ABAJO" in direcciones_validas:
                self.y += self.velocidad
                self.direccion_actual = "ABAJO"
            elif pacman.y < self.y and "ARRIBA" in direcciones_validas:
                self.y -= self.velocidad
                self.direccion_actual = "ARRIBA"
            else:
                # Si no puede moverse directamente, elige otra dirección válida
                self.direccion_actual = random.choice(direcciones_validas)

        # Avanzar en la dirección actual
        if self.direccion_actual == "DERECHA":
            self.x += self.velocidad
        elif self.direccion_actual == "IZQUIERDA":
            self.x -= self.velocidad
        elif self.direccion_actual == "ABAJO":
            self.y += self.velocidad
        elif self.direccion_actual == "ARRIBA":
            self.y -= self.velocidad


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
        super().__init__(x, y, FANTASMA_ROJO)
        self.pacman = pacman
        self.bloque = bloque



class FantasmaRosa(Fantasma):
    def __init__(self, x, y, pacman, bloque):
        super().__init__(x, y, FANTASMA_ROSA)
        self.pacman = pacman
        self.bloque = bloque



class FantasmaAzul(Fantasma):
    def __init__(self, x, y, pacman, bloque):
        super().__init__(x, y, FANTASMA_AZUL)
        self.pacman = pacman
        self.bloque = bloque



class FantasmaNaranja(Fantasma):
    def __init__(self, x, y, pacman, bloque):
        super().__init__(x, y, FANTASMA_NARANJA)
        self.pacman = pacman
        self.bloque = bloque


        if random.random() < 0.3:
            if self.pacman.x > self.x and not self.bloque.colision(self.x - self.velocidad, self.y):
                self.x -= self.velocidad
            elif self.pacman.x < self.x and not self.bloque.colision(self.x + self.velocidad, self.y):
                self.x += self.velocidad

            if self.pacman.y > self.y and not self.bloque.colision(self.x, self.y - self.velocidad):
                self.y -= self.velocidad
            elif self.pacman.y < self.y and not self.bloque.colision(self.x, self.y + self.velocidad):
                self.y += self.velocidad
        else:
            if self.pacman.x > self.x and not self.bloque.colision(self.x + self.velocidad, self.y):
                self.x += self.velocidad
            elif self.pacman.x < self.x and not self.bloque.colision(self.x - self.velocidad, self.y):
                self.x -= self.velocidad

            if self.pacman.y > self.y and not self.bloque.colision(self.x, self.y + self.velocidad):
                self.y += self.velocidad
            elif self.pacman.y < self.y and not self.bloque.colision(self.x, self.y - self.velocidad):
                self.y -= self.velocidad
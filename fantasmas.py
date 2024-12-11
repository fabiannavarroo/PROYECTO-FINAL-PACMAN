import pyxel
from constantes import *
import time

class Fantasma:
    def __init__(self, x, y, sprites):
        self.x = x
        self.y = y
        self.velocidad = 2
        self.x_inicial = x
        self.y_inicial = y
        self.sprites = sprites
        self.direccion_actual = "DERECHA"
        self.asustado = False
        self.tiempo_asustado = 0
        self.tiempo_para_ser_comido = 10
        self.tiempo_trampa = time.time()
        self.salida_final = SALIDA_FINAL
        self.puerta_salida = PUERTA_SALIDA
        self.trampa_coordenadas = ((144, 192), (240, 224))
        self.siguiente_celda = None
        self.celdas_para_emboscada = 10
        self.ultimo_cambio_modo = time.time()
        self.modo_perseguir = True

    def en_trampa(self):
        if self.trampa_coordenadas[0][0] <= self.x <= self.trampa_coordenadas[1][0] and \
           self.trampa_coordenadas[0][1] <= self.y <= self.trampa_coordenadas[1][1]:
            return True
        return False

    def activar_asustado(self):
        self.asustado = True
        self.velocidad = 1
        self.tiempo_asustado = time.time()

    def volver_a_trampa(self):
        self.x, self.y = self.x_inicial, self.y_inicial
        self.siguiente_celda = None
        self.asustado = False
        self.direccion_actual = "DERECHA"
        self.tiempo_trampa = time.time()
        self.velocidad = 2

        # Recolocar según el tipo de fantasma
        if isinstance(self, FantasmaRojo):
            self.x, self.y = 160, 208
        elif isinstance(self, FantasmaRosa):
            self.x, self.y = 181, 208
        elif isinstance(self, FantasmaAzul):
            self.x, self.y = 203, 208
        elif isinstance(self, FantasmaNaranja):
            self.x, self.y = 225, 208

    def salir_de_trampa(self, bloque, buscar_ruta_func):
        # Usar BFS para llegar primero a la puerta de salida y luego a la salida final.
        # De esta forma si hay muros, los rodeará.
        
        if self.en_trampa():
            inicio = (self.x // 16 * 16, self.y // 16 * 16)
            
            # Primero ruta hacia la puerta de salida
            ruta_hacia_puerta = buscar_ruta_func(inicio, (self.puerta_salida[0] // 16 * 16, self.puerta_salida[1] // 16 * 16))
            if ruta_hacia_puerta and len(ruta_hacia_puerta) > 1:
                # Seguir la ruta hacia la puerta
                self.siguiente_celda = ruta_hacia_puerta[1]
                # Mover un paso hacia la puerta
                # Este movimiento se completará en update con mover_hacia_siguiente_celda
            else:
                # Si no hay ruta a la puerta, no puede salir
                return
            
            # Comprobar si ya llegó a la puerta
            if (self.x, self.y) == self.puerta_salida:
                # Ahora desde la puerta a la salida final
                ruta_hacia_salida = buscar_ruta_func((self.x // 16 * 16, self.y // 16 * 16), (self.salida_final[0] // 16 * 16, self.salida_final[1] // 16 * 16))
                if ruta_hacia_salida and len(ruta_hacia_salida) > 1:
                    self.siguiente_celda = ruta_hacia_salida[1]
                # Si no hay ruta a la salida final, se quedará en la puerta sin avanzar
        # Si no está en la trampa, no hace nada


    def volver_a_posicion_inicial(self):
        self.x = self.x_inicial
        self.y = self.y_inicial
        self.siguiente_celda = None
        self.asustado = False
        self.tiempo_trampa = time.time()

    def actualizar_estado(self):
        if self.asustado:
            tiempo_restante = self.tiempo_para_ser_comido - (time.time() - self.tiempo_asustado)
            if tiempo_restante <= 0:
                self.asustado = False
                self.velocidad = 2

    def draw(self):
        if self.asustado:
            if pyxel.frame_count // REFRESH % 2 == 0:
                sprite = FANTASMAS_ASUSTADOS["AZUL"]["Coordenadas"]
            else:
                sprite = FANTASMAS_ASUSTADOS["BLANCO"]["Coordenadas"]
        else:
            sprite = self.sprites[self.direccion_actual]

        pyxel.blt(self.x, self.y, 0, sprite[0], sprite[1], 16, 16, colkey=0)


class FantasmaRojo(Fantasma):
    def __init__(self, x, y):
        super().__init__(x, y, FANTASMA_ROJO)

class FantasmaRosa(Fantasma):
    def __init__(self, x, y):
        super().__init__(x, y, FANTASMA_ROSA)

class FantasmaAzul(Fantasma):
    def __init__(self, x, y):
        super().__init__(x, y, FANTASMA_AZUL)

class FantasmaNaranja(Fantasma):
    def __init__(self, x, y):
        super().__init__(x, y, FANTASMA_NARANJA)
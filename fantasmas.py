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
        self.celdas_para_emboscada = 3 # Distancia de emboscada para el fantasma

#--------------------------------------------------------------------PROPERTY--------------------------------------------------------------------#
        
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def velocidad(self):
        return self.__velocidad

    @property
    def x_inicial(self):
        return self.__x_inicial

    @property
    def y_inicial(self):
        return self.__y_inicial

    @property
    def sprites(self):
        return self.__sprites

    @property
    def direccion_actual(self):
        return self.__direccion_actual

    @property
    def asustado(self):
        return self.__asustado

    @property
    def tiempo_asustado(self):
        return self.__tiempo_asustado

    @property
    def tiempo_para_ser_comido(self):
        return self.__tiempo_para_ser_comido

    @property
    def tiempo_trampa(self):
        return self.__tiempo_trampa

    @property
    def en_salida(self):
        return self.__en_salida

    @property
    def en_trampa(self):
        return self.__en_trampa

    @property
    def posicion_salida(self):
        return self.__posicion_salida
    
    @property
    def celdas_para_emboscada(self):
        return self.__celdas_para_emboscada

#--------------------------------------------------------------------SETTERS--------------------------------------------------------------------#

    @x.setter
    def x(self, nuevo_valor):
        self.__x = nuevo_valor

    @y.setter
    def y(self, nuevo_valor):
        self.__y = nuevo_valor

    @velocidad.setter
    def velocidad(self, nuevo_valor):
        self.__velocidad = nuevo_valor

    @x_inicial.setter
    def x_inicial(self, nuevo_valor):
        self.__x_inicial = nuevo_valor

    @y_inicial.setter
    def y_inicial(self, nuevo_valor):
        self.__y_inicial = nuevo_valor

    @sprites.setter
    def sprites(self, nuevo_valor):
        self.__sprites = nuevo_valor

    @direccion_actual.setter
    def direccion_actual(self, nuevo_valor):
        self.__direccion_actual = nuevo_valor

    @asustado.setter
    def asustado(self, nuevo_valor):
        self.__asustado = nuevo_valor

    @tiempo_asustado.setter
    def tiempo_asustado(self, nuevo_valor):
        self.__tiempo_asustado = nuevo_valor

    @tiempo_para_ser_comido.setter
    def tiempo_para_ser_comido(self, nuevo_valor):
        self.__tiempo_para_ser_comido = nuevo_valor

    @tiempo_trampa.setter
    def tiempo_trampa(self, nuevo_valor):
        self.__tiempo_trampa = nuevo_valor

    @en_salida.setter
    def en_salida(self, nuevo_valor):
        self.__en_salida = nuevo_valor

    @en_trampa.setter
    def en_trampa(self, nuevo_valor):
        self.__en_trampa = nuevo_valor
        
    @posicion_salida.setter
    def posicion_salida(self, nuevo_valor):
        self.__posicion_salida = nuevo_valor

    @posicion_salida.setter
    def posicion_salida(self, nuevo_valor):
        self.__posicion_salida = nuevo_valor

    @celdas_para_emboscada.setter
    def celdas_para_emboscada(self, nuevo_valor):
        self.__celdas_para_emboscada = nuevo_valor

#--------------------------------------------------------------------METODOS PROPIOS--------------------------------------------------------------------#   

    def activar_asustado(self):
        #Activa el estado asustado
        self.asustado = True
        self.velocidad = 1
        self.tiempo_asustado = time.time()

    def volver_a_posicion_inicial(self):
        # Envía al fantasma a la trampa
        # Reubicar al fantasma en la trampa y reiniciar estado
        self.x, self.y = self.x_inicial, self.y_inicial
        self.siguiente_celda = None
        self.asustado = False # Sale del estado asustado
        self.direccion_actual = "DERECHA"
        self.tiempo_trampa = time.time() 
        self.en_trampa = True
        self.en_salida = False
        self.velocidad = 2


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

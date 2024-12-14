import pyxel
from constantes import *
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

    @celdas_para_emboscada.setter
    def celdas_para_emboscada(self, nuevo_valor):
        self.__celdas_para_emboscada = nuevo_valor

#--------------------------------------------------------------------METODOS PROPIOS--------------------------------------------------------------------#   

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


    def activar_asustado(self):
        #Activa el estado asustado
        self.asustado = True
        self.velocidad = 1
        self.tiempo_asustado = time.time()

    def volver_a_posicion_inicial(self):
        # Envía al fantasma a la trampa
        # Y reiniciar estado
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


    def usar_portal(self, x, y):
        # Comprueba si el personaje está cerca de un portal y lo transporta al otro lado.
        if (x, y) in PORTALES:
            x, y = PORTALES[(x, y)]
            return x, y
        return False


    def perseguir_un_objetivo(self, bloque, objetivo_x, objetivo_y):
        # El fantasma persigue a un objetivo.
        # Obtener celdas de destino y elegir la mejor
        direcciones = {
            "ARRIBA": (self.x, self.y - self.velocidad),
            "ABAJO": (self.x, self.y + self.velocidad),
            "IZQUIERDA": (self.x - self.velocidad, self.y),
            "DERECHA": (self.x + self.velocidad, self.y),
        }

        mejor_direccion = None
        menor_distancia = 400 # Es lo que mide la pantalla por tanto es la maxima dirección
        objetivo = (objetivo_x, objetivo_y)

        for direccion in direcciones:
            nueva_x, nueva_y = direcciones[direccion]
            if not bloque.colision(nueva_x, nueva_y) and direccion != self.invertir_direccion():
                distancia = abs(nueva_x - objetivo[0]) + abs(nueva_y - objetivo[1])
                if distancia < menor_distancia:
                    menor_distancia = distancia
                    mejor_direccion = direccion

        # Mueve al fantasma en la mejor dirección encontrada
        if mejor_direccion:
            self.mover_fantasma(bloque, mejor_direccion)
        else:
            # Si no hay una mejor dirección, moverse en la dirección opuesta
            direccion_opuesta = self.invertir_direccion()
            if direccion_opuesta:
                self.mover_fantasma(bloque, direccion_opuesta)


    def mover_fantasma(self, bloque, direccion):
        # Mueve al fantasma en la dirección si no hay colisión.
        if direccion == "ARRIBA" and not bloque.colision(self.x, self.y - self.velocidad):
            self.y -= self.velocidad
            self.direccion_actual = "ARRIBA"
        elif direccion == "ABAJO" and not bloque.colision(self.x, self.y + self.velocidad):
            self.y += self.velocidad
            self.direccion_actual = "ABAJO"
        elif direccion == "IZQUIERDA" and not bloque.colision(self.x - self.velocidad, self.y):
            self.x -= self.velocidad
            self.direccion_actual = "IZQUIERDA"
        elif direccion == "DERECHA" and not bloque.colision(self.x + self.velocidad, self.y):
            self.x += self.velocidad
            self.direccion_actual = "DERECHA"

        # Portales: si el fantasma entra en un portal, salir por el otro lado del mapa
        self.ultima_direccion = direccion

    
    def invertir_direccion(self):
        # Devuelve la posicion opueta a la actual en la que esta el fantasma
        if self.direccion_actual == "DERECHA":
            return "IZQUIERDA"
        elif self.direccion_actual == "IZQUIERDA":
            return "DERECHA"
        elif self.direccion_actual == "ARRIBA":
            return "ABAJO"
        elif self.direccion_actual == "ABAJO":
            return "ARRIBA"
        else: 
            return None


    def calcular_emboscada(self, pacman, bloque):
        # Tamaño de cada celda
        celda_tamaño = 16
        # Calcular la posicion delante del pacman en funcion de la dirrecion de donde se encuentra
        if pacman.direccion_actual == "ARRIBA":
            objetivo_x = pacman.x
            objetivo_y = pacman.y - self.celdas_para_emboscada * celda_tamaño
        elif pacman.direccion_actual == "ABAJO":
            objetivo_x = pacman.x
            objetivo_y = pacman.y + self.celdas_para_emboscada * celda_tamaño
        elif pacman.direccion_actual == "IZQUIERDA":
            objetivo_x = pacman.x - self.celdas_para_emboscada * celda_tamaño
            objetivo_y = pacman.y 
        elif pacman.direccion_actual == "DERECHA":
            objetivo_x = pacman.x + self.celdas_para_emboscada * celda_tamaño
            objetivo_y = pacman.y 
        else:
            # Si no hay una direcciona valida, seguira al pacman
            return pacman.x, pacman.y
        
        # Verifica si la posicion calculada no tiene colision y se encuentra dentro del mapa
        if not bloque.colision(objetivo_x, objetivo_y):
            return objetivo_x, objetivo_y
        
        # Si la posicion no es valida simplemente seguira al pacman
        return pacman.x, pacman.y
    

    def calcular_objectivo_mas_lejano(self, pacman, bloque):

        pacman_x, pacman_y = pacman.x, pacman.y
        # Varibles de las distancia maxima y la posicion más lejana
        distancia_maxima = -1

        # Podibles direccionede los fantasmas
        direcciones = {
            "ARRIBA": (self.x, self.y - self.velocidad),
            "ABAJO": (self.x, self.y + self.velocidad),
            "IZQUIERDA": (self.x - self.velocidad, self.y),
            "DERECHA": (self.x + self.velocidad, self.y),
        }

        # Comprobar todas las celdas del mapa 
        for direccion in direcciones:
            # Vemos si la celda no tiene colision
            nueva_x, nueva_y = direcciones[direccion]
            if not bloque.colision(nueva_x, nueva_y):
                # Calculamos la distancia entre la celda y pacman
                distancia = abs(nueva_x - pacman_x) + abs(nueva_y - pacman_y)
                # Actualizamos si la distancia es mayor
                if distancia > distancia_maxima:
                    distancia_maxima = distancia
                    posicion_para_alejarse = (nueva_x, pacman_y)
        # Devuelve la posicion mas lejana                
        return posicion_para_alejarse


# Subclases de Fantasma
class FantasmaRojo(Fantasma):
    def __init__(self, x, y):
        super().__init__(x, y, FANTASMA_ROJO)

    def mover(self,bloque,pacman):
    
         # Fantasma rojo: persigue a Pac-Man
        if bloque.victoria or pacman.en_muerte:
            return False # Si se ha ganado o pacman esta muerto, no se mueve
        
        if self.en_trampa:
            return True # Si esta en la trampa, se rige por el movimiento de salida

        elif self.asustado:
            # Si esta asustado, se aleja del pacman
            objetivo_x, objetivo_y = self.calcular_objectivo_mas_lejano(pacman, bloque)
            self.perseguir_un_objetivo(bloque, objetivo_x, objetivo_y)

        else:
            self.perseguir_un_objetivo(bloque, pacman.x, pacman.y) # seguir a pacman directamente

       
class FantasmaRosa(Fantasma):
    def __init__(self, x, y):
        super().__init__(x, y, FANTASMA_ROSA)

    def mover(self,bloque,pacman):
        if bloque.victoria or pacman.en_muerte:
            return False # Si se ha ganado o pacman esta muerto, no se mueve

        if self.en_trampa:
            return True # Si esta en la trampa, se rige por el movimiento de salida

        elif self.asustado:
            # Si esta asustado, se aleja del pacman
            objetivo_x, objetivo_y = self.calcular_objectivo_mas_lejano(pacman, bloque)
            self.perseguir_un_objetivo(bloque, objetivo_x, objetivo_y)

        else:
            # Si no esta asustado, se embosca al pacman
            objetivo_x, objetivo_y = self.calcular_emboscada(pacman, bloque)
            self.perseguir_un_objetivo(bloque, objetivo_x, objetivo_y)


class FantasmaAzul(Fantasma):
    def __init__(self, x, y):
        # Inicializa al Fantasma Azul
        super().__init__(x, y, FANTASMA_AZUL)

    def mover(self,bloque,pacman):
        if bloque.victoria or pacman.en_muerte:
            return False
        
        if self.en_trampa:
            return True

        elif self.asustado:
            objetivo_x, objetivo_y = self.calcular_objectivo_mas_lejano(pacman, bloque)
            self.perseguir_un_objetivo(bloque, objetivo_x, objetivo_y)

        else:
            if time.time() - 10 >= 10: # Cada 10s se cambia el modo del fantasma
                modo = random.choice(["emboscada", "alejarse"])
                if modo == "emboscada":
                    objetivo_x, objetivo_y = self.calcular_emboscada(pacman, bloque)
                    self.perseguir_un_objetivo(bloque, objetivo_x, objetivo_y)
                else:
                    objetivo_x, objetivo_y = self.calcular_objectivo_mas_lejano(pacman, bloque)
                    self.perseguir_un_objetivo(bloque, objetivo_x, objetivo_y)


class FantasmaNaranja(Fantasma):
    def __init__(self, x, y):
        # Inicializa al Fantasma Naranja
        super().__init__(x, y, FANTASMA_NARANJA)

    def mover(self,bloque, pacman):
        if bloque.victoria or pacman.en_muerte:
            return False
        
        if self.en_trampa:
            return True

        elif self.asustado:
            objetivo_x, objetivo_y = self.calcular_objectivo_mas_lejano(pacman, bloque) 
            self.perseguir_un_objetivo(bloque, objetivo_x, objetivo_y)# alejarse de pacman

        else:
            if time.time() - 10 >= 10: # Cada 10s se cambia el modo del self
                modo = random.choice(["perseguir", "alejarse"])
                if modo == "perseguir":
                    self.perseguir_un_objetivo(bloque, pacman.x, pacman.y)
                else:
                    objetivo_x, objetivo_y = self.calcular_objectivo_mas_lejano(pacman, bloque )
                    self.perseguir_un_objetivo(bloque, objetivo_x, objetivo_y)

    
from constantes import *
import pyxel


class Pacman:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidad = 3  # Velocidad de movimiento
        self.direccion_actual = PACMAN  # Dirección inicial
        self.direccion_pendiente = None  # Dirección elegida por el jugador
        self.vidas = 3  # Pac-Man empieza con 3 vidas
        self.animacion_frame = 0
        self.en_muerte = False  # Indica si Pac-Man está en animación de muerte
        self.reiniciando = False  # Estado para evitar colisiones durante el reinicio
        self.fantasmas_comido = False
        self.mostrar_puntos = False
        self.texto_tiempo_inicio = 0
        self.posicion_fantasma_comido_x,self.posicion_fantasma_comido_y = None, None
        self.animacion_muerte_finalizada = False # Controlar la animación de muerte final de Pac-Man
         
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
    def direccion_actual(self):
        return self.__direccion_actual

    @property
    def direccion_pendiente(self):
        return self.__direccion_pendiente

    @property
    def vidas(self):
        return self.__vidas

    @property
    def animacion_frame(self):
        return self.__animacion_frame
    
    @property
    def en_muerte(self):
        return self.__en_muerte
    
    @property
    def reiniciando(self):
        return self.__reiniciando
    
    @property
    def texto_tiempo_inicio(self):
        return self.__texto_tiempo_inicio
    
    @property
    def fantasmas_comido(self):
        return self.__fantasmas_comido
    
    @property
    def mostrar_puntos(self):
        return self.__mostrar_puntos

    @property
    def posicion_fantasma_comido_x(self):
        return self.__posicion_fantasma_comido_x

    @property
    def posicion_fantasma_comido_y(self):
        return self.__posicion_fantasma_comido_y

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

    @direccion_actual.setter
    def direccion_actual(self, nuevo_valor):
        self.__direccion_actual = nuevo_valor

    @direccion_pendiente.setter
    def direccion_pendiente(self, nuevo_valor):
        self.__direccion_pendiente = nuevo_valor

    @vidas.setter
    def vidas(self, nuevo_valor):
        self.__vidas = nuevo_valor

    @animacion_frame.setter
    def animacion_frame(self, nuevo_valor):
        self.__animacion_frame = nuevo_valor

    @en_muerte.setter
    def en_muerte(self, nuevo_valor):
        self.__en_muerte = nuevo_valor

    @reiniciando.setter
    def reiniciando(self, nuevo_valor):
        self.__reiniciando = nuevo_valor

    @fantasmas_comido.setter
    def fantasmas_comido(self, nuevo_valor):
        self.__fantasmas_comido = nuevo_valor

    @mostrar_puntos.setter
    def mostrar_puntos(self, nuevo_valor):
        self.__mostrar_puntos = nuevo_valor

    @texto_tiempo_inicio.setter
    def texto_tiempo_inicio(self, nuevo_valor):
        self.__texto_tiempo_inicio = nuevo_valor

    @posicion_fantasma_comido_x.setter
    def posicion_fantasma_comido_x(self, nuevo_valor):
        self.__posicion_fantasma_comido_x = nuevo_valor

    @posicion_fantasma_comido_y.setter
    def posicion_fantasma_comido_y(self, nuevo_valor):
        self.__posicion_fantasma_comido_y = nuevo_valor

#--------------------------------------------------------------------METODOS PROPIOS--------------------------------------------------------------------# 

    def draw(self):
        if self.vidas <= 0:  # Si no hay vidas, no se dibuja
            return
        else:
            if pyxel.frame_count // REFRESH % 2 == 0:
                sprite_x, sprite_y = self.direccion_actual
            else:
                if self.direccion_actual == PACMAN_ARRIBA:
                    sprite_x, sprite_y = PACMAN_ARRIBA_CERRADA
                elif self.direccion_actual == PACMAN_ABAJO:
                    sprite_x, sprite_y = PACMAN_ABAJO_CERRADA
                elif self.direccion_actual == PACMAN_IZQUIERDA:
                    sprite_x, sprite_y = PACMAN_IZQUIERDA_CERRADA
                elif self.direccion_actual == PACMAN_DERECHA:
                    sprite_x, sprite_y = PACMAN_DERECHA_CERRADA
                else:
                    sprite_x, sprite_y = PACMAN
            # Dibujar Pac-Man
            pyxel.blt(self.x, self.y, 0, sprite_x, sprite_y, 16, 16, colkey=0)

            # Dibujar vidas
            self.ver_vidas(10, 10)

    def perder_vida(self):
        self.vidas -= 1
        self.en_muerte = True
        self.animacion_frame = 0
        self.reiniciando = True  # Activar estado de reinicio


    def ver_vidas(self, x, y):
        # Dibujar las vidas restantes
        sprite_x, sprite_y = PACMAN
        sprite_w, sprite_h = 16, 16
        pos_x = x
        for i in range(self.vidas):
            pyxel.blt(pos_x, y, 0, sprite_x, sprite_y, sprite_w, sprite_h, colkey=0)
            pos_x += sprite_w + 2


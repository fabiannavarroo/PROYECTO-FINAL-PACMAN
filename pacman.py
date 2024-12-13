from constantes import *
import pyxel


class Pacman:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidad = 2  # Velocidad de movimiento
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

    def movimineto_pacman(self,bloque):
        # Actualiza la posición de Pac-Man según las teclas presionadas y evita colisiones
        if self.vidas <= 0 or self.en_muerte or self.reiniciando:
            return False

        nueva_x, nueva_y = self.x, self.y

        # Leer las teclas para cambiar dirección
        if pyxel.btnp(pyxel.KEY_UP):
            self.direccion_pendiente = PACMAN_ARRIBA
        elif pyxel.btnp(pyxel.KEY_DOWN):
            self.direccion_pendiente = PACMAN_ABAJO
        elif pyxel.btnp(pyxel.KEY_LEFT):
            self.direccion_pendiente = PACMAN_IZQUIERDA
        elif pyxel.btnp(pyxel.KEY_RIGHT):
            self.direccion_pendiente = PACMAN_DERECHA
        elif pyxel.btnp(pyxel.KEY_W):
            self.direccion_pendiente = PACMAN_ARRIBA
        elif pyxel.btnp(pyxel.KEY_S):
            self.direccion_pendiente = PACMAN_ABAJO
        elif pyxel.btnp(pyxel.KEY_A):
            self.direccion_pendiente = PACMAN_IZQUIERDA
        elif pyxel.btnp(pyxel.KEY_D):
            self.direccion_pendiente = PACMAN_DERECHA

        # Comprobar si la dirección pendiente se puede usar es decir no hay colisión
        if self.direccion_pendiente:
            if self.direccion_pendiente == PACMAN_ARRIBA and not bloque.colision(self.x, self.y - self.velocidad):
                self.direccion_actual = self.direccion_pendiente
            elif self.direccion_pendiente == PACMAN_ABAJO and not bloque.colision(self.x, self.y + self.velocidad):
                self.direccion_actual = self.direccion_pendiente
            elif self.direccion_pendiente == PACMAN_IZQUIERDA and not bloque.colision(self.x - self.velocidad, self.y):
                self.direccion_actual = self.direccion_pendiente
            elif self.direccion_pendiente == PACMAN_DERECHA and not bloque.colision(self.x + self.velocidad, self.y):
                self.direccion_actual = self.direccion_pendiente

        # Mover Pac-Man en la dirección actual si no hay colisión
        if self.direccion_actual == PACMAN_ARRIBA:
            nueva_y -= self.velocidad
        elif self.direccion_actual == PACMAN_ABAJO:
            nueva_y += self.velocidad
        elif self.direccion_actual == PACMAN_IZQUIERDA:
            nueva_x -= self.velocidad
        elif self.direccion_actual == PACMAN_DERECHA:
            nueva_x += self.velocidad

        # Comprobar colisiones con muros
        if not bloque.colision(nueva_x, self.y):
            self.x = nueva_x
        if not bloque.colision(self.x, nueva_y):
            self.y = nueva_y

        # Portales: si Pac-Man entra en un portal, salir por el otro lado del mapa
        if self.usar_portal(self.x, self.y):
            return True

        print("Pacman", self.x, self.y)


    def usar_portal(self, x, y):
        # Comprueba si el personaje está cerca de un portal y lo transporta al otro lado.
        if (x, y) in PORTALES:
            x, y = PORTALES[(x, y)]
            return True
        return False
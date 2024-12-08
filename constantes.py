#---------PACMAN---------#
PACMAN = (0, 0)  # Coordenadas de Pacman
PACMAN_ARRIBA = (48, 0)  # Coordenadas de Pacman al moverse arriba
PACMAN_ARRIBA_CERRADA = (64, 16) # por la orientación con la cornamenta
PACMAN_ABAJO = (16, 32)  # Coordenadas de Pacman al moverse abajo
PACMAN_ABAJO_CERRADA = (80, 16) # por la orientación con la cornamenta
PACMAN_IZQUIERDA = (32, 0)  # Coordenadas de Pacman al moverse a la izquierda
PACMAN_IZQUIERDA_CERRADA = (80, 0) # por la orientación con la cornamenta
PACMAN_DERECHA = (16, 0)  # Coordenadas de Pacman al moverse a la derecha
PACMAN_DERECHA_CERRADA = (64, 0) # por la orientación con la cornamenta
ANIMACION_MUERTE = (
    (0, 0), (0, 16), (16, 16), (32, 16),(48,32),(64,32))  # animacion de la muerte del pacman

#---------FANTASMAS---------# 
FANTASMA_ROJO = {
    "ARRIBA": (48, 64), # Coordenadas del fantasma rojo al moverse arriba
    "ABAJO": (0, 64),  # Coordenadas del fantasma rojo al moverse abajo
    "IZQUIERDA": (16, 64), # Coordenadas del fantasma rojo al moverse a la izquierda
    "DERECHA": (32, 64)  # Coordenadas del fantasma rojo al moverse a la derecha
}
FANTASMA_ROSA = {
    "ARRIBA": (48, 96), # Coordenadas del fantasma rosa al moverse arriba
    "ABAJO": (0, 96),  # Coordenadas del fantasma rosa al moverse abajo
    "IZQUIERDA": (16, 96),  # Coordenadas del fantasma rosa al moverse a la izquierda
    "DERECHA": (32, 96) # Coordenadas del fantasma rosa al moverse a la derecha
}
FANTASMA_AZUL = {
    "ARRIBA": (48, 48), # Coordenadas del fantasma azul al moverse arriba
    "ABAJO": (0, 48), # Coordenadas del fantasma azul al moverse abajo
    "IZQUIERDA": (16, 48), # Coordenadas del fantasma azul al moverse a la izquierda
    "DERECHA": (32, 48)  # Coordenadas del fantasma azul al moverse a la derecha
}
FANTASMA_NARANJA = {
    "ARRIBA": (48, 80), # Coordenadas del fantasma naranja al moverse arriba
    "ABAJO": (0, 80), # Coordenadas del fantasma naranja al moverse abajo
    "IZQUIERDA": (16, 80), # Coordenadas del fantasma naranja al moverse a la izquierda
    "DERECHA": (32, 80) # Coordenadas del fantasma naranja al moverse a la derecha
}

FANTASMAS_ASUSTADOS = {
    "AZUL": {"Coordenadas": (0,112), "Tamaño": (16, 16)},
    "BLANCO": {"Coordenadas": (16, 112), "Tamaño": (16, 16)}
}

#--------PUNTOS Y FRUTAS---------#
OBJETOS = {
    "BASTON": {"Coordenadas": (48,16), "Puntos": 10}, 
    "REGALO": {"Coordenadas": (0,32), "Puntos": 15}, 
    "REGALO_BRILLANTE": {"Coordenadas": (32,32), "Puntos": 15}, 
    "CEREZA" : {"Coordenadas": (0, 128), "Puntos": 20}, 
    "FRESA" : {"Coordenadas":(16, 128), "Puntos": 30}, 
    "NARANJA" : {"Coordenadas":(32, 128), "Puntos": 40}, 
    "MANZANA" : {"Coordenadas":(48, 128), "Puntos": 50}, 
    "MELON" : {"Coordenadas":(0, 144), "Puntos": 60}, 
    "PARAGUAS" : {"Coordenadas":(16, 144), "Puntos": 100}, 
    "CAMPANA" : {"Coordenadas":(32, 144), "Puntos": 120}, 
    "LLAVE" : {"Coordenadas":(48, 144), "Puntos": 140}, 
    }

#-----------PORTALES-----------#
PORTALES={
    (-14,208):(402,208), # Portal izquierda
    (402,208):(-14,208),  # Portal derecha
    (-14, 144):(410, 144) # Portal izquierda
}

#---------------TEXTO--------------#
TEXTO={
    "READY!": {"Coordenadas": (32, 192), "Tamaño": (64, 16)}, 
    "HIGHSCORE":{"Coordenadas": (0, 168), "Tamaño": (80, 16)}, 
    "GAME OVER": {"Coordenadas": (0, 192), "Tamaño": (32, 24)}, 
}


#--------NÚMEROS--------#
NUMEROS_BLANCOS={
    "0": {"Coordenadas": (0, 216), "Tamaño": (8, 8)},
    "1": {"Coordenadas": (8, 216), "Tamaño": (8, 8)},
    "2": {"Coordenadas": (16, 216), "Tamaño": (8, 8)},
    "3": {"Coordenadas": (24, 216), "Tamaño": (8, 8)},
    "4": {"Coordenadas": (32, 216), "Tamaño": (8, 8)},
    "5": {"Coordenadas": (40, 216), "Tamaño": (8, 8)},
    "6": {"Coordenadas": (48, 216), "Tamaño": (8, 8)},
    "7": {"Coordenadas": (56, 216), "Tamaño": (8, 8)},
    "8": {"Coordenadas": (64, 216), "Tamaño": (8, 8)},
    "9": {"Coordenadas": (72, 216), "Tamaño": (8, 8)},
}
NUMEROS_NARANJAS={
    "0": {"Coordenadas": (0, 224), "Tamaño": (8, 8)},
    "1": {"Coordenadas": (8, 224), "Tamaño": (8, 8)},
    "2": {"Coordenadas": (16, 224), "Tamaño": (8, 8)},
    "3": {"Coordenadas": (24, 224), "Tamaño": (8, 8)},
    "4": {"Coordenadas": (32, 224), "Tamaño": (8, 8)},
    "5": {"Coordenadas": (40, 224), "Tamaño": (8, 8)},
    "6": {"Coordenadas": (48, 224), "Tamaño": (8, 8)},
    "7": {"Coordenadas": (56, 224), "Tamaño": (8, 8)},
    "8": {"Coordenadas": (64, 224), "Tamaño": (8, 8)},
    "9": {"Coordenadas": (72, 224), "Tamaño": (8, 8)},
}
NUMEROS_VERDES={
    "0": {"Coordenadas": (0, 232), "Tamaño": (8, 8)},
    "1": {"Coordenadas": (8, 232), "Tamaño": (8, 8)},
    "2": {"Coordenadas": (16, 232), "Tamaño": (8, 8)},
    "3": {"Coordenadas": (24, 232), "Tamaño": (8, 8)},
    "4": {"Coordenadas": (32, 232), "Tamaño": (8, 8)},
    "5": {"Coordenadas": (40, 232), "Tamaño": (8, 8)},
    "6": {"Coordenadas": (48, 232), "Tamaño": (8, 8)},
    "7": {"Coordenadas": (56, 232), "Tamaño": (8, 8)},
    "8": {"Coordenadas": (64, 232), "Tamaño": (8, 8)},
    "9": {"Coordenadas": (72, 232), "Tamaño": (8, 8)},
}
NUMEROS_MORADOS={
    "0": {"Coordenadas": (0, 240), "Tamaño": (8, 8)},
    "1": {"Coordenadas": (8, 240), "Tamaño": (8, 8)},
    "2": {"Coordenadas": (16, 240), "Tamaño": (8, 8)},
    "3": {"Coordenadas": (24, 240), "Tamaño": (8, 8)},
    "4": {"Coordenadas": (32, 240), "Tamaño": (8, 8)},
    "5": {"Coordenadas": (40, 240), "Tamaño": (8, 8)},
    "6": {"Coordenadas": (48, 240), "Tamaño": (8, 8)},
    "7": {"Coordenadas": (56, 240), "Tamaño": (8, 8)},
    "8": {"Coordenadas": (64, 240), "Tamaño": (8, 8)},
    "9": {"Coordenadas": (72, 240), "Tamaño": (8, 8)},
}

#--------OTROS---------#
REFRESH = 4
REFRESH_REGALOS = 35
TEXTO_MUERTE = ["Te has quedado sin vidas", "(ESC)Salir"]
ZONAS_PROHIBIDAS_MAPA_1 = [(0,0,384,16), (112,160,272,256),(32,64,64,96),(96,64,160,96), (224,64,288,96),
                           (320,64,352,96), (0,160,80, 256), (304, 160,384, 256),(192, 304,192, 304)]
ZONAS_PROHIBIDAS_MAPA_2 = [(0,0,384,16),(112,160,272,256),(0,160,80, 256),]
ZONAS_PROHIBIDAS = {1: ZONAS_PROHIBIDAS_MAPA_1, 2: ZONAS_PROHIBIDAS_MAPA_2} # Zonas prohibidas para generar puntos

#-----BLOQUES--------#

#BLOQUES NIVEL 1
SPRITE_BLOQUE_1 = (0,0,1,16,16) # Esquina izquierda horizontal
SPRITE_BLOQUE_2 = (8,0,1,16,16) # Borde horizontal
SPRITE_BLOQUE_3 = (16,0,1,16,16) # Esquina derecha horizontal
SPRITE_BLOQUE_4 = (48,0,1,16,16) # Esquina superior vertical
SPRITE_BLOQUE_5 = (48,8,1,16,16) # Borde vertical
SPRITE_BLOQUE_6 = (48,16,1,16,16) # Esquina inferior vertical
SPRITE_BLOQUE_7 = (0,16,1,16,16) # Cruce en T hacia abajo
SPRITE_BLOQUE_8 = (16,16,1,16,16) # Cruce en T hacia arriba
SPRITE_BLOQUE_9 = (32,16,1,16,16) # Cruce en T hacia derecha
SPRITE_BLOQUE_10 = (32,32,1,16,16) # Cruce en T hacia izquierda
SPRITE_BLOQUE_11 = (0,32,1,16,16) # Borde esquina superior izquieda
SPRITE_BLOQUE_12 = (16,32,1,16,16) # Borde esquina superior derecha
SPRITE_BLOQUE_13 = (0,48,1,16,16) #  Borde esquina inferior izquieda
SPRITE_BLOQUE_14 = (16,48,1,16,16) # Borde esquina inferior derecha
SPRITE_BLOQUE_15 = (8,72,1,16,16) # Esquina izquierda superior trampa fantasmas
SPRITE_BLOQUE_16 = (24,72,1,16,16) # Puerta salida de fantasmas
SPRITE_BLOQUE_17 = (40,72,1,16,16) # Esquina derecha superior trampa fantasmas
SPRITE_BLOQUE_18 = (8,88,1,16,16) # Esquina izquierda inferior trampa fantasmas
SPRITE_BLOQUE_19 = (32,56,1,16,16) # Borde superior trampa fantasma
SPRITE_BLOQUE_20 = (40,88,1,16,16) # Esquina derecha inferior trampa fantasmas
SPRITE_BLOQUE_21 = (8,80,1,16,16) # Borde derecha trampa fantasmas
SPRITE_BLOQUE_22 = (40,80,1,16,16) # Borde izquierda trampa fantasmas
SPRITE_BLOQUE_23 = (24,88,1,16,16) # Borde inferior trampa fantasma

#BLOQUES NIVEL 2
SPRITE_BLOQUE_1_1 = (80,0,1,16,16) # Esquina izquierda horizontal
SPRITE_BLOQUE_2_1 = (88,0,1,16,16) # Borde horizontal
SPRITE_BLOQUE_3_1 = (96,0,1,16,16) # Esquina derecha horizontal
SPRITE_BLOQUE_4_1 = (64,0,1,16,16) # Esquina superior vertical
SPRITE_BLOQUE_5_1 = (64,8,1,16,16) # Borde vertical
SPRITE_BLOQUE_6_1 = (64,16,1,16,16) # Esquina inferior vertical
SPRITE_BLOQUE_7_1 = (88,16,1,16,16) # Cruce en T hacia abajo
SPRITE_BLOQUE_8_1 = (104,16,1,16,16) # Cruce en T hacia arriba
SPRITE_BLOQUE_9_1 = (120,16,1,16,16) # Cruce en T hacia derecha
SPRITE_BLOQUE_10_1 = (120,32,1,16,16) # Cruce en T hacia izquierda
SPRITE_BLOQUE_11_1 = (80,40,1,16,16) # Borde esquina superior izquieda
SPRITE_BLOQUE_12_1 = (96,40,1,16,16) # Borde esquina superior derecha
SPRITE_BLOQUE_13_1 = (80,56,1,16,16) #  Borde esquina inferior izquieda
SPRITE_BLOQUE_14_1 = (96,56,1,16,16) # Borde esquina inferior derecha
SPRITE_BLOQUE_15_1 = (80,72,1,16,16) # Esquina izquierda superior trampa fantasmas
SPRITE_BLOQUE_16_1 = (96,72,1,16,16) # Puerta salida de fantasmas
SPRITE_BLOQUE_17_1 = (112,72,1,16,16) # Esquina derecha superior trampa fantasmas
SPRITE_BLOQUE_18_1 = (80,88,1,16,16) # Esquina izquierda inferior trampa fantasmas
SPRITE_BLOQUE_19_1 = (112,56,1,16,16) # Borde superior trampa fantasma
SPRITE_BLOQUE_20_1 = (112,88,1,16,16) # Esquina derecha inferior trampa fantasmas
SPRITE_BLOQUE_21_1 = (80,80,1,16,16) # Borde izquierda trampa fantasmas 
SPRITE_BLOQUE_22_1 = (112,80,1,16,16) # Borde derecha trampa fantasmas
SPRITE_BLOQUE_23_1 = (96,88,1,16,16) # Borde inferior trampa fantasma

#-----MAPA--------#
MAPA_1 = [
    # fila 1
    (0, 32, 11),      # Esquina superior izquierda
    (16, 32, 2),     # Borde horizontal
    (32, 32, 2),     # Borde horizontal
    (48, 32, 2),     # Borde horizontal
    (64, 32, 2),     # Borde horizontal
    (80, 32, 2),     # Borde horizontal
    (96, 32, 2),     # Borde horizontal
    (112, 32, 2),     # Borde horizontal
    (128, 32, 2),     # Borde horizontal
    (144, 32, 2),     # Borde horizontal
    (160, 32, 2),     # Borde horizontal
    (176, 32, 2),     # Borde horizontal
    (192, 32, 7),     # Cruce en T hacia abajo
    (208, 32, 2),     # Borde horizontal
    (224, 32, 2),     # Borde horizontal
    (240, 32, 2),     # Borde horizontal
    (256, 32, 2),     # Borde horizontal
    (272, 32, 2),     # Borde horizontal
    (288, 32, 2),     # Borde horizontal
    (304, 32, 2),     # Borde horizontal
    (320, 32, 2),     # Borde horizontal
    (336, 32, 2),     # Borde horizontal
    (352, 32, 2),     # Borde horizontal
    (368, 32, 2),     # Borde horizontal
    (384, 32, 12),     # Esquina superior derecha
    
    # Fila 2
    (0, 48, 5),      # Borde vertical
    (192, 48, 5),     # Borde vertical  
    (384, 48, 5),     # Borde vertical
    
    # fila 3
    (0, 64, 5),      # Borde vertical
    (32,64,11),      # Esquina superior izquierda
    (48,64,2),       # Borde horizontal
    (64,64,12),      # Esquina superior derecha
    (96,64,11),      # Esquina superior izquierda
    (112,64,2),      # Borde horizontal
    (128,64,2),      # Borde horizontal
    (144,64,2),      # Borde horizontal
    (160,64,12),     # Esquina superior izquierda
    (192, 64, 5),     # Borde vertical 
    (224,64,11),      # Esquina superior izquierda
    (240,64,2),       # Borde horizontal
    (256,64,2),       # Borde horizontal
    (272,64,2),       # Borde horizontal
    (288,64,12),      # Esquina superior izquierda 
    (320,64,11),      # Esquina superior izquierda
    (336,64,2),       # Borde horizontal
    (352,64,12),      # Esquina superior derecha
    (384, 64, 5),     # Esquina inferior derecha

    # fila 4
    (0, 80, 5),      # Borde vertical
    (32,80,5),      # Borde vertical
    (64,80,5),      # Borde vertical
    (96,80,5),      # Borde vertical
    (160,80,5),     # Borde vertical
    (192,80,5),     # Borde vertical
    (224,80,5),     # Borde vertical
    (288,80,5),     # Borde vertical
    (320,80,5),     # Borde vertical
    (352,80,5),     # Borde vertical
    (384,80,5),     # Borde vertical

    # fila 5
    (0, 96, 5),      # Borde vertical
    (32,96,13),      # Esquina izquierda inferior
    (48,96,2),       # Borde horizontal
    (64,96,14),      # Esquina derecha inferior
    (96,96,13),      # Esquina izquierda inferior
    (112,96,2),      # Borde horizontal
    (128,96,2),      # Borde horizontal
    (144,96,2),      # Borde horizontal
    (160,96,14),     # Esquina derecha inferior
    (192, 96, 6),     # Esquina inferior vertical
    (224,96,13),      # Esquina inferior izquierda
    (240,96,2),       # Borde horizontal
    (256,96,2),       # Borde horizontal
    (272,96,2),       # Borde horizontal
    (288,96,14),      # Esquina inferior izquierda
    (320,96,13),      # Esquina inferior izquierda
    (336,96,2),       # Borde horizontal
    (352,96,14),      # Esquina inferior derecha
    (384,96,5),     # Borde vertical

    # Fila 6
    (0, 112, 5),      # Borde vertical
    (384, 112, 5),     # Borde vertical

    # Fila 7
    (0, 128, 5),      # Borde vertical
    (32,128,1),      # Esquina izquierda horizontal
    (48,128,2),      # Borde horizontal
    (64,128,2),      # Borde horizontal
    (80,128,3),      # Esquina derecha horizontal
    (112,128,4),      # Esquina superior vertical
    (144,128,1),      # Esquina izquierda horizontal
    (160,128,2),      # Borde horizontal
    (176,128,2),      # Borde horizontal
    (192, 128, 7),     # Cruce en T hacia abajo
    (208,128,2),      # Borde horizontal
    (224,128,2),      # Borde horizontal
    (240,128,3),      # Esquina derecha horizontal
    (272,128,4),      # Esquina superior vertical
    (304,128,1),      # Esquina izquierda horizontal
    (320,128,2),      # Borde horizontal
    (336,128,2),      # Borde horizontal
    (352,128,3),      # Esquina derecha horizontal
    (384, 128, 5),     # Borde vertical

    # Fila 8
    (0, 144, 5),      # Borde vertical
    (112,144,5),      # Borde vertical
    (192, 144, 5),     # Borde vertical
    (272,144,5),      # Borde vertical
    (384, 144, 5),     # Borde vertical

    # Fila 9
    (0, 160, 13),      # Borde esquina inferior izquierda
    (16,160,2),      # Borde horizontal
    (32, 160, 2),     # Borde horizontal    
    (48,160,2),      # Borde horizontal
    (64, 160, 2),     # Borde horizontal
    (80, 160, 12),     # Borde esquina superior derecha
    (112, 160,9),      # Borde horizontal
    (128, 160, 2),     # Borde horizontal
    (144, 160, 2),     # Borde horizontal
    (160, 160, 3),     # Esquina derecha horizontal
    (192, 160, 6),     # Esquina inferior vertical
    (224, 160, 1),     # Esquina izquierda horizontal
    (240, 160, 2),     # Borde horizontal
    (256, 160, 2),     # Borde horizontal
    (272, 160, 10),     # Cruce en T hacia izquierda
    (304, 160, 11),     # Borde esquina superior izquierda
    (320, 160, 2),     # Borde horizontal
    (336, 160, 2),     # Borde horizontal
    (352, 160, 2),     # Borde horizontal
    (368, 160, 2),     # Borde horizontal
    (384, 160, 14),     # Borde esquina inferior derecha

    # Fila 10
    (80, 176, 5),     # Borde vertical
    (112, 176,5),      # Borde vertical
    (272, 176, 5),     # Borde vertical
    (304, 176, 5),     # Borde vertical

    # Fila 11
    (0, 192, 2),      # Borde esquina inferior izquierda
    (16,192,2),      # Borde horizontal
    (32, 192, 2),     # Borde horizontal    
    (48,192,2),      # Borde horizontal
    (64, 192, 2),     # Borde horizontal
    (80, 192, 14),     # Borde esquina inferior derecha
    (112, 192 ,6),     # Esquina inferior vertical
    (144, 192, 15),     # Esquina izquierda superior trampa fantasmas
    (160, 192, 19),     # Borde superior trampa fantasma
    (176, 192, 16),     # Puerta salida de fantasmas
    (192, 192, 16),     # Puerta salida de fantasmas
    (208, 192, 16),     # Puerta salida de fantasmas
    (224, 192, 19),     # Borde superior trampa fantasma
    (240, 192, 17),     # Esquina derecha superior trampa fantasmas
    (272, 192, 6),     # Esquina inferior vertical
    (304, 192, 13),     # Borde esquina inferior izquierda
    (320, 192, 2),     # Borde horizontal  
    (336, 192, 2),     # Borde horizontal
    (352, 192, 2),     # Borde horizontal  
    (368, 192, 2),     # Borde horizontal
    (384, 192, 2),     # Borde horizontal

    # Fila 12
    (144, 208, 21),     # Borde derecha trampa fantasmas
    (240, 208, 22),     # Borde izquierda trampa fantasmas

    # Fila 13
    (0, 224, 2),      # Borde esquina inferior izquierda
    (16,224,2),      # Borde horizontal
    (32, 224, 2),     # Borde horizontal    
    (48,224,2),      # Borde horizontal
    (64, 224, 2),     # Borde horizontal
    (80, 224, 12),     # Borde esquina superior derecha
    (112, 224, 4),     # Esquina superior vertical
    (144, 224, 18),     # Borde izquierda inferior trampa fantasma
    (160, 224, 23),     # Borde inferior trampa fantasmas
    (176, 224, 23),     # Borde inferior trampa fantasmas
    (192, 224, 23),     # Borde inferior trampa fantasmas
    (208, 224, 23),     # Borde inferior trampa fantasmas
    (224, 224, 23),     # Borde inferior trampa fantasmas
    (232, 224, 23),     # Borde inferior trampa fantasmas
    (240, 224, 20),     # Esquina derecha inferior trampa fantasmas
    (272, 224,4),     # Esquina superior vertical
    (304, 224, 11),     # Borde esquina superior izquierda
    (320, 224, 2),     # Borde horizontal
    (336, 224, 2),     # Borde horizontal
    (352, 224, 2),     # Borde horizontal
    (368, 224, 2),     # Borde horizontal
    (384, 224, 2),     # Borde horizontal
   
   # Fila 14
    (80, 240, 5),     # Borde vertical
    (112, 240,5),      # Borde vertical
    (272, 240, 5),     # Borde vertical
    (304, 240, 5),     # Borde vertical

    # Fila 15
    (0, 256, 11),      # Borde esquina inferior izquierda
    (16,256,2),      # Borde horizontal
    (32, 256, 2),     # Borde horizontal    
    (48,256,2),      # Borde horizontal
    (64, 256, 2),     # Borde horizontal
    (80, 256, 14),     # Borde esquina inferior derecha
    (112, 256 ,6),     # Esquina superior vertical
    (144, 256, 1),     # Esquina izquierda horizontal
    (160, 256, 2),     # Borde horizontal
    (176, 256, 2),     # Borde horizontal
    (192, 256, 7),     # Cruce en T hacia abajo
    (208, 256, 2),     # Borde horizontal
    (224, 256, 2),     # Borde horizontal   
    (240, 256, 3),     # Esquina derecha horizontal
    (272, 256, 6),     # Esquina inferior vertical
    (304, 256, 13),     # Borde esquina inferio izquierda
    (320, 256, 2),     # Borde horizontal  
    (336, 256, 2),     # Borde horizontal
    (352, 256, 2),     # Borde horizontal  
    (368, 256, 2),     # Borde horizontal
    (384, 256, 12),     # Borde horizontal

    # Fila 16
    (0, 272, 5),      # Borde vertical
    (192, 272, 5),     # Borde vertical  
    (384, 272, 5),     # Borde vertical

    # Fila 17
    (0, 288, 5),      # Borde vertical
    (32, 288, 1),     # Esquina izquierda horizontal
    (48, 288, 2),      # Borde horizontal
    (64, 288, 12),     # Esquina superior derecha
    (96, 288, 1),     # Esquina izquierda horizontal
    (112, 288, 2),     # Borde horizontal
    (128, 288, 2),     # Borde horizontal
    (144, 288, 2),     # Borde horizontal
    (160, 288, 3),     # Esquina inferior izquierda
    (192, 288, 6),     # Esquina inferior vertical
    (224, 288, 1),     # Esquina izquierda horizontal
    (240, 288, 2),     # Borde horizontal
    (256, 288, 2),     # Borde horizontal
    (272, 288, 2),     # Borde horizontal
    (288, 288, 3),     # Esquina inferior izquierda     
    (320, 288, 11),     # Borde horizontal
    (336, 288, 2),     # Borde horizontal
    (352, 288, 3),     # Esquina inferior izquierda
    (384, 288, 5),     # Borde vertical

    # Fila 18
    (0, 304, 5),      # Borde vertical
    (64, 304, 5),     # Borde vertical
    (320, 304, 5),     # Borde vertical
    (384, 304, 5),     # Borde vertical

    # Fila 19
    (0, 320, 9),      # Cruce en T hacia derecha
    (16, 320, 2),      # Borde horizontal
    (32, 320, 3),      # Esquina derecha horizontal
    (64, 320, 6),     # Esquina inferior vertical
    (96, 320, 4),     # Esquina superior vertical
    (128, 320, 1),     # Esquina izquierda horizontal
    (144, 320, 2),     # Borde horizontal
    (160, 320, 2),     # Borde horizontal
    (176, 320, 2),     # Borde horizontal
    (192, 320, 7),     # Cruce en T hacia abajo
    (208, 320, 2),     # Borde horizontal
    (224, 320, 2),     # Borde horizontal
    (240, 320, 2),     # Borde horizontal
    (256, 320, 3),     # Esquina derecha horizontal
    (288, 320, 4),     # Esquina superior vertical
    (320, 320, 6),     # Esquina inferior vertical
    (352, 320, 1),     # Esquina izquierda horizontal
    (368, 320, 2),     # Borde horizontal
    (384, 320, 10),     # Cruce en T hacia izquierda

    # Fila 20
    (0, 336, 5),      # Borde vertical
    (96, 336, 5),     # Borde vertical
    (192, 336, 5),     # Borde vertical
    (288, 336, 5),     # Borde vertical
    (384, 336, 5),     # Borde vertical

    # Fila 21
    (0, 352, 5),      # Borde vertical
    (32, 352, 1),     # Esquina izquierda horizontal
    (48, 352, 2),     # Borde horizontal
    (64, 352, 2),     # Borde horizontal
    (80, 352, 2),     # Borde horizontal
    (96, 352, 8),     # Cruce en T hacia arriba
    (112, 352, 2),     # Borde horizontal
    (128, 352, 2),     # Borde horizontal
    (144, 352, 2),     # Borde horizontal
    (160, 352, 3),     # Esquina derecha horizontal
    (192, 352, 6),     # Esquina inferior vertical
    (224, 352, 1),     # Esquina izquierda horizontal
    (240, 352, 2),     # Borde horizontal
    (256, 352, 2),     # Borde horizontal
    (272, 352, 2),     # Borde horizontal
    (288, 352, 8),     # Cruce en T hacia arriba
    (304, 352, 2),     # Borde horizontal
    (320, 352, 2),     # Borde horizontal
    (336, 352, 2),     # Borde horizontal
    (352, 352, 3),     # Esquina derecha horizontal
    (384, 352, 5),     # Borde vertical

    # Fila 22
    (0, 368, 5),      # Borde vertical
    (384, 368, 5),     # Borde vertical

    # Fila 23
    (0, 384, 13),     # Esquina inferior izquierda
    (16, 384, 2),     # Borde horizontal
    (32, 384, 2),     # Borde horizontal
    (48, 384, 2),     # Borde horizontal
    (64, 384, 2),     # Borde horizontal
    (80, 384, 2),     # Borde horizontal
    (96, 384, 2),     # Borde horizontal
    (112, 384, 2),     # Borde horizontal
    (128, 384, 2),     # Borde horizontal
    (144, 384, 2),     # Borde horizontal
    (160, 384, 2),     # Borde horizontal
    (176, 384, 2),     # Borde horizontal
    (192, 384, 2),     # Borde horizontal
    (208, 384, 2),     # Borde horizontal
    (224, 384, 2),     # Borde horizontal
    (240, 384, 2),     # Borde horizontal
    (256, 384, 2),     # Borde horizontal
    (272, 384, 2),     # Borde horizontal
    (288, 384, 2),     # Borde horizontal
    (304, 384, 2),     # Borde horizontal
    (320, 384, 2),     # Borde horizontal
    (336, 384, 2),     # Borde horizontal
    (352, 384, 2),     # Borde horizontal
    (368, 384, 2),     # Borde horizontal
    (384, 384, 14),     # Esquina inferior derecha
]

MAPA_2 = [
    # fila 1
    (0, 32, 11),      # Esquina superior izquierda
    (16, 32, 2),     # Borde horizontal
    (32, 32, 2),     # Borde horizontal
    (48, 32, 2),     # Borde horizontal
    (64, 32, 2),     # Borde horizontal
    (80, 32, 2),     # Borde horizontal
    (96, 32, 7),     # Cruce en T hacia abajo
    (112, 32, 2),     # Borde horizontal
    (128, 32, 2),     # Borde horizontal
    (144, 32, 2),     # Borde horizontal
    (160, 32, 2),     # Borde horizontal
    (176, 32, 2),     # Borde horizontal
    (192, 32, 7),     # Cruce en T hacia abajo
    (208, 32, 2),     # Borde horizontal
    (224, 32, 2),     # Borde horizontal
    (240, 32, 2),     # Borde horizontal
    (256, 32, 2),     # Borde horizontal
    (272, 32, 2),     # Borde horizontal
    (288, 32, 7),     # Cruce en T hacia abajo
    (304, 32, 2),     # Borde horizontal
    (320, 32, 2),     # Borde horizontal
    (336, 32, 2),     # Borde horizontal
    (352, 32, 2),     # Borde horizontal
    (368, 32, 2),     # Borde horizontal
    (384, 32, 12),     # Esquina superior derecha

    # Fila 2
    (0, 48, 5),      # Borde vertical
    (96, 48, 5),     # Borde vertical
    (192, 48, 5),     # Borde vertical
    (288, 48, 5),     # Borde vertical
    (384, 48, 5),     # Borde vertical

    # Fila 3
    (0, 64, 5),      # Borde vertical
    (32, 64, 1),     # Esquina izquierda horizontal
    (48, 64, 2),     # Borde horizontal
    (64, 64, 3),     # Esquina derecha horizontal
    (96, 64, 5),     # Borde vertical
    (128, 64, 1),     # Esquina izquierda horizontal
    (144, 64, 2),     # Borde horizontal
    (160, 64, 3),     # Esquina derecha horizontal
    (192, 64, 5),     # Borde vertical
    (224, 64, 1),     # Esquina izquierda horizontal
    (240, 64, 2),     # Borde horizontal
    (256, 64, 3),     # Esquina derecha horizontal
    (288, 64, 5),     # Borde vertical
    (320, 64, 1),     # Esquina izquierda horizontal
    (336, 64, 2),     # Borde horizontal
    (352, 64, 3),     # Esquina derecha horizontal
    (384, 64, 5),     # Borde vertical

    # Fila 4
    (0, 80, 5),      # Borde vertical
    (96, 80, 6),     # 
    (192, 80, 6),     # 
    (288, 80, 6),     # 
    (384, 80, 5),     # Borde vertical

    # Fila 5
    (0, 96, 5),      # Borde vertical
    (32, 96, 1),     # Esquina izquierda horizontal
    (48, 96, 2),     # Borde horizontal
    (64, 96, 3),     # Esquina derecha horizontal
    (128, 96, 1),     # Esquina izquierda horizontal
    (144, 96, 2),     # Borde horizontal
    (160, 96, 3),     # Esquina derecha horizontal
    (224, 96, 1),     # Esquina izquierda horizontal
    (240, 96, 2),     # Borde horizontal
    (256, 96, 3),     # Esquina derecha horizontal
    (320, 96, 1),     # Esquina izquierda horizontal
    (336, 96, 2),     # Borde horizontal
    (352, 96, 3),     # Esquina derecha horizontal
    (384, 96, 5),     # Borde vertical

    # Fila 6
    (0, 112, 5),     # Borde vertical
    (96, 112, 4),     # 
    (192, 112, 4),     # 
    (288, 112, 4),     # 
    (384, 112, 5),     # Borde vertical

    # Fila 7
    (0, 128, 8),     # Borde vertical
    (16, 128, 2),     # Borde horizontal
    (32, 128, 3),     # Esquina derecha horizontal
    (64, 128, 1),     # 
    (80, 128, 2),     # 
    (96, 128, 8),     # Esquina izquierda horizontal
    (112, 128, 2),     # Borde horizontal
    (128, 128, 3),     
    (160, 128, 1),     # 
    (176, 128, 2),     # 
    (192, 128, 8),     # 
    (208, 128, 2),     # Esquina izquierda horizontal
    (224, 128, 3),     # Borde horizontal
    (256, 128, 1),     # 
    (272, 128, 2),     # Borde horizontal
    (288, 128, 8),     # Esquina izquierda horizontal
    (304, 128, 2),     # Borde horizontal
    (320, 128, 3),     # Esquina derecha horizontal
    (352, 128, 1),     # Borde horizontal
    (368, 128, 2),     # Esquina derecha horizontal
    (384, 128, 8),     # Borde vertical

    # fila 8
    #ta vacia

    # fila 9
    (0, 160, 2),      # Borde esquina inferior izquierda
    (16,160,2),      # Borde horizontal
    (32, 160, 2),     # Borde horizontal    
    (48,160,2),      # Borde horizontal
    (64, 160, 2),     # Borde horizontal
    (80, 160, 12),     # Borde esquina inferior derecha
    (112, 160, 4),     # Esquina sueprior vertical
    (144,160,1),
    (160,160,2),
    (176,160,3),
    (208,160,1),
    (224,160,2),
    (240,160,3),
    (272,160,4),
    (304,160,11),
    (320,160,2),
    (336,160,2),
    (352,160,2),
    (368,160,2),
    (384,160,2),
    
    # Fila 10
    (80, 176, 5),     # Borde vertical
    (112, 176,5),      # Borde vertical
    (272, 176, 5),     # Borde vertical
    (304, 176, 5),     # Borde vertical

    # Fila 11
    (0, 192, 2),      # Borde esquina inferior izquierda
    (16,192,2),      # Borde horizontal
    (32, 192, 2),     # Borde horizontal    
    (48,192,2),      # Borde horizontal
    (64, 192, 2),     # Borde horizontal
    (80, 192, 14),     # Borde esquina inferior derecha
    (112, 192 ,6),     # Esquina inferior vertical
    (144, 192, 15),     # Esquina izquierda superior trampa fantasmas
    (160, 192, 19),     # Borde superior trampa fantasma
    (176, 192, 16),     # Puerta salida de fantasmas
    (192, 192, 16),     # Puerta salida de fantasmas
    (208, 192, 16),     # Puerta salida de fantasmas
    (224, 192, 19),     # Borde superior trampa fantasma
    (240, 192, 17),     # Esquina derecha superior trampa fantasmas
    (272, 192, 6),     # Esquina inferior vertical
    (304, 192, 13),     # Borde esquina inferior izquierda
    (320, 192, 2),     # Borde horizontal  
    (336, 192, 2),     # Borde horizontal
    (352, 192, 2),     # Borde horizontal  
    (368, 192, 2),     # Borde horizontal
    (384, 192, 2),     # Borde horizontal

    # Fila 12
    (144, 208, 21),     # Borde derecha trampa fantasmas
    (240, 208, 22),     # Borde izquierda trampa fantasmas

    # Fila 13
    (0, 224, 2),      # Borde esquina inferior izquierda
    (16,224,2),      # Borde horizontal
    (32, 224, 2),     # Borde horizontal    
    (48,224,2),      # Borde horizontal
    (64, 224, 2),     # Borde horizontal
    (80, 224, 12),     # Borde esquina superior derecha
    (112, 224, 4),     # Esquina superior vertical
    (144, 224, 18),     # Borde izquierda inferior trampa fantasma
    (160, 224, 23),     # Borde inferior trampa fantasmas
    (176, 224, 23),     # Borde inferior trampa fantasmas
    (192, 224, 23),     # Borde inferior trampa fantasmas
    (208, 224, 23),     # Borde inferior trampa fantasmas
    (224, 224, 23),     # Borde inferior trampa fantasmas
    (232, 224, 23),     # Borde inferior trampa fantasmas
    (240, 224, 20),     # Esquina derecha inferior trampa fantasmas
    (272, 224,4),     # Esquina superior vertical
    (304, 224, 11),     # Borde esquina superior izquierda
    (320, 224, 2),     # Borde horizontal
    (336, 224, 2),     # Borde horizontal
    (352, 224, 2),     # Borde horizontal
    (368, 224, 2),     # Borde horizontal
    (384, 224, 2),     # Borde horizontal
   
   # Fila 14
    (80, 240, 5),     # Borde vertical
    (112, 240,5),      # Borde vertical
    (272, 240, 5),     # Borde vertical
    (304, 240, 5),     # Borde vertical

    # Fila 15
    (0, 256, 11),     #
    (16, 256, 2),     #
    (32, 256, 2),     #
    (48, 256, 2),     #
    (64, 256, 2),     #
    (80, 256, 14),     #
    (112, 256, 6),     #
    (144, 256, 1),     #
    (160, 256, 2),     #
    (176, 256, 2),     #
    (192, 256, 7),     #
    (208, 256, 2),     #
    (224, 256, 2),     #
    (240, 256, 3),     #
    (272, 256, 6),     #
    (304, 256, 13),     #
    (320, 256, 2),     #
    (336, 256, 2),     #
    (352, 256, 2),     #
    (368, 256, 2),     #
    (384, 256, 12),     #

    # fila 16
    (0, 272, 5),     #
    (192, 272, 5),     #
    (384, 272, 5),     #

    # fila 17
    (0, 288, 9),
    (16, 288, 2),
    (32, 288, 2),
    (48, 288, 2),
    (64, 288, 2),
    (80, 288, 3),
    (112, 288, 4),
    (144, 288, 1),
    (160, 288, 2),
    (176, 288, 2),
    (192, 288, 8),
    (208, 288, 2),
    (224, 288, 2),
    (240, 288, 3),
    (272, 288, 4),
    (304, 288, 1),
    (320, 288, 2),
    (336, 288, 2),
    (352, 288, 2),
    (368, 288, 2),
    (384, 288, 10),

    # Fila 18
    (0, 304, 5),     # Borde vertical
    (112, 304, 5),
    (272, 304, 5),
    (384, 304, 5),     # Borde vertical
    
]

MAPA = {1: MAPA_1, 2: MAPA_2}
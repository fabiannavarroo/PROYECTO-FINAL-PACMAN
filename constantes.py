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
    "BASTON": {"Coordenadas": (48,16), "Puntos": 10}, # 0
    "REGALO": {"Coordenadas": (0,32), "Puntos": 15}, # 98
    "REGALO_BRILLANTE": {"Coordenadas": (32,32), "Puntos": 15}, # 98
    "CEREZA" : {"Coordenadas": (0, 128), "Puntos": 20}, # 97
    "FRESA" : {"Coordenadas":(16, 128), "Puntos": 30}, # 96
    "NARANJA" : {"Coordenadas":(32, 128), "Puntos": 40}, # 95
    "MANZANA" : {"Coordenadas":(48, 128), "Puntos": 50}, # 94
    "MELON" : {"Coordenadas":(0, 144), "Puntos": 60}, # 93
    "PARAGUAS" : {"Coordenadas":(16, 144), "Puntos": 100}, # 92 
    "CAMPANA" : {"Coordenadas":(32, 144), "Puntos": 120}, # 91
    "LLAVE" : {"Coordenadas":(48, 144), "Puntos": 140}, # 90
    }

#-----------PORTALES-----------#
PORTALES={
    (-14,208):(402,208), # Portal izquierda
    (402,208):(-14,208)  # Portal derecha
}

#---------------TEXTO--------------#
TEXTO={
    "READY!": {"Coordenadas": (32, 192), "Tamaño": (64, 16)}, # 69
    "HIGHSCORE":{"Coordenadas": (0, 168), "Tamaño": (80, 16)}, # 70
    "GAME OVER": {"Coordenadas": (0, 192), "Tamaño": (32, 24)}, # 71
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

#-----BLOQUES--------#
SPRITE_BLOQUE_1 = (0,0,1,16,16) # Esquina izquierda horizontal
SPRITE_BLOQUE_2 = (8,0,1,16,16) # Borde horizontal
SPRITE_BLOQUE_3 = (16,0,1,16,16) # Esquina derecha horizontal
SPRITE_BLOQUE_4 = (48,0,1,16,16) # Esquina superior vertical
SPRITE_BLOQUE_5 = (48,8,1,16,16) # Borde vertical
SPRITE_BLOQUE_6 = (48,16,1,16,16) # Esquina inferior vertical
SPRITE_BLOQUE_7 = (0,16,1,16,16) # Cruce en T hacia abajo
SPRITE_BLOQUE_8 = (16,16,1,16,16) # Cruce en T hacia arriba
SPRITE_BLOQUE_9 = (32,16,1,16,16) # Cruce en T hacia derecha
SPRITE_BLOQUE_10 = (32,32,1,16,16) # Cruce en T hacia dizquierda
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
    (80, 160, 12),     # 
    (112, 160,9),      # Borde horizontal
    (128, 160, 2),     # Borde horizontal
    (144, 160, 2),     # Borde horizontal
    (160, 160, 3),     #
    (192, 160, 6),     #  
    (224, 160, 1),     #
    (240, 160, 2),     # Borde horizontal
    (256, 160, 2),     # Borde horizontal
    (272, 160, 10),     #
    (304, 160, 11),     #
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
    (80, 192, 14),     # 
    (112, 192 ,6),     # 
    (144, 192, 15),     # 
    (160, 192, 19),     # 
    (176, 192, 16),     # 
    (192, 192, 16),     # 
    (208, 192, 16),     # 
    (224, 192, 19),     # 
    (240, 192, 17),     #  
    (272, 192, 6),     #
    (304, 192, 13),     #
    (320, 192, 2),     # Borde horizontal  
    (336, 192, 2),     # Borde horizontal
    (352, 192, 2),     # Borde horizontal  
    (368, 192, 2),     # Borde horizontal
    (384, 192, 2),     # Borde horizontal

    # Fila 12
    (144, 208, 21),     #
    (240, 208, 22),     #  

    # Fila 13
    (0, 224, 2),      # Borde esquina inferior izquierda
    (16,224,2),      # Borde horizontal
    (32, 224, 2),     # Borde horizontal    
    (48,224,2),      # Borde horizontal
    (64, 224, 2),     # Borde horizontal
    (80, 224, 12),     # 
    (112, 224, 4),     # 
    (144, 224, 18),     #
    (160, 224, 23),     # 
    (176, 224, 23),     # 
    (192, 224, 23),     # 
    (208, 224, 23),     # 
    (224, 224, 23),     # 
    (232, 224, 23),     # 
    (240, 224, 20),     # 
    (272, 224,4),     #
    (304, 224, 11),     #
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
    (80, 256, 14),     # 
    (112, 256 ,6),     # 
    (144, 256, 1),     # 
    (160, 256, 2),     # 
    (176, 256, 2),     # 
    (192, 256, 7),     # 
    (208, 256, 2),     # 
    (224, 256, 2),     # 
    (240, 256, 3),     #  
    (272, 256, 6),     #
    (304, 256, 13),     #
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
    (32, 320, 3),      # 
    (64, 320, 6),     # 
    (96, 320, 4),     # 
    (128, 320, 1),     # 
    (144, 320, 2),     # 
    (160, 320, 2),     # 
    (176, 320, 2),     # 
    (192, 320, 7),     # 
    (208, 320, 2),     # 
    (224, 320, 2),     # 
    (240, 320, 2),     # 
    (256, 320, 3),     # 
    (288, 320, 4),     # 
    (320, 320, 6),     # 
    (352, 320, 1),     # 
    (368, 320, 2),     # 
    (384, 320, 10),     # 

    # Fila 20
    (0, 336, 5),      # Borde vertical
    (96, 336, 5),     # Borde vertical
    (192, 336, 5),     # Borde vertical
    (288, 336, 5),     # Borde vertical
    (384, 336, 5),     # Borde vertical

    # Fila 21
    (0, 352, 5),      # 
    (32, 352, 1),     # 
    (48, 352, 2),     # 
    (64, 352, 2),     # 
    (80, 352, 2),     #
    (96, 352, 8),
    (112, 352, 2),     #
    (128, 352, 2),     #
    (144, 352, 2),     #
    (160, 352, 3),     #
    (192, 352, 6),     #
    (224, 352, 1),     #
    (240, 352, 2),     #
    (256, 352, 2),     #
    (272, 352, 2),     #
    (288, 352, 8),     #
    (304, 352, 2),     #
    (320, 352, 2),     #
    (336, 352, 2),     #
    (352, 352, 3),     #
    (384, 352, 5),     #

    # Fila 22
    (0, 368, 5),      # Borde vertical
    (384, 368, 5),     # Borde vertical
]

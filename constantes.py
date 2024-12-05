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
ANIMACION_MUERTE = [
    (0, 0), (0, 16), (16, 16), (32, 16),(48,32),(64,32)]  # animacion de la muerte del pacman

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
    (-16,192):(430,192), # Portal izquierda
    (430,192):(-16,192)  # Portal derecha
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
SPRITE_BLOQUE_19 = (24,96,1,16,16) # Borde superior trampa fantasma
SPRITE_BLOQUE_20 = (40,80,1,16,16) # Esquina derecha inferior trampa fantasmas
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
    (256,64,12),      # Esquina superior derecha
    (288,64,11),      # Esquina superior izquierda
    (304,64,2),       # Borde horizontal
    (320,64,2),       # Borde horizontal
    (336,64,2),       # Borde horizontal
    (352,64,12),      # Esquina superior izquierda
    (384, 64, 5),     # Esquina inferior derecha

    # fila 4
    (0, 80, 5),      # Borde vertical
    (32,80,5),      # Borde vertical
    (64,80,5),      # Borde vertical
    (96,80,5),      # Borde vertical
    (160,80,5),     # Borde vertical
    (192,80,5),     # Borde vertical
    (384,80,5),     # Borde vertical
    (224,80,5),     # Borde vertical
    (256,80,5),     # Borde vertical
    (288,80,5),     # Borde vertical
    (352,80,5),     # Borde vertical

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
    (384,96,5),     # Borde vertical
    (224,96,13),      # Esquina inferior izquierda
    (240,96,2),       # Borde horizontal
    (256,96,14),      # Esquina inferior derecha
    (288,96,13),      # Esquina inferior izquierda
    (304,96,2),       # Borde horizontal
    (320,96,2),       # Borde horizontal
    (336,96,2),       # Borde horizontal
    (352,96,14),      # Esquina inferior izquierda

    # Fila 6
    (0, 112, 5),      # Borde vertical
    (384, 112, 5),     # Borde vertical

    # Fila 7
    (0, 128, 5),      # Borde vertical
    (32,128,1),      # 
    (48,128,2),      # 
    (64,128,2),      # 
    (80,128,3),      # 
    (112,128,4),      # 
    (144,128,1),      # 
    (160,128,2),      # 
    (176,128,2),      # 
    (192, 128, 7),     # Cruce en T hacia abajo
    (208,128,2),      # 
    (224,128,2),      # 
    (240,128,1),      # 
    (256,128,3),      # 
    (288,128,1),      # 
    (304,128,2),      # 
    (320,128,2),      # 
    (336,128,3),      # 



    (384, 128, 5),     # Borde vertical
    
]

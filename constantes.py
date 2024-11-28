#---------PACMAN---------#
PACMAN = (0, 0)  # Coordenadas de Pacman
PACMAN_ARRIBA = (48, 0)  # Coordenadas de Pacman al moverse arriba
PACMAN_ABAJO = (16, 32)  # Coordenadas de Pacman al moverse abajo
PACMAN_IZQUIERDA = (32, 0)  # Coordenadas de Pacman al moverse a la izquierda
PACMAN_DERECHA = (16, 0)  # Coordenadas de Pacman al moverse a la derecha

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

#--------PUNTOS Y FRUTAS---------#
BASTON = (48, 16)
CEREZA = (0, 128)
FRESA = (16, 128)
NARANJA = (32, 128)
MANZANA = (48, 128)
MELON = (0, 144)
PARAGUAS = (16, 144) 
CAMPANA = (32, 144)
LLAVE = (48, 144)

#---------MUROS---------#
MUROS = {
    1: {"Coordenadas": (0, 0), "Tamaño": (16, 16)},  # Esquina izquierda horizontal
    2: {"Coordenadas": (8, 0), "Tamaño": (16, 16)},  # Borde horizontal
    3: {"Coordenadas": (16, 0), "Tamaño": (16, 16)},  # Esquina derecha horizontal
    4: {"Coordenadas": (48, 0), "Tamaño": (16, 16)},  # Esquina superior vertical
    5: {"Coordenadas": (48, 8), "Tamaño": (16, 16)},  # Borde vertical
    6: {"Coordenadas": (48, 16), "Tamaño": (16,16)},  # Esquina inferior vertical
    7: {"Coordenadas": (0, 16), "Tamaño": (16,16)},  # Cruce en T hacia abajo
    8: {"Coordenadas": (16, 16), "Tamaño": (16,16)},  # Cruce en T hacia arriba
    9: {"Coordenadas": (32, 16), "Tamaño": (16,16)},  # Cruce en T hacia derecha
    10: {"Coordenadas": (32, 32), "Tamaño": (16,16)},  # Cruce en T hacia dizquierda
    11: {"Coordenadas": (0, 32), "Tamaño": (16,16)},  # Borde esquina superior izquieda
    12: {"Coordenadas": (16, 32), "Tamaño": (16,16)},  # Borde esquina superior derecha
    13: {"Coordenadas": (0, 48), "Tamaño": (16,16)},  #  Borde esquina inferior izquieda
    14: {"Coordenadas": (16, 48), "Tamaño": (16,16)},  # Borde esquina inferior derecha
    15: {"Coordenadas": (8, 72), "Tamaño": (16,16)},  # Esquina izquierda superior trampa fantasmas
    16: {"Coordenadas": (24, 72), "Tamaño": (16,16)},  # Puerta salida de fantasmas
    17: {"Coordenadas": (40, 72), "Tamaño": (16,16)},  # Esquina derecha superior trampa fantasmas
    18: {"Coordenadas": (8, 88), "Tamaño": (16,16)},  # Esquina izquierda inferior trampa fantasmas
    19: {"Coordenadas": (24, 96), "Tamaño": (16,8)},  # Borde superior trampa fantasma
    20: {"Coordenadas": (40, 88), "Tamaño": (16,16)},  # Esquina derecha inferior trampa fantasmas
    21: {"Coordenadas": (8, 80), "Tamaño": (16,16)},  # Borde derecha trampa fantasmas
    22: {"Coordenadas": (40, 80), "Tamaño": (16,16)},  # Borde izquierda trampa fantasmas
    23: {"Coordenadas": (24, 88), "Tamaño": (16,16)},  # Borde inferior trampa fantasma
}

#-----------PORTALES-----------#
PORTALES={
    (-16,192):(430,192), # Portal izquierda
    (430,192):(-16,192)  # Portal derecha
}

#--------OTROS---------#
REFRESH = 4
TEXTO_MUERTE = ["Te has quedado sin vidas", "(ESC)Salir"]
#---------PACMAN---------#
PACMAN = (0, 0)  # Coordenadas de Pacman
PACMAN_ARRIBA = (48, 0)  # Coordenadas de Pacman al moverse arriba
PACMAN_ABAJO = (0, 0)  # Coordenadas de Pacman al moverse abajo
PACMAN_IZQUIERDA = (32, 0)  # Coordenadas de Pacman al moverse a la izquierda
PACMAN_DERECHA = (16, 0)  # Coordenadas de Pacman al moverse a la derecha

#---------FANTASMA ROJO---------#
FANTASMA_ROJO_ARIBA = (48, 64)  # Coordenadas del fantasma rojo al moverse arriba
FANTASMA_ROJO_ABAJO = (0, 64)  # Coordenadas del fantasma rojo al moverse abajo
FANTASMA_ROJO_IZQUIERDA = (16, 64)  # Coordenadas del fantasma rojo al moverse a la izquierda
FANTASMA_ROJO_DERECHA = (32, 64)  # Coordenadas del fantasma rojo al moverse a la derecha

#---------FANTASMA AZUL---------#
FANTASMA_AZUL_ARIBA = (48, 48)  # Coordenadas del fantasma azul al moverse arriba
FANTASMA_AZUL_ABAJO = (0, 48)  # Coordenadas del fantasma azul al moverse abajo
FANTASMA_AZUL_IZQUIERDA = (16, 48)  # Coordenadas del fantasma azul al moverse a la izquierda
FANTASMA_AZUL_DERECHA = (32, 48)  # Coordenadas del fantasma azul al moverse a la derecha

#---------FANTASMA NARANJA---------#
FANTASMA_NARANJA_ARIBA = (48, 80)  # Coordenadas del fantasma naranja al moverse arriba
FANTASMA_NARANJA_ABAJO = (0, 80)  # Coordenadas del fantasma naranja al moverse abajo
FANTASMA_NARANJA_IZQUIERDA = (16, 80)  # Coordenadas del fantasma naranja al moverse a la izquierda
FANTASMA_NARANJA_DERECHA = (32, 80)  # Coordenadas del fantasma naranja al moverse a la derecha

#---------FANTASMA ROSA---------#
FANTASMA_ROSA_ARIBA = (48, 96)  # Coordenadas del fantasma rosa al moverse arriba
FANTASMA_ROSA_ABAJO = (0, 96)  # Coordenadas del fantasma rosa al moverse abajo
FANTASMA_ROSA_IZQUIERDA = (16, 96)  # Coordenadas del fantasma rosa al moverse a la izquierda
FANTASMA_ROSA_DERECHA = (32, 96)  # Coordenadas del fantasma rosa al moverse a la derecha

#---------MUROS---------#
MUROS = {
    1: {"Coordenadas": (0, 0), "Tamaño": (16, 16)},  # Esquina izquierda horizontal
    2: {"Coordenadas": (8, 0), "Tamaño": (16, 16)},  # Borde horizontal
    3: {"Coordenadas": (24, 0), "Tamaño": (16, 16)},  # Esquina derecha horizontal
    4: {"Coordenadas": (0, 8), "Tamaño": (16, 16)},  # Esquina superior vertical
    5: {"Coordenadas": (8, 8), "Tamaño": (16, 16)},  # Borde vertical
    6: {"Coordenadas": (24, 8), "Tamaño": (16,16)},  # Esquina inferior vertical
    7: {"Coordenadas": (48, 0), "Tamaño": (16,16)},  # Cruce en T hacia abajo
    8: {"Coordenadas": (56, 0), "Tamaño": (16,16)},  # Cruce en T hacia arriba
    9: {"Coordenadas": (48, 8), "Tamaño": (16,16)},  # Cruce en T hacia derecha
    10: {"Coordenadas": (56, 8), "Tamaño": (16,16)},  # Cruce en T hacia dizquierda
    11: {"Coordenadas": (48, 24), "Tamaño": (16,16)},  # Borde esquina superior izquieda
    12: {"Coordenadas": (56, 24), "Tamaño": (16,16)},  # Borde esquina superior derecha
    13: {"Coordenadas": (0, 16), "Tamaño": (16,16)},  #  Borde esquina inferior izquieda
    14: {"Coordenadas": (8, 16), "Tamaño": (16,16)},  # Borde esquina inferior derecha
    15: {"Coordenadas": (16, 24), "Tamaño": (16,16)},  # Esquina izquierda superior trampa fantasmas
    16: {"Coordenadas": (24, 24), "Tamaño": (16,16)},  # Puerta salida de fantasmas
    17: {"Coordenadas": (0, 32), "Tamaño": (16,16)},  # Esquina derecha superior trampa fantasmas
    18: {"Coordenadas": (24, 32), "Tamaño": (16,16)},  # Esquina borde derecha
    19: {"Coordenadas": (0, 56), "Tamaño": (16,16)},  # Esquina borde izquierda
    20: {"Coordenadas": (24, 56), "Tamaño": (16,16)},  # Esquina borde derecha
    21: {"Coordenadas": (8, 72), "Tamaño": (16,16)},  # Esquina izquierda trampa fantasmas
    22: {"Coordenadas": (48, 72), "Tamaño": (16,16)},  # Esquina derecha trampa fantasmas

}

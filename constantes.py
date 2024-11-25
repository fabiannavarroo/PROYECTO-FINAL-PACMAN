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
MURO_ESQUINA_SUPERIOR_IZQUIERDA = {"Coordenadas": (0, 0), "Tamaño": (8, 8)}  # Esquina superior izquierda horizontal
MURO_BORDE_SUPERIOR = {"Coordenadas": (8, 0), "Tamaño": (8, 8)}  # Borde superior horizontal
MURO_ESQUINA_SUPERIOR_DERECHA = {"Coordenadas": (24, 0), "Tamaño": (8, 8)}  # Esquina superior derecha horizontal
MURO_ESQUINA_INFERIOR_IZQUIERDA = {"Coordenadas": (0, 8), "Tamaño": (8, 8)}  # Esquina inferior izquierda horizontal
MURO_BORDE_INFERIOR = {"Coordenadas": (8, 8), "Tamaño": (8, 8)}  # Borde inferior horizontal
MURO_ESQUINA_INFERIOR_DERECHA = {"Coordenadas": (24, 8), "Tamaño": (8, 8)}  # Esquina inferior derecha horizontal
MURO_VERTICAL_SUPERIOR_IZQUIERDA = {"Coordenadas": (48, 0), "Tamaño": (8, 8)}  # Esquina superior izquierda vertical
MURO_VERTICAL_SUPERIOR_DERECHA = {"Coordenadas": (56, 0), "Tamaño": (8, 8)}  # Esquina superior derecha vertical
MURO_VERTICAL_IZQUIERDO = {"Coordenadas": (48, 8), "Tamaño": (8, 8)}  # Borde izquierdo vertical
MURO_VERTICAL_DERECHO = {"Coordenadas": (56, 8), "Tamaño": (8, 8)}  # Borde derecho vertical
MURO_ESQUINA_INFERIOR_IZQUIERDA_VERTICAL = {"Coordenadas": (48, 24), "Tamaño": (8, 8)}  # Esquina inferior izquierda vertical
MURO_ESQUINA_INFERIOR_DERECHA_VERTICAL = {"Coordenadas": (56, 24), "Tamaño": (8, 8)}  # Esquina inferior derecha vertical
MURO_CRUCE_T_IZQUIERDA = {"Coordenadas": (0, 16), "Tamaño": (8, 8)}  # Cruce en T hacia arriba izquierda
MURO_CRUCE_T_DERECHA = {"Coordenadas": (8, 16), "Tamaño": (8, 8)}  # Cruce en T hacia arriba derecha
MURO_CRUCE_T_ABAJO_IZQUIERDA = {"Coordenadas": (16, 24), "Tamaño": (8, 8)}  # Cruce en T hacia abajo izquierda
MURO_CRUCE_T_ABAJO_DERECHA = {"Coordenadas": (24, 24), "Tamaño": (8, 8)}  # Cruce en T hacia abajo derecha
MURO_ESQUINA_BORDE_SUPERIOR_IZQUIERDA = {"Coordenadas": (0, 32), "Tamaño": (8, 8)}  # Esquina borde superior izquierda
MURO_ESQUINA_BORDE_SUPERIOR_DERECHA = {"Coordenadas": (24, 32), "Tamaño": (8, 8)}  # Esquina borde superior derecha
MURO_ESQUINA_BORDE_INFERIOR_IZQUIERDA = {"Coordenadas": (0, 56), "Tamaño": (8, 8)}  # Esquina borde inferior izquierda
MURO_ESQUINA_BORDE_INFERIOR_DERECHA = {"Coordenadas": (24, 56), "Tamaño": (8, 8)}  # Esquina borde inferior derecha
MURO_TRAMPA_FANTASMAS_IZQUIERDA = {"Coordenadas": (8, 72), "Tamaño": (8, 8)}  # Esquina superior izquierda trampa fantasmas
MURO_TRAMPA_FANTASMAS_DERECHA = {"Coordenadas": (48, 72), "Tamaño": (8, 8)}  # Esquina superior derecha trampa fantasmas
MURO_TRAMPA_FANTASMAS_INFERIOR_IZQUIERDA = {"Coordenadas": (8, 96), "Tamaño": (8, 8)}  # Esquina inferior izquierda trampa fantasmas
MURO_TRAMPA_FANTASMAS_INFERIOR_DERECHA = {"Coordenadas": (48, 96), "Tamaño": (8, 8)}  # Esquina inferior derecha trampa fantasmas
MURO_PUERTA_SALIDA_FANTASMAS = {"Coordenadas": (24, 72), "Tamaño": (8, 8)}  # Puerta de salida fantasmas


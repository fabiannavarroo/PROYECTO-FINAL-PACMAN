def calcular_celda_mas_alejada(self, fantasma):
    # Calcula la celda más alejada de Pac-Man en las direcciones posibles
    pacman_x = self.pacman.x // 16 * 16
    pacman_y = self.pacman.y // 16 * 16
    fantasma_x = fantasma.x // 16 * 16
    fantasma_y = fantasma.y // 16 * 16

    # Definir las direcciones posibles: izquierda, derecha, arriba, abajo
    direcciones = [(-16, 0), (16, 0), (0, -16), (0, 16)]
    max_distancia = -1
    celda_mas_lejos = None

    # Calcular la dirección opuesta para evitar retrocesos
    direccion_opuesta = None
    if fantasma.direccion_actual == "ARRIBA":
        direccion_opuesta = (0, 16)
    elif fantasma.direccion_actual == "ABAJO":
        direccion_opuesta = (0, -16)
    elif fantasma.direccion_actual == "IZQUIERDA":
        direccion_opuesta = (16, 0)
    elif fantasma.direccion_actual == "DERECHA":
        direccion_opuesta = (-16, 0)

    # Evaluar todas las celdas válidas
    celdas_validas = []
    for dx, dy in direcciones:
        nueva_celda_x = fantasma_x + dx
        nueva_celda_y = fantasma_y + dy

        if not self.colision_fantasmas(nueva_celda_x, nueva_celda_y) and (dx, dy) != direccion_opuesta:
            diferencia_x = nueva_celda_x - pacman_x
            diferencia_y = nueva_celda_y - pacman_y
            distancia = diferencia_x * diferencia_x + diferencia_y * diferencia_y  # Cuadrado de la distancia

            celdas_validas.append((distancia, (nueva_celda_x, nueva_celda_y)))

    # Seleccionar la celda con la mayor distancia
    if celdas_validas:
        celda_mas_lejos = max(celdas_validas, key=lambda x: x[0])[1]

    # Si no se encuentra una celda válida, elegir cualquier dirección disponible
    if celda_mas_lejos is None:
        for dx, dy in direcciones:
            nueva_celda_x = fantasma_x + dx
            nueva_celda_y = fantasma_y + dy
            if not self.colision_fantasmas(nueva_celda_x, nueva_celda_y):
                celda_mas_lejos = (nueva_celda_x, nueva_celda_y)

    return celda_mas_lejos


def alejarse_de_pacman(self, fantasma):
    # El fantasma busca una celda cercana que lo aleje de Pac-Man
    if fantasma.siguiente_celda is None or (fantasma.x == fantasma.siguiente_celda[0] and fantasma.y == fantasma.siguiente_celda[1]):
        inicio = (fantasma.x // 16 * 16, fantasma.y // 16 * 16)
        objetivo = self.calcular_celda_mas_alejada(fantasma)
        if objetivo is None:
            # Si no hay un objetivo válido, permanecer en la misma posición
            objetivo = inicio
        ruta = self.buscar_ruta_simple(inicio, objetivo)

        if ruta and len(ruta) > 1:
            fantasma.siguiente_celda = ruta[1]
        else:
            fantasma.siguiente_celda = None

    self.mover_hacia_siguiente_celda(fantasma)
#!/bin/bash

# Ruta a tu repositorio
REPO_PATH="/Users/fabiannavarrofonte/Documents/Uni/Programación/PROYECTO-FINAL-PACMAN"

# Archivo temporal para registrar la última ejecución
LAST_RUN_FILE=/tmp/last_git_run

# Intervalo mínimo entre ejecuciones (en segundos)
MIN_INTERVAL=10


# Verificar si ha pasado suficiente tiempo desde la última ejecución
if [[ -f "$LAST_RUN_FILE" ]]; then
    LAST_RUN=$(cat "$LAST_RUN_FILE")
    CURRENT_TIME=$(date +%s)
    ELAPSED=$((CURRENT_TIME - LAST_RUN))

    if [[ $ELAPSED -lt $MIN_INTERVAL ]]; then
        echo "Esperando antes de volver a ejecutar. Tiempo restante: $((MIN_INTERVAL - ELAPSED)) segundos."
        exit 0
    fi
fi

# Registrar el tiempo de la última ejecución
date +%s > "$LAST_RUN_FILE"

# Cambiar al directorio del repositorio
cd "$REPO_PATH" || exit

# Verificar si hay cambios en el repositorio
if [[ -n $(git status --porcelain) ]]; then
    echo "Hay cambios, procesando commit..."

    # Hacer pull antes de añadir cambios para evitar conflictos
    git pull origin main --rebase

    # Añadir todos los cambios
    git add .

    # Realizar el commit con fecha y hora actuales
    git commit -m "Auto-commit: $(date)"

    # Subir los cambios al repositorio remoto
    git push origin main

    echo "¡Cambios subidos correctamente!"
else
    echo "No hay cambios. Nada que confirmar."
fi
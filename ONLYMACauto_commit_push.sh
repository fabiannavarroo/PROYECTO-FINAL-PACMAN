#!/bin/bash

# Ruta a tu repositorio
cd /Users/fabiannavarrofonte/Documents/Uni/Programación/PROYECTO-FINAL-PACMAN

# Verificar si hay cambios en el repositorio
if [[ -n $(git status --porcelain) ]]; then
    echo "Hay cambios, procesando..."

    # Hacer pull antes de añadir cambios para evitar conflictos
    git pull origin main --rebase

    # Añadir todos los cambios
    git add .

    # Realizar commit con fecha y hora actuales
    git commit -m "Auto-commit: $(date)"

    # Subir cambios al repositorio
    git push origin main

    echo "¡Cambios subidos correctamente!"
else
    echo "No hay cambios. Nada que confirmar."
fi
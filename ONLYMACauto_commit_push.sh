#!/bin/bash

# Ruta a tu repositorio
cd /Users/fabiannavarrofonte/Documents/Uni/Programación/PROYECTO-FINAL-PACMAN # Cambia esta ruta por la ubicación de tu repositorio

# Añadir todos los cambios
echo "Añadiendo cambios..."
git add .

# Realizar commit con fecha y hora actuales
echo "Realizando commit..."
git commit -m "Auto-commit: $(date)"

# Subir cambios al repositorio
echo "Subiendo cambios al repositorio..."
git push origin main

echo "¡Cambios subidos correctamente!"
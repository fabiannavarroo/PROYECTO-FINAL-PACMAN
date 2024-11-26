#!/bin/bash

# Cambiar al directorio del repositorio
cd /Users/fabiannavarrofonte/Documents/Uni/Programación/PROYECTO-FINAL-PACMAN

# Actualizar el repositorio desde GitHub
echo "Actualizando el repositorio..."
git pull origin main

# Abrir el proyecto en Cursor
echo "Abriendo el proyecto en Cursor..."
open -a "Cursor" .

echo "¡Todo listo!"
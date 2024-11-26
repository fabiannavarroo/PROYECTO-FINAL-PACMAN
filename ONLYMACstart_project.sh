#!/bin/bash

# Ruta del repositorio
REPO_PATH="/Users/fabiannavarrofonte/Documents/Uni/Programación/PROYECTO-FINAL-PACMAN"

# Cambiar al directorio del repositorio
if cd "$REPO_PATH"; then
    echo "Cambiado al directorio del repositorio: $REPO_PATH"
else
    echo "Error: No se pudo acceder al directorio $REPO_PATH"
    exit 1
fi

# Actualizar el repositorio desde GitHub
echo "Descargando los últimos cambios del repositorio remoto..."
git fetch origin

# Forzar la sincronización de la rama local con la remota
echo "Reemplazando la rama local con la versión remota..."
git reset --hard origin/main

# Abrir el proyecto en Cursor (o Visual Studio Code)
echo "Abriendo el proyecto en Cursor..."
open -a "Cursor" "$REPO_PATH"

echo "¡Todo listo!"
exit 0

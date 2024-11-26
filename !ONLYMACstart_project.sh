#!/bin/bash

# Ruta del repositorio
REPO_PATH="/Users/fabiannavarrofonte/Documents/Uni/Programación/PROYECTO-FINAL-PACMAN"

# Cambiar al directorio del repositorio
cd "$REPO_PATH" || { echo "Error: No se pudo acceder al directorio"; exit 1; }

echo "Verificando el estado del repositorio..."
git status
if [ $? -ne 0 ]; then
    echo "Error: No se pudo verificar el estado del repositorio. Revisa si existe y está bien configurado."
    exit 1
fi

echo "Guardando cambios locales no confirmados (si los hubiera)..."
git stash
if [ $? -ne 0 ]; then
    echo "Advertencia: No se pudieron guardar los cambios locales. Verifica manualmente."
fi

echo "Actualizando el repositorio con los últimos cambios..."
git pull origin main --rebase
if [ $? -ne 0 ]; then
    echo "Error: Hubo un problema al actualizar el repositorio. Revisa posibles conflictos."
    exit 1
fi

echo "Restaurando cambios locales guardados..."
git stash pop
if [ $? -ne 0 ]; then
    echo "Advertencia: No se pudieron aplicar los cambios locales guardados. Puede haber conflictos."
fi

echo "Abriendo el proyecto en Cursor..."
open -a "Cursor" .

echo "¡Todo listo!"
exit 0

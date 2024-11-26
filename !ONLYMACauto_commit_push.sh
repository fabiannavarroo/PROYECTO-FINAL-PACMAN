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

echo "Añadiendo todos los cambios locales..."
git add .
if [ $? -ne 0 ]; then
    echo "Error: No se pudieron añadir los cambios. Revisa el estado de los archivos."
    exit 1
fi

echo "Realizando el commit..."
git commit -m "Auto-commit: $(date)"
if [ $? -ne 0 ]; then
    echo "Error: No se pudo realizar el commit. Asegúrate de que hay cambios para confirmar."
    exit 1
fi

echo "Subiendo los cambios al repositorio remoto..."
git push origin main
if [ $? -ne 0 ]; then
    echo "Error: No se pudieron subir los cambios. Revisa la conexión y los permisos del repositorio."
    exit 1
fi

echo "Cambios subidos correctamente."
exit 0

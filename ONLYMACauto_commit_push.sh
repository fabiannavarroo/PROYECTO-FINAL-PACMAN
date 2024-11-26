#!/bin/bash

echo "Añadiendo todos los cambios locales..."
git add .

echo "Haciendo commit..."
git commit -m "Auto-commit: $(date)"

echo "Sincronizando con el repositorio remoto..."
git fetch origin

echo "Reemplazando la rama local con la remota si hay conflictos..."
git reset --hard origin/main

echo "Subiendo los cambios locales..."
git push origin main

if [ $? -ne 0 ]; then
    echo "Error al subir cambios. Por favor, verifica tu conexión."
    exit 1
fi

echo "Cambios subidos correctamente."
exit 0

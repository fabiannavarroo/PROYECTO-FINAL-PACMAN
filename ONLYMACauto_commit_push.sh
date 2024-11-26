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

# Guardar los cambios locales no confirmados
echo "Guardando cambios locales no confirmados..."
git stash

# Añadir todos los cambios locales
echo "Añadiendo todos los cambios locales..."
git add .

# Hacer commit con la fecha y hora actual
COMMIT_MESSAGE="Auto-commit: $(date)"
echo "Haciendo commit con mensaje: '$COMMIT_MESSAGE'"
git commit -m "$COMMIT_MESSAGE"

# Sincronizar con la rama remota
echo "Sincronizando con la rama remota..."
git fetch origin

# Reemplazar la rama local con la remota
echo "Reemplazando la rama local con la versión remota..."
git reset --hard origin/main

# Recuperar los cambios locales guardados
echo "Recuperando cambios locales guardados..."
git stash pop

# Subir los cambios locales
echo "Subiendo los cambios locales al repositorio remoto..."
git push origin main

if [ $? -ne 0 ]; then
    echo "Error al subir cambios. Por favor, verifica tu conexión o conflictos."
    exit 1
fi

echo "Cambios subidos correctamente."
exit 0

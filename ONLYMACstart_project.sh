#!/bin/bash

echo "Actualizando el proyecto..."

echo "Descargando los últimos cambios del repositorio remoto..."
git fetch origin

echo "Forzando la sincronización de la rama local con la remota..."
git reset --hard origin/main

echo "Proyecto actualizado correctamente. Abriendo el editor..."
code .

exit 0

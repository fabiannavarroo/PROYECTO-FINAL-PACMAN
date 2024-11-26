@echo off
echo Actualizando el repositorio...

echo Descargando los últimos cambios del repositorio remoto...
git fetch origin

echo Reemplazando la rama local con la versión remota...
git reset --hard origin/main

echo Proyecto actualizado correctamente. Abriendo el editor...
start code .

pause
exit

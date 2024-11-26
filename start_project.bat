@echo off
echo Guardando cambios locales no confirmados...
git stash

echo Descargando los últimos cambios del repositorio remoto...
git fetch origin

echo Reemplazando la rama local con la versión remota...
git reset --hard origin/main

echo Recuperando cambios locales guardados...
git stash pop

echo Proyecto actualizado correctamente. Abriendo el editor...
start code .

pause
exit

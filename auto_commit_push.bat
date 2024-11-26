@echo off
echo Guardando cambios locales no confirmados...
git stash

echo Añadiendo todos los cambios locales...
git add .

echo Haciendo commit...
git commit -m "Auto-commit: %date% %time%"

echo Sincronizando con el repositorio remoto...
git fetch origin

echo Fusionando con los cambios remotos...
git reset --hard origin/main

echo Recuperando cambios locales guardados...
git stash pop

echo Subiendo los cambios locales al repositorio remoto...
git push origin main

if %errorlevel% neq 0 (
    echo Error al subir cambios. Por favor, verifica tu conexión o conflictos.
    pause
    exit /b
)

echo Cambios subidos correctamente.
pause
exit

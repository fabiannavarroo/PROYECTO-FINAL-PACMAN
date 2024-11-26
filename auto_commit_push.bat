@echo off
echo Añadiendo todos los cambios locales...
git add .

echo Haciendo commit...
git commit -m "Auto-commit: %date% %time%"

echo Sincronizando con el repositorio remoto...
git fetch origin

echo Reemplazando la rama local con la remota si hay conflictos...
git reset --hard origin/main

echo Subiendo los cambios locales...
git push origin main

if %errorlevel% neq 0 (
    echo Error al subir cambios. Por favor, verifica tu conexión.
    pause
    exit /b
)

echo Cambios subidos correctamente.
pause
exit
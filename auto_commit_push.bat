@echo off
echo Añadiendo todos los cambios locales...
git add .

echo Haciendo commit...
git commit -m "Auto-commit: %date% %time%"

echo Sincronizando con la rama remota...
git fetch origin

echo Reemplazando la rama local con la versión remota...
git reset --hard origin/main

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

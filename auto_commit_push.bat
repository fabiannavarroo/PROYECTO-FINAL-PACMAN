@echo off
echo Añadiendo cambios al repositorio...
git add .
git commit -m "Auto-commit: %date% %time%"
if %errorlevel% neq 0 (
    echo Error al realizar el commit. Verifica el estado del repositorio.
    pause
    exit /b
)

echo Subiendo los cambios al repositorio remoto...
git push origin main
if %errorlevel% neq 0 (
    echo Error al subir los cambios. Verifica la conexión o el estado del repositorio remoto.
    pause
    exit /b
)

echo Cambios subidos correctamente.
pause

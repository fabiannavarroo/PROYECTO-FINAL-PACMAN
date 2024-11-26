@echo off
echo Verificando el estado del repositorio...
git status
if %errorlevel% neq 0 (
    echo Error al verificar el estado. Asegúrate de que el repositorio existe y está bien configurado.
    pause
    exit /b
)

echo Limpiando cambios locales no confirmados...
git stash
if %errorlevel% neq 0 (
    echo No se pudieron guardar los cambios locales. Por favor, verifica manualmente.
    pause
    exit /b
)

echo Actualizando el repositorio con los últimos cambios...
git pull origin main --rebase
if %errorlevel% neq 0 (
    echo Error al actualizar el repositorio. Verifica posibles conflictos.
    pause
    exit /b
)

echo Aplicando cambios locales guardados, si los hubiera...
git stash pop
if %errorlevel% neq 0 (
    echo No se pudieron aplicar los cambios locales guardados. Puede haber conflictos.
    pause
)

echo Iniciando el proyecto...
start code .
exit

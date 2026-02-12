@echo off
REM ============================================================
REM Script de Preview - Solaire Empire
REM Lance le serveur local et ouvre le navigateur
REM ============================================================

echo ============================================================
echo    SOLAIRE EMPIRE - Preview Local
echo ============================================================
echo.

REM Verification Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERREUR] Python n'est pas installe
    echo Installation: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [OK] Python detecte
echo.

REM Changement de repertoire
cd /d "%~dp0src"
echo Repertoire: %CD%
echo.

echo [1/2] Demarrage du serveur...
echo URL: http://localhost:8000
echo.
echo [2/2] Ouverture du navigateur dans 3 secondes...
echo.
echo Appuyez sur Ctrl+C pour arreter le serveur
echo ============================================================
echo.

REM Attendre 3 secondes et ouvrir le navigateur
timeout /t 3 /nobreak >nul
start http://localhost:8000

REM Lancer le serveur Python
python -m http.server 8000

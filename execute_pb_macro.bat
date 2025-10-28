@echo off

:: ---------------------------------------------------------------------
:: 1. Bloco de Verificacao de Administrador
:: ---------------------------------------------------------------------
REM Verifica se o script ja tem privilegios de admin
fsutil dirty query %systemdrive% >nul

REM Se o comando acima falhar (errorLevel nao for 0), nao e admin.
if %errorLevel% NEQ 0 (
    echo Solicitando privilegios de Administrador...
    
    REM Re-lanca este mesmo script (.bat) como Administrador
    powershell -Command "Start-Process -FilePath '%~f0' -Verb RunAs"
    
    REM Sai da instancia atual (que nao e admin)
    exit
)

:: ---------------------------------------------------------------------
:: 2. Codigo Principal (so executa se for Admin)
:: ---------------------------------------------------------------------

:: --- ESTA É A CORREÇÃO ---
:: Força o terminal a mudar para o diretório onde o .bat está
cd /d "%~dp0"

REM Limpa a tela apos a verificacao de admin
cls
echo ===================================
echo  PRIVILEGIOS DE ADMINISTRADOR OBTIDOS
echo  Executando a partir de: %cd%
echo ===================================
echo.

ECHO Ativando o ambiente virtual (.venv)...
call .\.venv\Scripts\activate

ECHO Iniciando o script pb_macro.py...
ECHO (Pressione Ctrl+C no terminal para parar o script)
python pb_macro.py

ECHO Script encerrado.
pause
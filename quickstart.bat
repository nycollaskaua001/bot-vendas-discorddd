@echo off
echo 🤖 Bem-vindo ao Bot de Vendas Discord!
echo.

REM Verificar se Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python não está instalado!
    pause
    exit /b 1
)

echo ✅ Python encontrado

REM Verificar se .env existe
if not exist .env (
    echo ⚠️  Arquivo .env não encontrado!
    echo Criando .env a partir de .env.example...
    copy .env.example .env
    echo 📝 Por favor, edite o arquivo .env com suas configurações!
    pause
    exit /b 1
)

echo ✅ Arquivo .env encontrado

REM Criar virtual environment se não existir
if not exist "venv" (
    echo 📦 Criando virtual environment...
    python -m venv venv
)

REM Ativar virtual environment
echo 🔌 Ativando virtual environment...
call venv\Scripts\activate.bat

REM Instalar dependências
echo 📥 Instalando dependências...
pip install -r requirements.txt

REM Criar pastas necessárias
echo 📁 Criando pastas...
if not exist data mkdir data
if not exist assets mkdir assets

echo.
echo ✅ Tudo pronto!
echo.
echo Para iniciar o bot, execute:
echo    python main.py
echo.
pause

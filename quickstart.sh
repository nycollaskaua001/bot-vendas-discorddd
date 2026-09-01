#!/bin/bash
# Quick Start Script - Bot de Vendas Discord

echo "🤖 Bem-vindo ao Bot de Vendas Discord!"
echo ""

# Verificar se Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 não está instalado!"
    exit 1
fi

echo "✅ Python encontrado"

# Verificar se .env existe
if [ ! -f .env ]; then
    echo "⚠️  Arquivo .env não encontrado!"
    echo "Criando .env a partir de .env.example..."
    cp .env.example .env
    echo "📝 Por favor, edite o arquivo .env com suas configurações!"
    exit 1
fi

echo "✅ Arquivo .env encontrado"

# Criar virtual environment se não existir
if [ ! -d "venv" ]; then
    echo "📦 Criando virtual environment..."
    python3 -m venv venv
fi

# Ativar virtual environment
echo "🔌 Ativando virtual environment..."
source venv/bin/activate

# Instalar dependências
echo "📥 Instalando dependências..."
pip install -r requirements.txt

# Criar pastas necessárias
echo "📁 Criando pastas..."
mkdir -p data
mkdir -p assets

echo ""
echo "✅ Tudo pronto!"
echo ""
echo "Para iniciar o bot, execute:"
echo "   python main.py"
echo ""

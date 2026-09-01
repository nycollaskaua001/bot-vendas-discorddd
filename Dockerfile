FROM python:3.11-slim

WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copiar arquivos
COPY requirements.txt .
COPY . .

# Instalar dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Criar diretórios
RUN mkdir -p data assets

# Comando padrão
CMD ["python", "main.py"]

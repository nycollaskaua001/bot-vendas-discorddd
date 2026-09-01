# 🚀 Guia de Deploy - Bot de Vendas Discord

Instruções para colocar seu bot em produção.

## ☁️ Opções de Deploy

### 1. **Seu Próprio Computador** (Teste/Desenvolvimento)
- Grátis
- Fácil de configurar
- Seu PC precisa estar ligado 24/7

### 2. **Hosting em Nuvem** (Recomendado)
- Heroku (descontinuado)
- Replit
- Oracle Cloud (Free Tier)
- AWS / DigitalOcean / Linode
- Railway / Render

### 3. **VPS (Servidor Virtual)**
- Mais controle
- Melhor performance
- Requer conhecimento técnico

---

## 📱 Deploy no Replit (Mais Fácil)

### Passo 1: Criar Conta
1. Vá para [replit.com](https://replit.com)
2. Crie uma conta
3. Clique em "Create Repl"

### Passo 2: Upload do Código
```bash
# No seu computador
git clone seu-repositorio
cd bot-vendas-discord

# Ou upload manual via interface
```

### Passo 3: Instalar Dependências
```bash
pip install -r requirements.txt
```

### Passo 4: Configurar .env
```bash
# Na interface do Replit
# Crie um arquivo .env com suas configurações
DISCORD_TOKEN=seu_token
# ... resto das variáveis
```

### Passo 5: Executar
```bash
python main.py
```

---

## 🐳 Deploy com Docker

### Pré-requisitos
- Docker instalado ([docker.com](https://www.docker.com))
- Docker Compose (opcional)

### Build da Imagem
```bash
docker build -t bot-vendas-discord .
```

### Executar Container
```bash
docker run --name bot-vendas \
  -e DISCORD_TOKEN="seu_token" \
  -e GUILD_ID="seu_id" \
  -e PIX_KEY="sua_chave" \
  -e OWNER_ID="seu_id" \
  -v $(pwd)/data:/app/data \
  -v $(pwd)/assets:/app/assets \
  bot-vendas-discord
```

### Ou com Docker Compose
```bash
docker-compose up -d
```

---

## 🌐 Deploy no Oracle Cloud (Free Tier)

### Passo 1: Criar Conta
1. Vá para [oracle.com/cloud/free](https://www.oracle.com/cloud/free/)
2. Crie uma conta
3. Configure a instância sempre ativa

### Passo 2: Conectar via SSH
```bash
ssh -i sua_chave.key ubuntu@seu_ip_publico
```

### Passo 3: Instalação
```bash
# Atualizar sistema
sudo apt update && sudo apt upgrade -y

# Instalar Python
sudo apt install python3 python3-pip git -y

# Clonar repositório
git clone seu-repositorio
cd bot-vendas-discord

# Instalar dependências
pip3 install -r requirements.txt
```

### Passo 4: Configurar .env
```bash
nano .env
# Adicionar configurações
```

### Passo 5: Rodando com systemd
```bash
# Criar arquivo de serviço
sudo nano /etc/systemd/system/bot-vendas.service
```

Conteúdo:
```ini
[Unit]
Description=Bot de Vendas Discord
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/bot-vendas-discord
ExecStart=/usr/bin/python3 main.py
Restart=on-failure
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Ativar:
```bash
sudo systemctl daemon-reload
sudo systemctl enable bot-vendas
sudo systemctl start bot-vendas
```

---

## 🎯 Deploy no Railway

### Passo 1: Criar Conta
1. Vá para [railway.app](https://railway.app)
2. Login com GitHub

### Passo 2: Criar Novo Projeto
1. Clique em "New Project"
2. Selecione "Deploy from GitHub repo"
3. Selecione seu repositório

### Passo 3: Variáveis de Ambiente
1. Na dashboard, clique em "Variables"
2. Adicione:
   - DISCORD_TOKEN
   - GUILD_ID
   - PIX_KEY
   - OWNER_ID
   - etc...

### Passo 4: Deploy
O Railway faz deploy automaticamente!

---

## 🔧 Configuração para Produção

### Melhorias de Performance

1. **Aumentar Pool de Conexões**
```python
# No main.py
max_cached_messages = 128  # Reduzir uso de memória
```

2. **Logging em Produção**
```python
import logging
logging.basicConfig(
    level=logging.INFO,
    filename='bot.log',
    format='%(asctime)s - %(levelname)s - %(message)s'
)
```

3. **Error Handling**
```python
@bot.event
async def on_error(event, *args, **kwargs):
    logger.error(f"Erro em {event}: {sys.exc_info()}")
```

### Monitoramento

1. **Verificar Status**
```bash
# Verificar logs
docker logs bot-vendas

# Ou
tail -f bot.log
```

2. **Restart Automático**
```bash
# Docker
docker run --restart=always bot-vendas-discord

# Ou systemd
sudo systemctl restart bot-vendas
```

### Backup de Dados

```bash
# Fazer backup
tar -czf backup_$(date +%Y%m%d).tar.gz data/ assets/

# Restaurar
tar -xzf backup_20240115.tar.gz
```

---

## 🔒 Segurança em Produção

### 1. Proteger Token
- ✅ Use `.env` (nunca commitar)
- ✅ Use variáveis de ambiente do hosting
- ✅ Regenere token se for vazado

### 2. Permissões
- Restrinja comandos apenas ao owner
- Valide inputs de usuários
- Use rate limiting

### 3. Dados Sensíveis
- Não salve tokens/senhas nos logs
- Faça backup criptografado
- Implemente HTTPS para APIs

### 4. Monitoramento
```python
# Adicionar ao config.py
ENABLE_MONITORING = True
LOG_LEVEL = logging.INFO
```

---

## 📊 Performance

### Otimizações

1. **Cache de Produtos**
```python
# No cogs/vendas.py
from functools import lru_cache

@lru_cache(maxsize=100)
def load_products():
    # Carregará em cache
    pass
```

2. **Async Operations**
```python
# Use sempre async em I/O
async def save_transaction(data):
    # Não bloqueia o bot
    pass
```

3. **Database (Futuro)**
Substitua JSON por banco de dados real para melhor performance.

---

## 🆘 Troubleshooting em Produção

### Bot desconecta frequentemente
- Verifique conexão com internet
- Aumente timeout no config
- Verifique logs de erro

### Memória aumentando
- Limpar cache periodicamente
- Reduzir mensagens em cache
- Usar profiler: `pip install memory-profiler`

### QR Code não funciona
- Verifique permissões de arquivo
- Verifique tamanho de imagem
- Teste em máquina local primeiro

---

## 📈 Monitoramento e Logs

### Ver Logs em Tempo Real
```bash
# Em systemd
sudo journalctl -u bot-vendas -f

# Em Docker
docker logs -f bot-vendas

# Em arquivo
tail -f bot.log
```

### Análise de Performance
```python
# Adicione ao main.py
import time

@bot.event
async def on_command(ctx):
    start = time.time()
    # comando executa
    elapsed = time.time() - start
    print(f"Comando levou {elapsed:.2f}s")
```

---

## 🚨 Alertas e Notificações

```python
# Notificar se houver erro crítico
async def on_error(self, event, *args, **kwargs):
    # Enviar mensagem para owner
    owner = await bot.fetch_user(OWNER_ID)
    await owner.send(f"❌ Erro em produção: {event}")
```

---

## ✅ Checklist de Deploy

- [ ] Token seguro em .env
- [ ] Banco de dados funcionando
- [ ] Comandos testados
- [ ] Permissões corretas
- [ ] Logging habilitado
- [ ] Backup configurado
- [ ] Backup feito
- [ ] Monitoramento ativo
- [ ] Documentação atualizada
- [ ] Teste final em staging

---

## 🎉 Deploy Bem-Sucedido!

Se tudo funcionou:
```bash
# Ver status
docker ps  # Se usando Docker

# Ou
systemctl status bot-vendas  # Se usando systemd

# Ou verificar no Discord
# Se o bot está online, está funcionando!
```

---

**Última atualização:** Agosto 2026  
**Versão:** 1.0.0

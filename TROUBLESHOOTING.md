# 🆘 Troubleshooting - Bot de Vendas Discord

## Problemas Comuns e Soluções

### 1. Bot não aparece online

**Problema:** O bot não está respondendo aos comandos e não aparece como online no servidor.

**Soluções:**
- Verifique se o token do bot está correto no arquivo `.env`
- Verifique se o bot está convidado para o servidor
- Certifique-se de que tem as permissões necessárias no servidor
- Reinicie o bot: `python main.py`

```bash
# Teste se o token é válido
python -c "import discord; print('Token válido' if 'seu_token' else 'Token vazio')"
```

---

### 2. ModuleNotFoundError: No module named 'discord'

**Problema:** Python não encontra a biblioteca discord.py

**Solução:**
Instale as dependências:
```bash
pip install -r requirements.txt
```

Ou instale manualmente:
```bash
pip install discord.py==2.3.2
```

---

### 3. Comando não é reconhecido

**Problema:** `!comando` não funciona

**Soluções:**
- Verifique se está usando o prefixo correto: `!`
- Certifique-se de que o bot tem permissão de enviar mensagens
- Se é um comando de admin, verifique se seu ID está correto
- Reinicie o bot

---

### 4. QR Code não funciona/não escaneia

**Problema:** O QR Code gerado não pode ser lido pelo celular

**Soluções:**
- Verifique se a chave PIX está correta no arquivo `.env`
- Certifique-se de que está usando um tipo de chave PIX válida:
  - CPF: `12345678900`
  - Email: `seu@email.com`
  - Telefone: `+5511999999999`
  - Aleatória: UUID válido
  
- Teste o QR Code manualmente com um gerador online
- Verifique se a biblioteca `qrcode` está instalada

```bash
pip install qrcode[pil]==7.4.2
```

---

### 5. Arquivo `.env` não encontrado

**Problema:** `FileNotFoundError: .env not found`

**Solução:**
```bash
# Copiar o arquivo de exemplo
cp .env.example .env

# Depois edite o arquivo .env com suas configurações
```

---

### 6. Erro: "Missing permissions"

**Problema:** O bot não tem permissão para executar uma ação

**Soluções:**
- Verifique as permissões do bot no servidor
- Certifique-se de que o bot está acima de outras roles
- Dê permissão de "Send Messages", "Embed Links", "Attach Files"

---

### 7. Produtos não aparecem na vitrine

**Problema:** O comando `!vitrine` não mostra produtos

**Soluções:**
- Verifique se há produtos cadastrados: `!listprodutos`
- Certifique-se de que estão ativos: `!toggleproduto 1`
- Verifique o arquivo `data/products.json`

---

### 8. Erro ao fazer upload de imagem

**Problema:** `!setbanner` não funciona

**Soluções:**
- Certifique-se de que anexou uma imagem
- Verifique se o arquivo é uma imagem válida (PNG, JPG, etc.)
- Verifique se a pasta `assets` existe e tem permissão de escrita

---

### 9. "Invalid Token" ou "401 Unauthorized"

**Problema:** Token inválido ou expirado

**Soluções:**
- Gere um novo token no [Discord Developer Portal](https://discord.com/developers/applications)
- Copie o novo token para `.env`
- Certifique-se de que o bot tem as permissões necessárias
- Reinicie o bot

---

### 10. Cogs não carregam

**Problema:** Os comandos dos cogs não aparecem

**Soluções:**
- Verifique se os arquivos estão em `cogs/` com extensão `.py`
- Certifique-se de que cada arquivo tem uma função `async def setup(bot)`
- Verifique o console para mensagens de erro
- Reinicie o bot

---

## Verificar Logs

Para ver logs detalhados do bot:

```python
# No arquivo main.py, aumente o nível de logging
import logging
logging.basicConfig(level=logging.DEBUG)  # DEBUG para mais detalhes
```

---

## Redefinir Tudo

Se tudo estiver quebrado, você pode redefinir:

```bash
# Remove o ambiente virtual
rm -rf venv

# Remove dados (cuidado!)
rm -rf data/
rm -rf assets/

# Refaça o setup
python quickstart.py  # ou quickstart.sh / quickstart.bat
```

---

## Contato e Suporte

Se o problema persistir:
1. Verifique a documentação do [discord.py](https://discordpy.readthedocs.io/)
2. Verifique o [Discord Developer Portal](https://discord.com/developers/applications)
3. Consulte o console para mensagens de erro detalhadas

---

## Debug Mode

Para executar em modo debug:

```python
# Modifique o final do main.py
if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.DEBUG)
    bot.run(DISCORD_TOKEN)
```

---

**Última atualização:** Agosto 2026

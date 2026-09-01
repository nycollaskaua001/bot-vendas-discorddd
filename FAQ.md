# ❓ FAQ - Perguntas Frequentes

## Instalação e Setup

### P: Como criar um bot no Discord?
**R:** 
1. Acesse [Discord Developer Portal](https://discord.com/developers/applications)
2. Clique em "New Application"
3. Dê um nome ao seu bot
4. Vá para "Bot" e clique em "Add Bot"
5. Copie o token (esse é seu `DISCORD_TOKEN`)
6. Em "OAuth2" > "URL Generator", selecione "bot" e "Administrator"
7. Copie a URL e abra no navegador para convidar o bot

### P: Como encontrar meu Guild ID?
**R:**
1. No Discord, ative "Modo de Desenvolvedor" (Configurações > Avançado)
2. Clique com botão direito no servidor
3. Selecione "Copiar ID do Servidor"
4. Cole em `GUILD_ID` no `.env`

### P: Como encontrar meu User ID?
**R:**
1. Ative "Modo de Desenvolvedor" no Discord
2. Clique com botão direito no seu usuário
3. Selecione "Copiar ID do Usuário"
4. Cole em `OWNER_ID` no `.env`

### P: Preciso instalar Python?
**R:** Sim! Python 3.8 ou superior. Baixe em [python.org](https://www.python.org)

---

## Configuração do PIX

### P: Qual tipo de chave PIX usar?
**R:** Qualquer uma:
- **CPF:** `12345678900`
- **Email:** `seu@email.com`
- **Telefone:** `+5511999999999`
- **Aleatória:** Uma chave UUID válida do seu banco

### P: Onde copio a chave PIX?
**R:**
1. Abra o app do seu banco
2. Procure por "Minhas chaves PIX" ou similar
3. Copie a chave desejada
4. Cole em `PIX_KEY` no `.env`

### P: Como bloquear um banco?
**R:** No arquivo `.env`:
```env
BLOCKED_BANKS=NuBank,Inter,Bradesco
```
Separe os bancos por vírgula.

### P: O QR Code não funciona no meu banco
**R:** Alguns bancos têm limitações. Tente:
- Usar um tipo de chave diferente
- Escanear com outro app de PIX
- Verificar se a chave está correta

---

## Gerenciamento de Produtos

### P: Como adicionar um produto?
**R:**
```
!addproduto "Nome do Produto" 99.90 "Descrição"
```

### P: Posso editar um produto depois?
**R:** Sim! Use:
```
!editproduto <id> nome "Novo Nome"
!editproduto <id> preco 149.90
!editproduto <id> descricao "Nova descrição"
```

### P: Como ativar/desativar um produto?
**R:**
```
!toggleproduto <id>
```

### P: Qual é o ID do meu produto?
**R:** Use `!listprodutos` para ver todos com seus IDs.

### P: Posso ter produtos grátis?
**R:** Sim! Use preço `0` ou remova o produto.

---

## Compras e Pagamentos

### P: Como um cliente compra um produto?
**R:**
1. Cliente usa `!vitrine` para ver produtos
2. Cliente usa `!comprar <id>` para iniciar compra
3. Escaneia o QR Code com PIX
4. Faz o pagamento
5. Usa `!comprovar` para registrar o comprovante

### P: Como confirmar o pagamento?
**R:** Você pode:
1. Receber a notificação no seu banco
2. Verificar o arquivo `data/transactions.json`
3. Criar um sistema de confirmação automática (futuro)

### P: O cliente pode modificar o valor do PIX?
**R:** Teoricamente sim, mas o valor correto já vem no QR Code. Recomende que paguem o valor exato.

---

## Personalizações

### P: Como adicionar um banner personalizado?
**R:**
1. Use `!setbanner` no Discord
2. Anexe uma imagem PNG ou JPG
3. A imagem será usada na vitrine

### P: Qual tamanho de imagem devo usar?
**R:** Recomendado:
- **Banner:** 1200x300 pixels
- **QR Code:** 300x300 pixels

### P: Como mudar a cor do embed?
**R:** Edite o arquivo `config.py`:
```python
COLORS = {
    'success': 0x00ff00,  # Verde
    'error': 0xff0000,    # Vermelho
    'info': 0x0099ff,     # Azul
    'warning': 0xffaa00,  # Laranja
}
```

Os números são códigos HEX de cores.

---

## Dados e Segurança

### P: Onde meus dados são armazenados?
**R:** Em arquivos JSON na pasta `data/`:
- `products.json` - Produtos
- `transactions.json` - Histórico de vendas

### P: Posso fazer backup dos dados?
**R:** Sim! Copie a pasta `data/` para um local seguro.

### P: Como deletar um cliente ou transação?
**R:** Edite manualmente o arquivo `data/transactions.json` (cuidado!)

### P: O `.env` é seguro?
**R:** Sim, está no `.gitignore`. Nunca commite o `.env` no Git!

---

## Problemas Comuns

### P: Bot diz "I don't have permission"
**R:**
1. Verifique as permissões do bot no servidor
2. Certifique-se de que o bot está acima de outros roles
3. Dê permissão de "Send Messages", "Embed Links", "Attach Files"

### P: Comando não é reconhecido
**R:**
- Use `!help_vendas` para listar comandos
- Certifique-se de usar o prefixo `!`
- Alguns comandos só funcionam para o owner

### P: Python says "module not found"
**R:**
```bash
pip install -r requirements.txt
```

### P: QR Code não aparece no Discord
**R:**
- Verifique se a biblioteca `qrcode` está instalada
- Certifique-se de que a chave PIX é válida
- Tente outra chave PIX

---

## Desenvolvimento e Customização

### P: Como adicionar um novo comando?
**R:** Crie um arquivo em `cogs/` com:
```python
from discord.ext import commands

class MeuCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='meucomando')
    async def meu_comando(self, ctx):
        await ctx.send("Olá!")

async def setup(bot):
    await bot.add_cog(MeuCog(bot))
```

### P: Como editar o layout do embed?
**R:** Edite o arquivo `cogs/vendas.py` e procure por `discord.Embed`:
```python
embed = discord.Embed(
    title="Título",
    description="Descrição",
    color=0x0099ff
)
```

### P: Como adicionar um banco de dados real?
**R:** Você pode usar SQLite, MongoDB, etc. Substitua as funções em `utils.py`.

---

## Suporte

### P: Onde reporto bugs?
**R:** 
1. Verifique o [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
2. Consulte os logs do bot
3. Leia a documentação do [discord.py](https://discordpy.readthedocs.io/)

### P: Como contribuir melhorias?
**R:** Faça um fork, crie uma branch, e envie um pull request!

### P: O projeto é open source?
**R:** Sim! Use livremente conforme a licença.

---

## Dicas e Truques

### 💡 Dica 1: Automatizar Confirmações
Você pode criar um sistema que confirma transações automaticamente verificando o PIX do banco.

### 💡 Dica 2: Relatórios
Use `data/transactions.json` para gerar relatórios de vendas.

### 💡 Dica 3: Sistema de Cupons
Você pode adicionar cupons desconto criando um novo cog.

### 💡 Dica 4: Notificações
Envie notificações automáticas quando um produto vende.

### 💡 Dica 5: Multi-Idioma
Use a variável de `config.py` para adicionar suporte a outros idiomas.

---

**Última atualização:** Agosto 2026  
**Versão do Bot:** 1.0.0

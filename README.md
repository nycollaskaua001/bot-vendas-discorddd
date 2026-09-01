# 🤖 Bot de Vendas Discord

Um bot Discord completo para gerenciamento e venda de produtos com suporte a PIX, QR Code customizável e controle total sobre produtos.

## 🎯 Funcionalidades

✅ **Gerenciamento de Produtos**
- Criar, editar e deletar produtos
- Ativar/desativar produtos
- Definir preços e descrições

✅ **Sistema de Vendas**
- Vitrine com embed personalizado
- QR Code PIX automático
- Suporte a banner customizado
- Registro de comprovantes

✅ **Pagamento PIX**
- Geração automática de QR Code
- Suporte a diferentes tipos de chave PIX
- Bloqueio de bancos específicos
- Validação de pagamentos

✅ **Segurança**
- Apenas o criador pode gerenciar produtos
- Produtos podem ser ativados/desativados
- Registro de todas as transações

## 📋 Pré-requisitos

- Python 3.8+
- Token do Discord Bot
- ID da Guild (servidor)
- ID do usuário (para Owner)

## 🚀 Instalação

### 1. Clone ou baixe o projeto

```bash
cd bot-vendas-discord
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Configure o arquivo .env

Copie o arquivo `.env.example` para `.env` e preencha as informações:

```bash
cp .env.example .env
```

Edite o `.env`:

```env
DISCORD_TOKEN=seu_token_do_bot_aqui
GUILD_ID=seu_guild_id_aqui
LOG_CHANNEL_ID=seu_canal_de_log_aqui
OWNER_ID=seu_user_id_aqui
PIX_KEY=sua_chave_pix_aqui
RECEIVER_NAME=Seu Nome
BANNER_PATH=assets/banner.png
QRCODE_PATH=assets/qrcode.png
BLOCKED_BANKS=Banco1,Banco2,Banco3
```

### 4. Execute o bot

```bash
python main.py
```

## 📖 Guia de Uso

### Para Administradores (Criador do Bot)

#### Adicionar Produto
```
!addproduto "Camiseta" 49.90 "Camiseta de qualidade"
```

#### Listar Todos os Produtos
```
!listprodutos
```

#### Editar Produto
```
!editproduto 1 nome "Nova Camiseta"
!editproduto 1 preco 59.90
!editproduto 1 descricao "Descrição nova"
```

#### Deletar Produto
```
!delproduto 1
```

#### Ativar/Desativar Produto
```
!toggleproduto 1
```

#### Definir Banner da Loja
```
!setbanner
[Anexar imagem]
```

#### Definir QR Code Customizado
```
!setqrcode
[Anexar imagem]
```

### Para Clientes

#### Ver Vitrine
```
!vitrine
```
Mostra todos os produtos com descrições e preços.

#### Comprar um Produto
```
!comprar 1
```
Exibe o QR Code PIX e as informações de pagamento.

#### Ver Informações de PIX
```
!pix 1
```
Mostra dados de PIX para um produto específico.

#### Enviar Comprovante
```
!comprovar Enviei o pagamento via PIX
```
Registra o comprovante para análise.

#### Ajuda
```
!help_vendas
```
Mostra todos os comandos disponíveis.

## 🏗️ Estrutura do Projeto

```
bot-vendas-discord/
├── main.py                 # Arquivo principal do bot
├── config.py               # Configurações
├── utils.py                # Funções utilitárias
├── requirements.txt        # Dependências
├── .env.example            # Exemplo de variáveis de ambiente
├── .env                    # Variáveis de ambiente (não commitar)
├── data/                   # Dados do bot
│   ├── products.json       # Produtos cadastrados
│   └── transactions.json   # Histórico de vendas
├── cogs/                   # Comandos do bot
│   ├── admin.py            # Comandos de administração
│   └── vendas.py           # Comandos de vendas
└── assets/                 # Imagens e mídia
    ├── banner.png          # Banner da loja
    └── qrcode_custom.png   # QR Code customizado
```

## 💾 Dados Salvos

### products.json
```json
{
  "1": {
    "id": 1,
    "nome": "Camiseta",
    "preco": 49.90,
    "descricao": "Camiseta de qualidade",
    "ativo": true
  }
}
```

### transactions.json
```json
[
  {
    "timestamp": "2024-01-15T10:30:00",
    "product": "Camiseta",
    "price": 49.90,
    "buyer_id": 123456789,
    "buyer_name": "User#1234",
    "payment_method": "PIX",
    "status": "pending"
  }
]
```

## 🔐 Segurança

- ✅ Apenas o owner pode gerenciar produtos
- ✅ Token salvo em variável de ambiente (.env)
- ✅ Banco de dados local (JSON)
- ✅ Validação de tipos de imagem
- ✅ Bloqueio de bancos específicos para PIX

## 🛠️ Configuração Avançada

### Bancos Bloqueados
No `.env`, você pode listar bancos que não devem ser usados:
```env
BLOCKED_BANKS=NuBank,Inter,Bradesco
```

### Diferentes Tipos de Chave PIX
Você pode usar qualquer um destes como `PIX_KEY`:
- CPF: `12345678900`
- Email: `seu@email.com`
- Telefone: `+5511999999999`
- Chave Aleatória: `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`

### Customização do Banner
Use o comando `!setbanner` para fazer upload de uma imagem que será exibida na vitrine.

### Customização do QR Code
Use o comando `!setqrcode` para fazer upload de uma imagem customizada do QR Code.

## 📊 Estatísticas

Os dados são armazenados em JSON na pasta `data/`:
- `products.json` - Lista de produtos
- `transactions.json` - Histórico de vendas

Você pode consultar esses arquivos para gerar relatórios.

## 🐛 Troubleshooting

### Bot não aparece online
- Verifique se o `DISCORD_TOKEN` está correto
- Verifique se o bot está convidado para o servidor

### Comandos não funcionam
- Verifique se está usando o prefix correto `!`
- Verifique se tem permissão (@is_owner)
- Use `!help` para listar comandos

### QR Code não funciona
- Verifique se a chave PIX está correta
- Certifique-se de que PIX_KEY está preenchido no .env

## 📝 Licença

Este projeto é de código aberto e pode ser usado livremente.

## 💬 Suporte

Para dúvidas ou problemas, consulte a documentação:
- [discord.py Documentation](https://discordpy.readthedocs.io/)
- [Discord Developer Portal](https://discord.com/developers/applications)

## 🎉 Créditos

Desenvolvido com ❤️ para a comunidade Discord.

---

**Versão:** 1.0.0  
**Data:** Agosto 2026

# 🤝 Contribuindo para o Bot de Vendas Discord

Obrigado por se interessar em contribuir! Este documento oferece diretrizes e instruções.

## 📋 Código de Conduta

Por favor, siga nosso código de conduta em todas as interações:
- Seja respeitoso e inclusivo
- Não faça assédio ou discriminação
- Aceite críticas construtivas

## 🐛 Reportando Bugs

### Antes de reportar
- Verifique se o bug já foi reportado
- Teste com a versão mais recente do código
- Leia [TROUBLESHOOTING.md](TROUBLESHOOTING.md)

### Ao reportar
Forneça:
- Descrição clara do problema
- Passos para reproduzir
- Comportamento esperado vs. atual
- Sistema operacional e versão do Python
- Mensagens de erro completas (se houver)

### Exemplo:
```
Título: Comando !comprar não funciona

Descrição:
Quando uso !comprar 1, o bot não responde.

Passos:
1. Executar !addproduto "Teste" 10.00 "Teste"
2. Usar !comprar 1
3. Bot não responde

Esperado: Deveria mostrar o QR Code
Atual: Sem resposta

Ambiente:
- Python 3.11
- Windows 11
- discord.py 2.3.2
```

## 💡 Sugerindo Novas Funcionalidades

### Antes de sugerir
- Verifique se a funcionalidade já existe
- Verifique se foi sugerida antes

### Ao sugerir
Descreva:
- Qual é a funcionalidade?
- Qual problema ela resolve?
- Exemplos de uso
- Benefícios

### Exemplo:
```
Título: Adicionar sistema de cupons de desconto

Descrição:
Permitir que administradores criem cupons que dão desconto nas compras.

Uso:
!addcupom DESCONTO10 10.5
Um cliente usa: !comprar 1 --cupom DESCONTO10

Benefício:
Promoções e fidelização de clientes
```

## 🔧 Setup de Desenvolvimento

### 1. Faça um Fork do Repositório
```bash
git clone https://github.com/seu-usuario/bot-vendas-discord.git
cd bot-vendas-discord
```

### 2. Crie uma Branch
```bash
git checkout -b feature/sua-funcionalidade
# ou para bugfixes:
git checkout -b bugfix/seu-bugfix
```

### 3. Setup do Ambiente
```bash
# Criar virtual environment
python -m venv venv

# Ativar (Linux/Mac)
source venv/bin/activate
# Ou (Windows)
venv\Scripts\activate

# Instalar dependências de desenvolvimento
pip install -r requirements-dev.txt
```

### 4. Faça suas Alterações
- Escreva código limpo e legível
- Siga a convenção de nomes Python (snake_case)
- Adicione docstrings às funções
- Teste suas mudanças

## 📝 Guia de Estilo

### Naming Conventions
```python
# Funções e variáveis: snake_case
def load_products():
    user_id = 123

# Classes: PascalCase
class VendasCog(commands.Cog):
    pass

# Constantes: UPPER_SNAKE_CASE
PIX_KEY = "chave_pix"
```

### Documentação
```python
def comprar_produto(product_id: int, user_id: int) -> bool:
    """
    Realiza a compra de um produto.
    
    Args:
        product_id: ID do produto a comprar
        user_id: ID do usuário que está comprando
        
    Returns:
        True se bem-sucedido, False caso contrário
        
    Raises:
        ValueError: Se o produto não existe
    """
    pass
```

### Commits
- Use mensagens descritivas em inglês
- Use o imperativo: "Add feature" não "Added feature"
- Referencie issues quando aplicável

Exemplos:
```
Add product filtering by price range
Fix QR code generation error (#42)
Improve performance of product listing
Refactor payment verification logic
```

## 🧪 Testes

### Executar testes
```bash
pytest tests/
```

### Criar um teste
```python
# tests/test_admin.py
import pytest
from cogs.admin import Admin

@pytest.fixture
def admin_cog(bot):
    return Admin(bot)

def test_add_product(admin_cog):
    result = admin_cog.load_products()
    assert isinstance(result, dict)
```

## 📤 Enviando Mudanças

### Antes de fazer Push
```bash
# Formatar código
black .

# Verificar erros
flake8 .

# Executar testes
pytest
```

### Fazer Commit e Push
```bash
git add .
git commit -m "Add new feature description"
git push origin feature/sua-funcionalidade
```

### Abrir Pull Request
1. Vá para o repositório no GitHub
2. Clique em "New Pull Request"
3. Compare sua branch com `main`
4. Descreva suas mudanças:
   - O que foi mudado?
   - Por quê?
   - Como testar?
   - Issues relacionadas

### Template de PR
```markdown
## Descrição
Breve descrição do que foi mudado.

## Tipo de Mudança
- [ ] Bug fix
- [ ] Nova funcionalidade
- [ ] Breaking change
- [ ] Melhoria de documentação

## Como Testar
Passos para verificar as mudanças:
1. ...
2. ...

## Checklist
- [ ] Código segue as convenções de estilo
- [ ] Sem erros de lint
- [ ] Testes passam
- [ ] Documentação atualizada
- [ ] Sem breaking changes
```

## 📚 Arquitetura do Projeto

```
bot-vendas-discord/
├── main.py              # Entrada do bot
├── config.py            # Configurações
├── utils.py             # Funções auxiliares
├── cogs/                # Extensões (plugins)
│   ├── admin.py         # Gerenciamento
│   └── vendas.py        # Sistema de vendas
└── data/                # Dados persistentes
```

### Entendendo os Cogs
Cogs são extensões do bot. Para criar uma nova:

```python
from discord.ext import commands

class MeuCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def meu_comando(self, ctx):
        await ctx.send("Oi!")

async def setup(bot):
    await bot.add_cog(MeuCog(bot))
```

## 🎓 Recursos Úteis

- [discord.py Documentation](https://discordpy.readthedocs.io/)
- [Discord Developer Portal](https://discord.com/developers/)
- [Python Style Guide (PEP 8)](https://pep8.org/)
- [Git Tutorial](https://git-scm.com/book)

## ❓ Dúvidas?

- Abra uma Issue no repositório
- Participe das Discussions
- Envie um email para suporte

## 🎉 Obrigado!

Obrigado por contribuir para melhorar o Bot de Vendas Discord!

---

**Última atualização:** Agosto 2026

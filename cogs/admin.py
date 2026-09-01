import discord
from discord.ext import commands
import json
import os
from config import PRODUCTS_FILE, COLORS, OWNER_ID, DATA_DIR

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Carregar produtos do arquivo
    def load_products(self):
        if os.path.exists(PRODUCTS_FILE):
            with open(PRODUCTS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    # Salvar produtos no arquivo
    def save_products(self, products):
        os.makedirs(DATA_DIR, exist_ok=True)
        with open(PRODUCTS_FILE, 'w', encoding='utf-8') as f:
            json.dump(products, f, ensure_ascii=False, indent=2)

    @commands.command(name='addproduto')
    @commands.is_owner()
    async def add_product(self, ctx, nome: str, preco: float, descricao: str = "Sem descrição"):
        """
        Adiciona um novo produto
        Uso: !addproduto <nome> <preço> [descrição]
        Exemplo: !addproduto "Camiseta" 49.90 "Camiseta de qualidade"
        """
        products = self.load_products()
        
        # Gerar ID único
        product_id = len(products) + 1
        
        products[str(product_id)] = {
            'id': product_id,
            'nome': nome,
            'preco': preco,
            'descricao': descricao,
            'ativo': True
        }
        
        self.save_products(products)
        
        embed = discord.Embed(
            title="✅ Produto Adicionado",
            description=f"**{nome}** foi adicionado com sucesso!",
            color=COLORS['success']
        )
        embed.add_field(name="ID", value=product_id, inline=True)
        embed.add_field(name="Preço", value=f"R$ {preco:.2f}", inline=True)
        embed.add_field(name="Descrição", value=descricao, inline=False)
        
        await ctx.send(embed=embed)

    @commands.command(name='editproduto')
    @commands.is_owner()
    async def edit_product(self, ctx, product_id: int, campo: str, *, valor):
        """
        Edita um produto existente
        Campos: nome, preco, descricao
        Uso: !editproduto <id> <campo> <novo_valor>
        """
        products = self.load_products()
        
        if str(product_id) not in products:
            await ctx.send(f"❌ Produto com ID {product_id} não encontrado!")
            return
        
        campo = campo.lower()
        if campo == 'preco':
            try:
                valor = float(valor)
            except ValueError:
                await ctx.send("❌ Preço inválido! Use um número.")
                return
        
        if campo not in ['nome', 'preco', 'descricao']:
            await ctx.send("❌ Campo inválido! Use: nome, preco ou descricao")
            return
        
        products[str(product_id)][campo] = valor
        self.save_products(products)
        
        embed = discord.Embed(
            title="✅ Produto Editado",
            description=f"Produto **{products[str(product_id)]['nome']}** atualizado!",
            color=COLORS['success']
        )
        embed.add_field(name=campo.capitalize(), value=str(valor), inline=False)
        
        await ctx.send(embed=embed)

    @commands.command(name='delproduto')
    @commands.is_owner()
    async def delete_product(self, ctx, product_id: int):
        """
        Deleta um produto
        Uso: !delproduto <id>
        """
        products = self.load_products()
        
        if str(product_id) not in products:
            await ctx.send(f"❌ Produto com ID {product_id} não encontrado!")
            return
        
        nome = products[str(product_id)]['nome']
        del products[str(product_id)]
        self.save_products(products)
        
        embed = discord.Embed(
            title="✅ Produto Deletado",
            description=f"Produto **{nome}** foi removido!",
            color=COLORS['success']
        )
        
        await ctx.send(embed=embed)

    @commands.command(name='listprodutos')
    @commands.is_owner()
    async def list_products(self, ctx):
        """
        Lista todos os produtos cadastrados
        """
        products = self.load_products()
        
        if not products:
            await ctx.send("❌ Nenhum produto cadastrado!")
            return
        
        embed = discord.Embed(
            title="📦 Produtos Cadastrados",
            color=COLORS['info']
        )
        
        for product_id, product in products.items():
            status = "✅ Ativo" if product.get('ativo', True) else "❌ Inativo"
            embed.add_field(
                name=f"[ID: {product_id}] {product['nome']}",
                value=f"R$ {product['preco']:.2f} - {product['descricao']}\n{status}",
                inline=False
            )
        
        await ctx.send(embed=embed)

    @commands.command(name='toggleproduto')
    @commands.is_owner()
    async def toggle_product(self, ctx, product_id: int):
        """
        Ativa/Desativa um produto
        Uso: !toggleproduto <id>
        """
        products = self.load_products()
        
        if str(product_id) not in products:
            await ctx.send(f"❌ Produto com ID {product_id} não encontrado!")
            return
        
        products[str(product_id)]['ativo'] = not products[str(product_id)].get('ativo', True)
        self.save_products(products)
        
        status = "✅ Ativado" if products[str(product_id)]['ativo'] else "❌ Desativado"
        embed = discord.Embed(
            title="✅ Produto Atualizado",
            description=f"{status}",
            color=COLORS['success']
        )
        
        await ctx.send(embed=embed)

    @commands.command(name='setbanner')
    @commands.is_owner()
    async def set_banner(self, ctx):
        """
        Define a imagem do banner da loja
        Responda a este comando com anexo de imagem
        """
        if not ctx.message.attachments:
            await ctx.send("❌ Anexe uma imagem para definir como banner!")
            return
        
        attachment = ctx.message.attachments[0]
        
        if not attachment.content_type.startswith('image/'):
            await ctx.send("❌ O arquivo deve ser uma imagem!")
            return
        
        banner_path = 'assets'
        os.makedirs(banner_path, exist_ok=True)
        
        await attachment.save(f"{banner_path}/banner.png")
        
        embed = discord.Embed(
            title="✅ Banner Definido",
            description="A imagem do banner foi atualizada com sucesso!",
            color=COLORS['success']
        )
        
        await ctx.send(embed=embed)

    @commands.command(name='setqrcode')
    @commands.is_owner()
    async def set_qrcode(self, ctx):
        """
        Define a imagem do QR Code customizado
        Responda a este comando com anexo de imagem
        """
        if not ctx.message.attachments:
            await ctx.send("❌ Anexe uma imagem para definir como QR Code!")
            return
        
        attachment = ctx.message.attachments[0]
        
        if not attachment.content_type.startswith('image/'):
            await ctx.send("❌ O arquivo deve ser uma imagem!")
            return
        
        qrcode_path = 'assets'
        os.makedirs(qrcode_path, exist_ok=True)
        
        await attachment.save(f"{qrcode_path}/qrcode_custom.png")
        
        embed = discord.Embed(
            title="✅ QR Code Definido",
            description="A imagem customizada do QR Code foi atualizada!",
            color=COLORS['success']
        )
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Admin(bot))

import discord
from discord.ext import commands
import json
import os
from config import PRODUCTS_FILE, COLORS, DATA_DIR, PIX_KEY, RECEIVER_NAME, BLOCKED_BANKS
import qrcode
from io import BytesIO

class Vendas(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Carregar produtos do arquivo
    def load_products(self):
        if os.path.exists(PRODUCTS_FILE):
            with open(PRODUCTS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    def generate_qr_code(self, data):
        """Gera QR Code em base64"""
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Converter para bytes
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        buffer.seek(0)
        
        return buffer

    @commands.command(name='vitrine')
    async def showcase(self, ctx):
        """
        Exibe a vitrine de produtos com embed bonito
        """
        products = self.load_products()
        
        # Filtrar apenas produtos ativos
        active_products = {k: v for k, v in products.items() if v.get('ativo', True)}
        
        if not active_products:
            await ctx.send("❌ Nenhum produto disponível no momento!")
            return
        
        # Criar embed da vitrine
        embed = discord.Embed(
            title="🛍️ NOSSA LOJA",
            description="Bem-vindo à nossa vitrine! Escolha o seu produto:",
            color=COLORS['info']
        )
        
        # Adicionar banner se existir
        if os.path.exists('assets/banner.png'):
            embed.set_image(url="attachment://banner.png")
        
        total_preco = 0
        for product_id, product in active_products.items():
            embed.add_field(
                name=f"▶️ {product['nome']}",
                value=f"**R$ {product['preco']:.2f}**\n_{product['descricao']}_\n\n`ID: {product_id}`",
                inline=False
            )
            total_preco += product['preco']
        
        embed.add_field(
            name="📋 Como Comprar?",
            value="1️⃣ Use `!comprar <ID>` para comprar\n2️⃣ Escaneie o QR Code PIX\n3️⃣ Envie o comprovante",
            inline=False
        )
        
        embed.set_footer(text=f"Total de produtos: {len(active_products)} | Use !comprar <id>")
        
        # Enviar embed com banner se existir
        if os.path.exists('assets/banner.png'):
            with open('assets/banner.png', 'rb') as f:
                file = discord.File(f, filename='banner.png')
                await ctx.send(embed=embed, file=file)
        else:
            await ctx.send(embed=embed)

    @commands.command(name='comprar')
    async def buy(self, ctx, product_id: int):
        """
        Inicia o processo de compra de um produto
        Uso: !comprar <id>
        """
        products = self.load_products()
        
        if str(product_id) not in products:
            await ctx.send(f"❌ Produto com ID {product_id} não encontrado!")
            return
        
        product = products[str(product_id)]
        
        if not product.get('ativo', True):
            await ctx.send("❌ Este produto está indisponível no momento!")
            return
        
        # Criar embed de compra
        embed = discord.Embed(
            title=f"💳 COMPRA - {product['nome']}",
            description=f"Informações do produto selecionado:",
            color=COLORS['info']
        )
        
        embed.add_field(name="Produto", value=product['nome'], inline=True)
        embed.add_field(name="Preço", value=f"R$ {product['preco']:.2f}", inline=True)
        embed.add_field(name="Descrição", value=product['descricao'], inline=False)
        
        # Gerar dados PIX
        pix_data = f"00020126580014br.gov.bcb.pix0136{PIX_KEY}52040000530398654{int(product['preco']*100):010d}5303986540510.005802BR5913{RECEIVER_NAME}6009SAO PAULO62410503***63047D91"
        
        # Gerar QR Code
        qr_buffer = self.generate_qr_code(pix_data)
        qr_file = discord.File(qr_buffer, filename='qrcode.png')
        
        embed.set_image(url="attachment://qrcode.png")
        embed.add_field(
            name="📱 PIX",
            value=f"**Chave PIX:** `{PIX_KEY}`\n**Valor:** R$ {product['preco']:.2f}",
            inline=False
        )
        embed.add_field(
            name="✅ Próximos Passos",
            value="1️⃣ Escaneie o QR Code acima\n2️⃣ Faça o pagamento de R$ {:.2f}\n3️⃣ Use `!comprovar <mensagem>` para enviar o comprovante".format(product['preco']),
            inline=False
        )
        
        embed.set_footer(text=f"⏰ Válido por 30 minutos | ID: {product_id}")
        
        await ctx.send(embed=embed, file=qr_file)

    @commands.command(name='pix')
    async def pix_info(self, ctx, product_id: int = None):
        """
        Exibe as informações de PIX para pagamento
        Se product_id for omitido, exibe apenas a chave PIX
        """
        if product_id is None:
            embed = discord.Embed(
                title="💰 Informações PIX",
                description=f"Chave PIX para pagamentos",
                color=COLORS['info']
            )
            embed.add_field(name="Chave PIX", value=f"`{PIX_KEY}`", inline=False)
            embed.add_field(name="Recebedor", value=RECEIVER_NAME, inline=False)
            embed.add_field(
                name="Bancos Bloqueados",
                value=", ".join(BLOCKED_BANKS) if BLOCKED_BANKS else "Nenhum",
                inline=False
            )
            await ctx.send(embed=embed)
            return
        
        products = self.load_products()
        if str(product_id) not in products:
            await ctx.send(f"❌ Produto com ID {product_id} não encontrado!")
            return
        
        product = products[str(product_id)]
        
        embed = discord.Embed(
            title=f"💰 PIX - {product['nome']}",
            color=COLORS['info']
        )
        
        embed.add_field(name="Produto", value=product['nome'], inline=True)
        embed.add_field(name="Valor", value=f"R$ {product['preco']:.2f}", inline=True)
        embed.add_field(name="Chave PIX", value=f"`{PIX_KEY}`", inline=False)
        embed.add_field(name="Recebedor", value=RECEIVER_NAME, inline=False)
        
        if BLOCKED_BANKS:
            embed.add_field(
                name="⚠️ Bancos Bloqueados",
                value="NÃO use os seguintes bancos:\n" + ", ".join(BLOCKED_BANKS),
                inline=False
            )
            embed.color = COLORS['warning']
        
        qr_buffer = self.generate_qr_code(f"00020126580014br.gov.bcb.pix0136{PIX_KEY}52040000530398654{int(product['preco']*100):010d}5303986540510.005802BR5913{RECEIVER_NAME}6009SAO PAULO62410503***63047D91")
        qr_file = discord.File(qr_buffer, filename='qrcode.png')
        
        embed.set_image(url="attachment://qrcode.png")
        
        await ctx.send(embed=embed, file=qr_file)

    @commands.command(name='comprovar')
    async def verify_payment(self, ctx, *, mensagem):
        """
        Registra comprovante de pagamento
        Uso: !comprovar <ID do produto ou descrição>
        """
        embed = discord.Embed(
            title="✅ Comprovante Recebido",
            description=f"Obrigado pela compra!",
            color=COLORS['success']
        )
        
        embed.add_field(name="Usuário", value=ctx.author.mention, inline=True)
        embed.add_field(name="Informação", value=mensagem, inline=False)
        embed.add_field(
            name="Status",
            value="Seu comprovante foi enviado para análise. Você receberá uma confirmação em breve!",
            inline=False
        )
        
        await ctx.send(embed=embed)
        
        # Log em um canal se configurado
        # await log_channel.send(f"Novo comprovante de {ctx.author}: {mensagem}")

    @commands.command(name='help_vendas')
    async def help_vendas(self, ctx):
        """
        Exibe ajuda sobre os comandos de vendas
        """
        embed = discord.Embed(
            title="📖 Ajuda - Sistema de Vendas",
            color=COLORS['info']
        )
        
        embed.add_field(
            name="!vitrine",
            value="Exibe todos os produtos disponíveis",
            inline=False
        )
        embed.add_field(
            name="!comprar <id>",
            value="Inicia a compra de um produto",
            inline=False
        )
        embed.add_field(
            name="!pix [id]",
            value="Exibe informações de PIX (com ou sem ID de produto)",
            inline=False
        )
        embed.add_field(
            name="!comprovar <mensagem>",
            value="Registra o comprovante de pagamento",
            inline=False
        )
        
        embed.set_footer(text="Use !help_admin para comandos do administrador")
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Vendas(bot))

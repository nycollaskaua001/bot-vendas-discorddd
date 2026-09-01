import discord
from discord.ext import commands
import os
import logging
from config import DISCORD_TOKEN, INTENTS, DATA_DIR, GUILD_ID

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('bot')

# Criar diretório de dados se não existir
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Criar bot
intents = discord.Intents.default()
intents.message_content = INTENTS['message_content']
intents.members = INTENTS['members']

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    logger.info(f'{bot.user} está online!')
    
    # Carregar todos os cogs
    cogs_dir = 'cogs'
    if os.path.exists(cogs_dir):
        for filename in os.listdir(cogs_dir):
            if filename.endswith('.py'):
                try:
                    await bot.load_extension(f'cogs.{filename[:-3]}')
                    logger.info(f'Carregado: {filename}')
                except Exception as e:
                    logger.error(f'Erro ao carregar {filename}: {e}')

if __name__ == '__main__':
    bot.run(DISCORD_TOKEN)

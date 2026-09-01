import os
from dotenv import load_dotenv

load_dotenv()

# Bot Configuration
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = int(os.getenv('GUILD_ID', 0))
LOG_CHANNEL_ID = int(os.getenv('LOG_CHANNEL_ID', 0))
OWNER_ID = int(os.getenv('OWNER_ID', 0))

# PIX Configuration
PIX_KEY = os.getenv('PIX_KEY')
RECEIVER_NAME = os.getenv('RECEIVER_NAME', 'Loja')

# Paths
BANNER_PATH = os.getenv('BANNER_PATH', 'assets/banner.png')
QRCODE_PATH = os.getenv('QRCODE_PATH', 'assets/qrcode.png')

# Blocked Banks
BLOCKED_BANKS = [bank.strip() for bank in os.getenv('BLOCKED_BANKS', '').split(',') if bank.strip()]

# Bot Intents
INTENTS = {
    'message_content': True,
    'guilds': True,
    'guild_messages': True,
    'direct_messages': True,
    'members': True,
}

# Colors (Discord embeds)
COLORS = {
    'success': 0x00ff00,
    'error': 0xff0000,
    'info': 0x0099ff,
    'warning': 0xffaa00,
}

# Database
DATA_DIR = 'data'
PRODUCTS_FILE = os.path.join(DATA_DIR, 'products.json')
TRANSACTIONS_FILE = os.path.join(DATA_DIR, 'transactions.json')

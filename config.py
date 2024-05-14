import os
from telethon import TelegramClient

api_id = os.environ.get('API_ID', 24665357)
api_hash = os.environ.get('API_HASH', "beb7e4b83ada668fa85f9a9b56338f1d")
bot_token = os.environ.get('BOT_TOKEN', "6700540841:AAEzEG75XEQXqfTGmIvy136zVclAUBxQKOI")
skeleton_url = os.environ.get('SKELETON_URL')


bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)



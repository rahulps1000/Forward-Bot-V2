from dotenv import load_dotenv
from os import environ, path

load_dotenv()

if path.exists("bot_config.py"):
    from bot_config import Config
else:
    class Config(object):
        APP_ID = int(environ.get("APP_ID", None))
        API_HASH = environ.get("API_HASH", None)
        BOT_TOKEN = environ.get("BOT_TOKEN", None)
        BOT_WORKERS = int(environ.get("BOT_WORKERS", 40))
        SUDO_USERS = environ.get("SUDO_USERS", None)
        DB_URI = environ.get("DB_URI", None)
        SESSION_NAME = environ.get("SESSION_NAME", "test")
        MULTI_USER_MODE = environ.get('MULTI_USER_MODE', '').lower() in ['true', '1']
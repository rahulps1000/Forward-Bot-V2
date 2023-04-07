import logging
from logging.handlers import RotatingFileHandler
from pyrogram import Client
from Bot.config import Config

# Important import for addons
from pyropatch import listen, flood_handler, command_handler

# ---------- ---------- ---------- ----------

LOG_FILE_NAME = "codexbotz.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)


# ---------- ---------- ---------- ----------

class CodeXBotz(Client):
    def __init__(self):
        super().__init__(
            "bot",
            api_hash=Config.API_HASH,
            api_id=Config.APP_ID,
            plugins={
                "root": "Bot/plugins"
            },
            workers=Config.BOT_WORKERS,
            bot_token=Config.BOT_TOKEN
        )
        self.bot_details = None
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        bot_details = await self.get_me()
        self.LOGGER(__name__).info(f"@{bot_details.username}  started!")
        self.LOGGER(__name__).info("Created by Code X Botz\nhttps://t.me/CodeXBotz")
        self.bot_details = bot_details

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")

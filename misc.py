import os

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from libs.database import db
from libs.utils import get_logger

# create root logger
logger = get_logger("root")

# bot initialization
logger.info("Launching Bot")

# replace with actual token
bot = Bot(token=os.getenv("BOT_TOKEN"))

# State storage initialization
logger.info("Creating Redis States Storage")

# replace with actual password
storage = RedisStorage2(
    host=os.getenv("REDIS_HOST"), port=int(os.getenv("REDIS_PORT")), password=os.getenv("REDIS_PASSWORD")
)

# Dispatcher initialization
logger.info("Launching Dispatcher")
dp = Dispatcher(bot, storage=storage)


async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()

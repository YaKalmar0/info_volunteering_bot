import asyncio

from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor

import handlers  # crucial import
from libs.utils import get_logger
from misc import db, dp

logger = get_logger("ping_logger")


async def db_ping(wait: int):
    while True:
        await asyncio.sleep(wait)
        logger.info("Scheduled MySQL connection ping")
        db.ping()


# launch long polling
if __name__ == "__main__":
    dp.middleware.setup(LoggingMiddleware())
    loop = asyncio.get_event_loop()
    loop.create_task(db_ping(3600))
    executor.start_polling(dp)

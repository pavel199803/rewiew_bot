import asyncio
import logging
import sqlite3

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

import config
from review_handlers import router


async def main():
    bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    # connection = sqlite3.connect('chat_bot.db')
    # cursor = connection.cursor()
    # scheduler = AsyncIOScheduler()

    # scheduler.start()
    # scheduler.add_job(get_tours_day, 'interval', seconds=3, args=(bot,))
    # while True:
    # await asyncio.sleep(1000)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

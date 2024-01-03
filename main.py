import logging
import asyncio
import sys

from aiogram.filters.callback_data import CallbackData
from create_bot import dp,bot 
from routers import bot_routers

async def main():
    cb = CallbackData()
    dp.include_router(bot_routers.router)
    await dp.start_polling(bot)



if __name__ == "__main__":
    print("work")
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

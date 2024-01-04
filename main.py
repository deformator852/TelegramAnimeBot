from create_bot import dp, bot
from routers import bot_routers
import logging
import asyncio
import sys


async def main() -> None:
    dp.include_router(bot_routers.router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

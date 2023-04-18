from aiogram.utils import executor
from create_bot import dp
from handlers import anime_list

anime_list.register_handlers_anime_list(dp)
if __name__ == '__main__':
    executor.start_polling(skip_updates=True,dispatcher=dp)


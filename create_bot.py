from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
import os
import sqlite3

TOKEN = ""
bot: Bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
dp: Dispatcher = Dispatcher()
data_base: sqlite3.Connection = sqlite3.connect(
    os.path.join(os.getcwd(), "database", "anime.db")
)
ROOT_ADMIN = 6672886067

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import sqlite3
TOKEN = ""
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
data_base = sqlite3.connect('/home/nikita/PycharmProjects/user_bot/database/anime.db')
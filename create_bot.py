from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode
import os
import sqlite3

TOKEN = "6603101405:AAGSTkBKgjuzxzTFE7GYUYJhp7zZXXOFrIU"
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()
data_base = sqlite3.connect(os.path.join(os.getcwd(),"database","anime.db"))

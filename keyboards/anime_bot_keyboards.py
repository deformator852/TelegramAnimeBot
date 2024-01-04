import sqlite3
from typing import List, Tuple
from create_bot import data_base
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

cur: sqlite3.Cursor = data_base.cursor()


async def take_anime_names() -> List[Tuple[str]]:
    anime_names: List[Tuple[str]] = cur.execute("SELECT name FROM anime;").fetchall()
    return anime_names


class Keyboards:
    @staticmethod
    async def kb_bot() -> ReplyKeyboardMarkup:
        builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
        builder.button(text="/Anime_info")
        builder.button(text="/Output_the_anime_list")
        builder.button(text="/AnimeByReleaseDate")
        builder.button(text="/Shonen")

        builder.adjust(1)
        return builder.as_markup()

    @staticmethod
    async def kb_anime() -> InlineKeyboardMarkup:
        anime_names: List[Tuple[str]] = await take_anime_names()
        builder = InlineKeyboardBuilder()
        for anime_name in anime_names:
            builder.button(text=anime_name[0], callback_data="anime_" + anime_name[0])
        builder.adjust(2)
        return builder.as_markup()

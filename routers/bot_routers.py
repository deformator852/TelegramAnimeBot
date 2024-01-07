import os
from typing import List, Tuple
from aiogram.types.callback_query import CallbackQuery
from aiogram.types.input_file import FSInputFile
from create_bot import bot, data_base, dp, ROOT_ADMIN
from aiogram import types
from aiogram import F
from aiogram import Router
from keyboards.anime_bot_keyboards import Keyboards
from aiogram.filters.command import Command
from aiogram.utils.media_group import MediaGroupBuilder
import re
import sqlite3

router = Router()
cur: sqlite3.Cursor = data_base.cursor()
keyboards: Keyboards = Keyboards()


@router.message(Command("start"))
async def command_start(message: types.Message) -> None:
    reply_markup = (
        await keyboards.kb_admin()
        if message.from_user.id == ROOT_ADMIN
        else await keyboards.kb_bot()
    )
    await message.answer("You started anime bot!", reply_markup=reply_markup)


@router.message(F.text == "/Anime list by genres")
async def command_anime_list_by_genres(message: types.Message) -> None:
    anime_list: List[Tuple[str, str]] = cur.execute(
        "SELECT name,genre FROM anime"
    ).fetchall()
    for anime in anime_list:
        await message.answer("Name: " + anime[0] + " | Genre: " + anime[1])


@router.message(F.text == "/Anime list")
async def command_anime_info(message: types.Message) -> None:
    await message.answer(
        "anime list:", reply_markup=await keyboards.kb_anime()
    )  # pyright:ignore


@router.message(F.text == "/Anime by release date")
async def command_anime_by_release_date(message: types.Message) -> None:
    anime_by_release_date = cur.execute(
        "SELECT data_release,name FROM anime"
    ).fetchall()
    anime_by_release_date.sort()
    for anime in anime_by_release_date:
        await bot.send_message(message.from_user.id, anime[1] + " — " + anime[0])


@router.message(F.text == "/Shonen")
async def command_shonen(message: types.Message) -> None:
    senen_anime = cur.execute(r"SELECT name,genre FROM anime").fetchall()
    for anime in senen_anime:
        if re.search(r"[Ss]honen", anime[1]):
            await bot.send_message(message.from_user.id, anime[0])


@router.callback_query(F.data.startswith("anime_"))
async def command_anime_list(callback_query: CallbackQuery) -> None:
    anime_name: str = callback_query.data[6:]
    anime: List[Tuple[int, str, str, int, str]] = cur.execute(
        "SELECT * FROM anime WHERE name=?", (anime_name,)
    ).fetchall()

    if anime:
        media_group: MediaGroupBuilder = MediaGroupBuilder()
        anime_directory: str = anime[0][5]

        for image in os.listdir(anime_directory):
            media_group.add(
                type="photo", media=FSInputFile(os.path.join(anime_directory, image))
            )  # pyright:ignore
        await callback_query.message.answer_media_group(media=media_group.build())
        await callback_query.message.answer(
            f"Name - {anime[0][1]}.Genre - {anime[0][3]}.Release date - {anime[0][4]}"
        )
        await callback_query.message.answer(f"Description - {anime[0][2]} ")

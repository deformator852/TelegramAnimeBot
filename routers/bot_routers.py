import os
from typing import List, Tuple
from aiogram.types.callback_query import CallbackQuery
from aiogram.types.input_file import FSInputFile
from create_bot import bot, data_base, dp
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
    await message.answer(
        "You started anime bot!",
        reply_markup=await keyboards.kb_bot(),  # pyright:ignore
    )


@router.message(Command("Output_the_anime_list"))
async def command_output_anime_list(message: types.Message) -> None:
    anime_list: List[Tuple[str, str]] = cur.execute(
        "SELECT name,genre FROM anime"
    ).fetchall()
    for anime in anime_list:
        await message.answer("Name: " + anime[0] + " | Genre: " + anime[1])


@router.message(Command("Anime_info"))
async def command_anime_info(message: types.Message) -> None:
    await message.answer(
        "anime list:", reply_markup=await keyboards.kb_anime()
    )  # pyright:ignore


@router.message(Command("AnimeByReleaseDate"))
async def command_Anime_ByReleaseDate(message: types.Message) -> None:
    anime_by_release_date = cur.execute(
        "SELECT data_release,name FROM anime"
    ).fetchall()
    anime_by_release_date.sort()
    for anime in anime_by_release_date:
        await bot.send_message(message.from_user.id, anime[1] + " — " + anime[0])


@router.message(Command("BackMenu"))
async def command_BackMenu(message: types.Message) -> None:
    await bot.send_message(
        message.from_user.id, "⁠", reply_markup=await keyboards.kb_bot()
    )  # pyright:ignore


@router.message(Command("Shonen"))
async def command_Shonen(message: types.Message) -> None:
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
            image_path: str = os.path.join(anime_directory, image)
            media_group.add(
                type="photo", media=FSInputFile(os.path.join(anime_directory, image))
            )
        await callback_query.message.answer_media_group(media=media_group.build())

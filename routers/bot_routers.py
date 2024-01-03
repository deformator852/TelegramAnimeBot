from aiogram.types.callback_query import CallbackQuery
from create_bot import bot, data_base, dp
from aiogram import types
from aiogram import F
from aiogram import Router
from keyboards.anime_bot_keyboards import Keyboards
from aiogram.filters.command import Command
import re
import sqlite3

router = Router()
con: sqlite3.Cursor = data_base.cursor()
keyboards: Keyboards = Keyboards()


async def take_info(message, ID):
    anime_list = con.execute(f"SELECT name,content,images FROM anime WHERE ID = {ID} ")
    for anime in anime_list:
        await bot.send_message(message.from_user.id, "Name: " + anime[0])
        await bot.send_message(message.from_user.id, anime[1])
        await bot.send_photo(message.from_user.id, types.InputFile(anime[2]))
        return


@router.message(Command("start"))
async def command_start(message: types.Message) -> None:
    await message.answer(
        "You started anime bot!",
        reply_markup=await keyboards.kb_bot(),  # pyright:ignore
    )


@router.message(Command("Output_the_anime_list"))
async def command_output_anime_list(message: types.Message) -> None:
    anime_list = con.execute("SELECT name,genre FROM anime")
    for anime in anime_list:
        await message.answer("Name: " + anime[0] + " | Genre: " + anime[1])


@router.message(Command("Anime_info"))
async def command_anime_info(message: types.Message) -> None:
    await message.answer(
        "anime list:", reply_markup=await keyboards.kb_anime()
    )  # pyright:ignore


@router.message(Command("AnimeByReleaseDate"))
async def command_Anime_ByReleaseDate(message: types.Message):
    data = con.execute("SELECT data_release,name FROM anime")
    data = list(data)
    data.sort()
    for d in data:
        await bot.send_message(message.from_user.id, d[1] + " — " + d[0])


@router.message(Command("BackMenu"))
async def command_BackMenu(message: types.Message):
    await bot.send_message(
        message.from_user.id, "⁠", reply_markup=await keyboards.kb_bot()
    )  # pyright:ignore


@router.message(Command("Shonen"))
async def command_Shonen(message: types.Message):
    data = con.execute(r"SELECT name,genre FROM anime")
    for d in data:
        if re.search(r"[Ss]honen", d[1]):
            await bot.send_message(message.from_user.id, d[0])


@router.callback_query(F.data.startswith("anime_"))
async def command_anime_list(callback_query: CallbackQuery):
    anime = con.execute(f"SELECT * FROM anime WHERE name='{callback_query.data[6:]}'").fetchall()
    if anime:
        await callback_query.message.answer(anime[0][1])


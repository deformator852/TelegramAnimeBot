from aiogram import Router, F
from aiogram.filters.logic import and_f
from aiogram.types import Message
from custom_filters.custom_filters import IsAdminFilter  # pyright:ignore
from aiogram.fsm.context import FSMContext
from states import AddNewAnimeState

router: Router = Router()


@router.message(and_f(IsAdminFilter(F.text), F.text == "/Add new anime"))
async def command_add_new_anime(message: Message, state: FSMContext) -> None:
    await state.set_state(AddNewAnimeState.NAME)
    await message.answer("Write the anime name: ")


@router.message(AddNewAnimeState.NAME)
async def command_get_name_set_genres(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    await state.set_state(AddNewAnimeState.GENRES)
    await message.answer("Write the anime genres: ")


@router.message(AddNewAnimeState.GENRES)
async def command_get_genres_set_release_date(
    message: Message, state: FSMContext
) -> None:
    await state.update_data(genres=message.text)
    await state.set_state(AddNewAnimeState.RELEASE_DATE)
    await message.answer("Write the anime release date: ")


@router.message(AddNewAnimeState.RELEASE_DATE)
async def command_get_release_date_set_description(
    message: Message, state: FSMContext
) -> None:
    await state.update_data(release_date=message.text)
    await state.set_state(AddNewAnimeState.ANIME_DESCRIPTION)
    await message.answer("Write the anime description: ")


@router.message(AddNewAnimeState.ANIME_DESCRIPTION)
async def command_get_description_set_images(
    message: Message, state: FSMContext
) -> None:
    await state.update_data(anime_description=message.text)
    await state.set_state(AddNewAnimeState.IMAGES)
    await message.answer("Send the anime images: ")


@router.message(AddNewAnimeState.IMAGES)
async def command_get_images_and_finally(message: Message, state: FSMContext) -> None:
    print(await state.get_data())
    await state.clear()

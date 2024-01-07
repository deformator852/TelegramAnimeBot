from aiogram.fsm.state import State, StatesGroup


class AddNewAnimeState(StatesGroup):
    NAME = State()
    GENRES = State()
    RELEASE_DATE = State()
    ANIME_DESCRIPTION = State()
    IMAGES = State()

from aiogram.dispatcher.filters.state import State, StatesGroup

class GetAge(StatesGroup):
    getting_age = State()

class Music_admin(StatesGroup):
    getting_file_music = State()
    getting_name_music = State()
    getting_singer_music = State()

class Music_user(StatesGroup):
    getting_name_music = State()
    getting_singer_music = State()
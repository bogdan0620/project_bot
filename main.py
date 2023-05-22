from aiogram import Bot, Dispatcher, executor
import buttons
from states import *
from token2 import TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardRemove
import database

bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def cmd_start(message):
    user_id = message.from_user.id
    checker = database.cheсk_user(user_id)
    if checker:
        await message.answer_sticker('CAACAgIAAxkBAAIFYmRjeHZS7w1EnHLodGf22k7GXGT3AAKTLQACrFEYS3DrE5B4jXmXLwQ')
        await message.answer('Выберите раздел ⬇️', reply_markup=buttons.menu_kb())
    else:
        await message.answer_sticker('CAACAgIAAxkBAAIFYmRjeHZS7w1EnHLodGf22k7GXGT3AAKTLQACrFEYS3DrE5B4jXmXLwQ')
        await message.answer('Привет. Это бот для скачивания музыки 🎶\nВведите ваш возраст', reply_markup=buttons.age_kb())
        await GetAge.getting_age.set()

users_ages = [str(i) for i in range(10, 81)]

@dp.message_handler(state=GetAge.getting_age, content_types=['text'])
async def age_user(message, state=GetAge.getting_age):
    user_answer = message.text
    if user_answer == "Зачем нужен возраст?":
        await message.answer('Возраст нужен для наилучшей персонализации музыки под определенный возраст (скоро)\nВведите возраст', reply_markup=ReplyKeyboardRemove())

    elif user_answer in users_ages:
        age = message.text
        tg_id = message.from_user.id
        name = message.from_user.full_name
        database.add_user(tg_id, name, age)
        await message.answer('Выберите раздел ⬇️', reply_markup=buttons.menu_kb())
        await state.finish()

    else:
        await message.answer('Введите корректный возраст\n(Ограничение от 10 до 80)')


@dp.message_handler(content_types=['text'], state=Music_user.getting_name_music)
async def getting_name(message, state=Music_user.getting_name_music):
    m = message.text
    user = database.get_music_name(m)
    if user:
        result1 = '⤵️ Вот что еще есть в базе:\n\n'
        for i in user:
            result1 += f'{i[0]}. Название: {i[2]}\nИсполнитель: {i[3]}\n'
            result2 = f'{i[1]}'
        await message.answer_audio(result2)
        await message.answer(result1, reply_markup=buttons.menu_kb())
    else:
        await message.answer('Ничего не найдено 📂', reply_markup=buttons.menu_kb())
    await state.finish()

@dp.message_handler(content_types=['text'], state=Music_user.getting_singer_music)
async def getting_singer(message, state=Music_user.getting_singer_music):
    m = message.text
    user = database.get_music_singer(m)
    if user:
        result1 = '⤵️ Вот что еще есть в базе:\n\n'
        for i in user:
            result1 += f'{i[0]}. Название: {i[2]}\nИсполнитель: {i[3]}\n'
            result2 = f'{i[1]}'
        await message.answer_audio(result2)
        await message.answer(result1, reply_markup=buttons.menu_kb())
    else:
        await message.answer('Ничего не найдено 📂', reply_markup=buttons.menu_kb())\

@dp.message_handler(content_types=['text'], state=Music_user.getting_num_music)
async def getting_singer(message, state=Music_user.getting_num_music):
    m = message.text
    user = database.get_music_num(m)
    if user:
        result1 = '⤵️ Вот что есть в базе:\n\n'
        for i in user:
            result1 += f'{i[0]}. Название: {i[2]}\nИсполнитель: {i[3]}\n'
            result2 = f'{i[1]}'
        await message.answer_audio(result2)
        await message.answer(result1, reply_markup=buttons.menu_kb())
    else:
        await message.answer('Ничего не найдено 📂', reply_markup=buttons.menu_kb())

    await state.finish()


@dp.message_handler(commands=['admin'])
async def login_admin(message):
    if message.from_user.id == 1097387511:
        await message.answer('Вы вошли как администратор 🔓\nВыберите раздел ⬇️', reply_markup=buttons.admin_kb())
    else:
        await message.answer('Вы не являетесь администратором 🔒\nВыберите раздел ⬇️', reply_markup=buttons.menu_kb())


@dp.message_handler(lambda message: message.text == 'Добавить музыку 📨')
async def add_music(message):
    if message.from_user.id == 1097387511:
        await message.answer('Отправьте файл музыки 💿', reply_markup=ReplyKeyboardRemove())
        await Music_admin.getting_file_music.set()
    else:
        await message.answer('Вы не являетесь администратором 🔒\nВыберите раздел ⬇️', reply_markup=buttons.menu_kb())


@dp.message_handler(content_types=['audio'], state=Music_admin.getting_file_music)
async def add_file(message, state=Music_admin.getting_file_music):
    user_file = message.audio.file_id
    await state.update_data(file_id=user_file)
    await message.answer('Введите название 📝', reply_markup=ReplyKeyboardRemove())
    await Music_admin.getting_name_music.set()

@dp.message_handler(content_types=['text'], state=Music_admin.getting_name_music)
async def add_name(message, state=Music_admin.getting_name_music):
    name_file = message.text
    await state.update_data(name=name_file)
    await message.answer('Введите исполнителя 📝', reply_markup=ReplyKeyboardRemove())
    await Music_admin.getting_singer_music.set()

@dp.message_handler(content_types=['text'], state=Music_admin.getting_singer_music)
async def add_singer(message, state=Music_admin.getting_singer_music):
    singer_file = message.text
    all_info = await state.get_data()
    tg_file_id = all_info.get('file_id')
    name = all_info.get('name')
    singer = singer_file
    database.add_music(tg_file_id, name, singer)
    await message.answer('Трек успешно добавлен в базу ✅')
    await state.finish()
    await message.answer('Выберите действие ⬇️', reply_markup=buttons.admin_kb())

@dp.message_handler(lambda message: message.text == 'Список пользователей')
async def list_users(message):
    if message.from_user.id == 1097387511:
        user = database.get_users()
        if user:
            users = ''
            for i in user:
                users += f'{i[0]}. Имя: {i[2]}\nВозраст: {i[3]}\nTG ID: {i[1]}\n'
            await message.answer(users, reply_markup=buttons.admin_kb())
        else:
            await message.answer('База пуста 📂', reply_markup=buttons.admin_kb())
@dp.message_handler(lambda message: message.text == 'Список возрастов пользователей')
async def list_users_age(message):
    if message.from_user.id == 1097387511:
        user = database.get_users()
        if user:
            users = ''
            for i in user:
                users += f'{i[0]}. Возраст: {i[3]}\n'
            await message.answer(users, reply_markup=buttons.admin_kb())
        else:
            await message.answer('База пуста 📂', reply_markup=buttons.admin_kb())

    else:
        await message.answer('Вы не являетесь администратором 🔒т\nВыберите раздел ⬇️', reply_markup=buttons.menu_kb())

@dp.message_handler(content_types=['text'])
async def search_music(message):
    if message.text == 'Найти музыку по названию 🔎':
        await message.answer('Введите название', reply_markup=ReplyKeyboardRemove())
        await Music_user.getting_name_music.set()

    elif message.text == 'Найти музыку по исполнителю 🔎':
        await message.answer('Введите имя', reply_markup=ReplyKeyboardRemove())
        await Music_user.getting_singer_music.set()

    elif message.text == 'Выбрать музыку по номеру 🔢':
        await message.answer('Введите номер', reply_markup=ReplyKeyboardRemove())
        await Music_user.getting_num_music.set()

    else:
        if message.text == '/admin' and message.from_user.id == 1097387511:
            await message.answer('Вы вошли как администратор 🔓\nВыберите раздел ⬇️', reply_markup=buttons.admin_kb())

        elif message.text == '/admin':
            await message.answer('Вы не являетесь администратором 🔒\nВыберите раздел ⬇️', reply_markup=buttons.menu_kb())

        elif message.text == '/catalog' and message.from_user.id == 1097387511:
            user = database.get_all_music()
            if user:
                catalog = '🧾 Каталог:\n\n'
                for i in user:
                        catalog += f'{i[0]}. Название: {i[2]}\nИсполнитель: {i[3]}\n'
                await message.answer(catalog, reply_markup=buttons.admin_kb())
            else:
                await message.answer('База пуста 📂', reply_markup=buttons.admin_kb())

        elif message.text == '/catalog':
            user = database.get_all_music()
            if user:
                catalog = '🧾 Каталог:\n\n'
                for i in user:
                    catalog += f'{i[0]}. Название: {i[2]}\nИсполнитель: {i[3]}\n'
                await message.answer(catalog, reply_markup=buttons.menu_kb())
            else:
                await message.answer('База пуста 📂', reply_markup=buttons.menu_kb())

        else:
            await message.answer('Выберите раздел ⬇️', reply_markup=buttons.menu_kb())



@dp.message_handler()
async def answer_not(message):
    await message.answer('Не понимаю', reply_markup=buttons.menu_kb())





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
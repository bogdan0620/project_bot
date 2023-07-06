from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


def back_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('◀️ Назад')
    kb.add(button)
    return kb


def age_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Зачем нужен возраст?')
    kb.add(button)
    return kb


def menu_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    button0 = KeyboardButton('Выбрать музыку по номеру 🔢')
    button = KeyboardButton('Найти музыку по названию 🔎')
    button2 = KeyboardButton('Найти музыку по исполнителю 🔎')
    buttonanswer = KeyboardButton('Как искать?')
    kb.add(buttonanswer)
    return kb


def admin_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    button = KeyboardButton('Добавить музыку 📨')
    button_user = KeyboardButton('Список пользователей')
    button_user2 = KeyboardButton('Список возрастов пользователей')
    button2 = KeyboardButton('⏪ Выйти из меню администратора')
    kb.add(button, button_user, button_user2, button2)
    return kb


def main_menu_kb(music_from_db):
    # Создаем пространство для кнопок
    kb = InlineKeyboardMarkup(row_width=1)

    # создаем кнопки (несгораемые)
    # order = InlineKeyboardButton(text='Оформить заказ', callback_data='order')
    # cart = InlineKeyboardButton(text='Корзина', callback_data='cart')

    # Генерация кнопок с товарами(берем из базы)
    # создаем кнопки с продуктами
    all_music = [InlineKeyboardButton(text=f'{i[3]} – {i[2]}', callback_data=i[0])
                 for i in music_from_db]

    # Объединить пространство с кнопками
    kb.add(*all_music)
    # https://telq.org/question/62bef641b2d5debe9e082d3f

    # Возвращаем кнопки
    return kb

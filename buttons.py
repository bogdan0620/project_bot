from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import database

def age_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Зачем нужен возраст?')
    kb.add(button)
    return kb

def ok_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Хорошо')
    kb.add(button)
    return kb

def menu_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    button = KeyboardButton('Найти музыку по названию')
    button2 = KeyboardButton('Найти музыку по исполнителю')
    # button3 = KeyboardButton('Рандомные 5 песен')
    kb.add(button, button2)
    return kb

# def menu_a_kb():
#     kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
#     button = KeyboardButton('Найти музыку по названию')
#     button2 = KeyboardButton('Рандомные 5 песен')
#     button3 = KeyboardButton('Войти как администратор')
#     kb.add(button, button2, button3)
#     return kb

def add_music_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    button = KeyboardButton('Добавить музыку')
    button2 = KeyboardButton('Выйти из меню администратора')
    kb.add(button, button2)
    return kb
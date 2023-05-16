from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import database

def age_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Зачем нужен возраст?')
    kb.add(button)
    return kb


def menu_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    button = KeyboardButton('Найти музыку по названию 🔎')
    button2 = KeyboardButton('Найти музыку по исполнителю 🔎')
    kb.add(button, button2)
    return kb


def admin_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    button = KeyboardButton('Добавить музыку 📨')
    button_user = KeyboardButton('Список пользователей')
    button_user2 = KeyboardButton('Список возрастов пользователей')
    button2 = KeyboardButton('⏪ Выйти из меню администратора')
    kb.add(button, button_user, button_user2, button2)
    return kb

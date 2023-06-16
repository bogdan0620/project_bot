import sqlite3

connection = sqlite3.connect('users.db')
sql = connection.cursor()

sql.execute('CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY AUTOINCREMENT, tg_id INTEGER, name TEXT, age INTEGER);')
sql.execute('CREATE TABLE IF NOT EXISTS music (music_id INTEGER PRIMARY KEY AUTOINCREMENT, tg_file_id INTEGER, name TEXT, singer TEXT);')
connection.commit()

def add_user(tg_id, name, age):
    connection = sqlite3.connect('users.db')
    sql = connection.cursor()
    user = sql.execute('SELECT * FROM users WHERE tg_id = ?;', (tg_id, )).fetchone()
    if not user:
        sql.execute('INSERT INTO users (tg_id, name, age) VALUES (?, ?, ?);', (tg_id, name, age))
        connection.commit()

def get_users():
    connection = sqlite3.connect('users.db')
    sql = connection.cursor()
    users = sql.execute('SELECT * FROM users;').fetchall()
    return users

def get_users_age():
    connection = sqlite3.connect('users.db')
    sql = connection.cursor()
    users = sql.execute('SELECT age FROM users;').fetchall()
    return users

def add_music(tg_file_id, name, singer):
    connection = sqlite3.connect('users.db')
    sql = connection.cursor()
    user = sql.execute('SELECT * FROM music WHERE tg_file_id = ?;', (tg_file_id, )).fetchone()
    if not user:
        sql.execute('INSERT INTO music (tg_file_id, name, singer) VALUES (?, ?, ?);', (tg_file_id, name, singer))
        connection.commit()

def get_all_music():
    connection = sqlite3.connect('users.db')
    sql = connection.cursor()
    user = sql.execute('SELECT * FROM music;').fetchall()
    return user

def get_music_num(m):
    connection = sqlite3.connect('users.db')
    sql = connection.cursor()
    music = sql.execute('SELECT * FROM music WHERE music_id = ?;', (m, )).fetchall()
    return music

import csv

def get_music_name(m):
    connection = sqlite3.connect('users.db')
    sql = connection.cursor()
    music = sql.execute('SELECT * FROM music WHERE name = ?;', (m, )).fetchall()
    return music

def get_music_singer(m):
    connection = sqlite3.connect('users.db')
    sql = connection.cursor()
    music = sql.execute('SELECT * FROM music WHERE singer = ?;', (m, )).fetchall()
    return music

def cheсk_user(user_id):
    connection = sqlite3.connect('users.db')
    sql = connection.cursor()
    checker = sql.execute('SELECT tg_id FROM users WHERE tg_id = ?;', (user_id, ))
    if checker.fetchone():
        return True
    else:
        return False

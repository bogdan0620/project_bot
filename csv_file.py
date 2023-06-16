import csv
import database

user = database.get_all_music()
def get_csv_file():
    with open('Каталог.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=';', lineterminator='\r', quotechar='|')
        csv_writer.writerow(['Номер:', 'id в телеграме:', 'Название трека:', 'Исполнитель:'])
        csv_writer.writerows(user)
        return


user1 = database.get_users()
def get_csv_users():
    with open("users.csv", "w") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=';', lineterminator='\r', quotechar='|')
        csv_writer.writerow(['Номер:', 'id в телеграме:', 'Имя:', 'Возраст:'])
        csv_writer.writerows(user1)
        return

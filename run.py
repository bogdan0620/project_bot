import csv
import database

user = database.get_all_music()
def get_csv_file():
    with open('catalog.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=';', lineterminator='\r', quotechar='|')
        csv_writer.writerow(['Номер:', 'id в телеграме:', 'Название трека:', 'Исполнитель:'])
        csv_writer.writerows(user)
        return
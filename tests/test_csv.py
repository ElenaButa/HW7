import csv
from conftest import resources_path
import os.path



# TODO оформить в тест, добавить ассерты и использовать универсальный путь


def test_check():
    with open((os.path.join(resources_path,'eggs.csv')), 'w',  newline='') as csvfile: #добавлен параметр , ктр удаляет пустые строки
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['Anna', 'Pavel', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])
    with open('resources/eggs.csv', 'r') as csvfile:
        num_lines = sum(1 for line in csvfile)
        print(num_lines)
        assert num_lines == 2 #удалены пустые строки, итого запиано 2 строки, а не 4  - замечание 3
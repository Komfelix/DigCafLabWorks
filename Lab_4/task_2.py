# TODO импортировать необходимые молули
import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r', newline='') as csv_file:  # TODO считать содержимое csv файла
        csv_reader = csv.DictReader(csv_file, delimiter=',', lineterminator='\n')  # Чтение CSV-файла
        json_data = [row for row in csv_reader]  # Создание списка с помощью цикла из данных в CSV-файле
    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as json_file:  # TODO Сериализовать в файл с отступами равными 4
        json.dump(json_data, json_file, indent=4, ensure_ascii=False)  # Запись данных в файл в формате JSON


if __name__ == '__main__':
    task()  # Выполнение основной задачи

    # Чтение и вывод содержимого JSON файла для проверки
    with open(OUTPUT_FILENAME, 'r', encoding='utf-8') as output_file:
        for line in output_file:
            print(line, end="")

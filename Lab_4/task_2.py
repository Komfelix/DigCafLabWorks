import json


FILENAME = "input.json"


def task() -> float:  # TODO решите задачу
    file = FILENAME
    with open(file) as f:
        json_data = json.load(f)
    sum_of_products = sum(item['score'] * item['weight'] for item in json_data)
    return round(sum_of_products, 3)


print(task())

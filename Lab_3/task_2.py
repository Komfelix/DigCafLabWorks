# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, symbol=','):
    first_group = first_group.split(symbol)
    second_group = second_group.split(symbol)
    common_participants = []
    for i in first_group:
        for j in second_group:
            if i == j:
                common_participants.append(i)
    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
delimiter = "|"

# TODO Проверьте работу функции с разделителем отличным от запятой
common_participants_without_delimiter = (
    find_common_participants(participants_first_group, participants_second_group, delimiter))

print(common_participants_without_delimiter)

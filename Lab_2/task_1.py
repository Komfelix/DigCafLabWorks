money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
number_of_month = 0

while money_capital > 0:
    spend *= (increase+1)
    deficit = spend - salary
    money_capital -= deficit
    number_of_month += 1

print("Количество месяцев, которое можно протянуть без долгов:", number_of_month)
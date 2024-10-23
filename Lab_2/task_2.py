salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
number_of_month = 0
money_capital = 0

for number_of_month in range(10):
    if number_of_month != 0:
        spend *= (increase + 1)
    deficit = spend - salary
    money_capital += deficit
    number_of_month += 1

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))

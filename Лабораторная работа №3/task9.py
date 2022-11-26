salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

money_capital = 0  # количество денег, чтобы прожить 10 месяцев

for i in range(0, months):
    money_capital += spend
    spend *= 1 + increase
money_capital -= salary * months

print(round(money_capital))

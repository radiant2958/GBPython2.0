# ✔ Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии

name = ['Rick', 'Tom', 'Rose']
rate = [10000, 12000, 15000]
percent = ['10.25%', '11.0%', '9.32%']

result = {n: int(r * (1 + float(p.strip('%')) / 100)) for n, r, p in zip(name, rate, percent)}
print(result)

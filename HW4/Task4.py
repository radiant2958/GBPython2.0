# ✔ Создайте функцию генератор чисел Фибоначчи.

def fibonacci(n: int):
    n_1 = 0
    n_2 = 1
    for _ in range(n+1):
        yield n_1
        n_1,n_2 = n_2, n_1 + n_2

for i in fibonacci(10):
    print(i)
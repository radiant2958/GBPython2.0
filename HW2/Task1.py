# Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего
# результата, а не для решения.
number = int(input("ВВедите целое число: "))
original_number = number 

if number != 0:
    number_binary = ""
    while number > 0:
        number_binary = str(number % 2) + number_binary
        number //= 2

   
    number = original_number

    number_octal = ""
    while number > 0:
        number_octal = str(number % 8) + number_octal
        number //= 8
else:
    number_binary = "0"
    number_octal = "0"

# print(f"Двоичное представление: {number_binary} (Проверка: {bin(original_number)[2:]})")
# print(f"Восьмеричное представление: {number_octal} (Проверка: {oct(original_number)[2:]})")

# ✔ Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой.
from decimal import Decimal, getcontext
import math
getcontext().prec = 41
PI = Decimal(math.pi)
while True:
    d = Decimal(input("введите диаметр окружности не более 1000\n"))
    if d > 1000 or d < 0:
        print("введите корректный диаметр от 0 до 1000")
    else:
        break

r = Decimal(d / 2)
area = PI * r * r
circumference = PI * d

print (f'длина окружности = {circumference}\nплощадь окружности = {area}')

print(len(str(area)), len(str(circumference)))

# ✔ Напишите программу, которая решает
# квадратные уравнения даже если
# дискриминант отрицательный.
# ✔ Используйте комплексные числа
# для извлечения квадратного корня.

a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

D = complex(b**2 - 4*a*c)

x1 = (-b + D) / (2 * a)
x2 = (-b - D) / (2 * a)

print(f"Корни уравнения: x1 = {x1}, x2 = {x2}, Дискриминант = {D}")

# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег



CASHING_PERCENT = 0.015 
TAX = 0.1
PERCENT_ADD = 0.03
account = 0 
count = 0 
def add_cash(cash: float):
    global PERCENT_ADD, account, count
    if cash % 50 == 0:
        account+=cash
        count+=1
        if count % 3 == 0:
            account=account + account * PERCENT_ADD
            print(f"Начислен процент за пополнения счета, сумма на счете равна {account}")
        else:
            print(f"Сумма на счете {account} y.e.")
    else:
        print("Сумма пополнения счета должна быть кратна 50 у.е.")

def take_cash(cash: float):
    global PERCENT_ADD, account, count
    expenses = cash + percent_cash(cash)
    if account > expenses:
        if cash % 50 == 0:
            account-=expenses
            count+=1
            if count % 3 == 0:
                account = account + account * PERCENT_ADD
                print(f"Начислен процент за пополнения счета, сумма на счете равна {account}")
            else:
                print(f"Сумма на счете {account} y.e.")
        else:
            print("Сумма снятия должна быть кратна 50 у.е.")
    else:
        print(f"Недостаточно денег на счете, баланс {account} y.e.")


def percent_cash(cash: float):
    global CASHING_PERCENT
    cash_percent = cash*CASHING_PERCENT
    if cash_percent < 30:
        cash_percent = 30
    elif cash_percent > 600:
        cash_percent = 600

    return cash_percent

def exit_bank():
    print("Рады вас видетеь снова!\n")
    exit()

while True:
    action = input("1 - пополнить\n2 - снять деньги\n3 - баланс\n4 -выйти\n")
    if account > 5_000_000:
        account = account - account * TAX
        print(f"списан налог на богатство: ",  {account * TAX})

    if action == '1':
        cash = float(input("ВВедите сумму пополнения кратно 50 у.е. "))
        add_cash(cash)
    elif action == '2':
        cash = float(input("ВВедите сумму снятия кратно 50 у.е. "))
        take_cash(cash)
    elif action == '3':
        print("Баланс = ", account)
    else:
        exit_bank()   
# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.


original_number = int(input("Введите целое число: "))
number = abs(original_number) 

if number != 0:
    hex_map = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    number_hex = ""
    while number > 0:
        remainder = number % 16
        if remainder in hex_map:
            number_hex = hex_map[remainder] + number_hex
        else:
            number_hex = str(remainder) + number_hex
        number //= 16

    prefix = "-0x" if original_number < 0 else "0x"
    print(f'Шестнадцатеричное строковое представление числа: {prefix}{number_hex}, проверка: {hex(original_number)}')

else:
    print("Шестнадцатеричное строковое представление числа: 0, проверка: 0x0")

# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
from fractions import Fraction

fraction_1 = input("Введите дробь первую, разделяя числитель и знаменатель знаком /: ")
fraction_2 = input("Введите дробь вторую, разделяя числитель и знаменатель знаком /: ")

def sum_fractions(fraction_1, fraction_2):
    a, b = map(int, fraction_1.split("/"))
    c, d = map(int, fraction_2.split("/"))
    if b == d:
        numerator = a + c 
        print(f"Сумма дробей равна {numerator}/b")
    else: 
        numerator = a * d + c * b
        denominator = d*b
        print(f"Сумма дробей равна {numerator}/{denominator}")

def product_fractions(fraction_1, fraction_2):
    a, b = map(int, fraction_1.split("/"))
    c, d = map(int, fraction_2.split("/"))
    product_numerator = a * c
    product_denominator = b * d

    print(f"Произведение дробей равно {product_numerator}/{product_denominator}")


sum_fractions(fraction_1,fraction_2)
product_fractions(fraction_1,fraction_2)
fraction_1 = Fraction(fraction_1)
fraction_2 = Fraction(fraction_2)

sum_fr = fraction_1+fraction_2
print(sum_fr)
prod_fr = fraction_1*fraction_2
print(prod_fr)
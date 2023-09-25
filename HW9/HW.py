# Напишите следующие функции:
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
# Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса

import cmath
import csv
import random
from typing import Callable
import json




def apply_from_csv(file):
    def decorat(func: Callable ):
        def wrapper(*args, **kwargs):
            results = []
            with open(file, 'r', newline='') as f:
                reader = csv.reader(f)
                for row in reader:
                    a, b, c = map(float, row)
                    result = func(a, b, c)
                    print(f'Значения а = {a}, b = {b}, c = {c}, решением квадратного уравнения будет равно {result}')
                    results.append(result)

            return results
        
        return wrapper
    
    return decorat


def to_json(file):
    def decort(func:Callable):
        def wrapper(a,b,c):
            result = func(a,b,c)

            data = {
                'function_name': func.__name__,
                'a': a,
                'b': b,
                'c': c,
                'result': str(result)
            }

            with open(file, 'a') as f:
                json.dump(data,f, indent=5)
                f.write(",\n")



            return result
        return wrapper
    return decort

def quadratic_equation(a=1, b=1, c=1):
    d = cmath.sqrt(b**2- 4*a*c)
    if d.real < 0:
        print('Корней нет')
    elif d.real > 0:
        x_1 = (-b + d) / (2*a)
        x_2 = (-b - d) / (2*a)
        return x_1,x_2
    else:
        x_1=(-b+d**0.5)/2*a
        return x_1
    


def generate_csv(filename, num_rows=None):
    num_rows = num_rows or random.randint(100, 1000)
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for _ in range(num_rows):
            row = [random.randint(1, 100) for _ in range(3)]
            writer.writerow(row)

# generate_csv("generated_numbers.csv", 10)

@apply_from_csv("generated_numbers.csv")
@to_json("results.json")
def decorated_quadratic_equation(a, b, c):
    return quadratic_equation(a, b, c)


results = decorated_quadratic_equation()
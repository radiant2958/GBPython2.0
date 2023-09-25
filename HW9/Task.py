# Создайте функцию-замыкание, которая запрашивает два целых
# числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток. 
from functools import wraps
import json
import time
from typing import Callable
import random


def guess_game(game: Callable):
    def wrapper(*args, **kwargs):
        print('игра началась')
        result = game(*args, **kwargs)

        return result
    
    return wrapper


@guess_game
def game(attempts: int)->str:
    secret_number = random.randint(1,100)
    resul = None
    while attempts > 0:
        number = int(input('Введите число от 1 до 100, чтобы угадать число: '))
        if secret_number == number:
            resul = 'Ты угадал'
            break

        elif secret_number < number:
            print('Загаданное число меньше!')
            attempts-=1

        elif secret_number > number:
            print('Загаданное число больше!')  
            attempts-=1

    if resul == None:
        resul = 'Ты проиграл!'
    
    return resul

# print(game(5))

# Напишите декоратор, который сохраняет в json файл
# параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен
# расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ
# json словаря.
# Для декорирования напишите функцию, которая может
# принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой
# функции.

def to_json(func: Callable):
    
    def wrapper(*args, **kwargs):

        result = func(*args, **kwargs)

        data = {'function_name': func.__name__,
                'args': args,
                'kwargs': kwargs,
                'result': result}
        
        file_name = f"{func.__name__}.json"
        mode = 'a+' if json_open(file_name) else 'w'
        with open(file_name, mode) as f:
            if mode == 'a+':
                f.seek(f.tell() - 1, 0)  # Перемещаемся на одну позицию назад, чтобы убрать последнюю закрывающую скобку
                f.write(",\n")  # Добавляем запятую для следующего элемента
            else:
                f.write("[\n")  # Начинаем новый json массив

            json.dump(data, f, indent=4)
            f.write("\n]")

        return result
    
    return wrapper


def json_open(file_name):
    try:
        with open(file_name, 'r') as f:
            content = f.read().strip()
            return bool(content)
    except FileNotFoundError:
        return False
    
@to_json
def func_summ(a,b, c, d=0, f=0):
    return a+b+c+d+f



# func_summ(4,5,7, d=1, f=2)

# Создайте декоратор с параметром.

def count(a: int = 1):
    def deco(func: Callable):
        def wrapper(*args, **kwargs):
            time_for_count = []
            result = None
            for _ in range(a):
                start = time.perf_counter()
                result = func(*args, **kwargs)
                stop = time.perf_counter()
                time_for_count.append(stop - start)
            print(f'Результаты замеров {time_for_count}')
            
            return result
        
        return wrapper
    return deco


@count(2)
def factorial(n: int) ->int:
    f = 1 
    for i in range(2, n+1):
        f*=i
    return f

# print(f'{factorial(5)}')

# Объедините функции из прошлых задач.
# Функцию угадайку задекорируйте:
# ○ декораторами для сохранения параметров,
# ○ декоратором контроля значений и
# ○ декоратором для многократного запуска.
# Выберите верный порядок декораторов

@count(2)
@to_json
def sum_all(a,b,c=1):
    return a+b+c
    
# sum_all(2,4,c=7)

def log_to_json(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        
        data = {
            'function_name': func.__name__,
            'args': args,
            'kwargs': kwargs,
            'result': result
        }

        with open(f"{func.__name__}.json", 'a') as f:
            json.dump(data, f, indent=4)
            f.write(",\n")

        return result

    return wrapper

def run_multiple_times(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)

        return wrapper
    return decorator

@run_multiple_times
@log_to_json
def factorial(n: int) ->int:
    f = 1 
    for i in range(2, n+1):
        f*=i
    return f

print(f'{factorial(5)}')
  


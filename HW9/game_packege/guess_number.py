import random
from typing import Callable


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
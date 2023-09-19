# Создайте модуль с функцией внутри. 
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток. 
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток. 
# Функция выводит подсказки “больше” и “меньше”. 
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
from random import randint
import sys
def is_guess_number(lower: int, upper: int, attempts: int) -> bool:
    
    random_number = randint(lower,upper)
    flag = False
    while attempts > 0:
        number = int(input('Попробуй угадать число введи какое ты думаешь: '))
        if number!=random_number:
            if number>random_number:
                print('твое число больше чем закаданное')
                attempts-=1
            else:
                print('твое число меньше чем загаданное')
                attempts-=1
        else:
            flag = True
            break
    
    return flag

# if __name__ == "__main__":

#     resalt, number = is_guess_number(5,1,3)
#     print(resalt,number)

if __name__ == "__main__":
    args = sys.argv[1:]
    if 1 <= len(args) <= 3:
        parameters = [int(arg) for arg in args]
        
        if len(parameters) == 1:
            result = is_guess_number(1, parameters[0], 3)
        elif len(parameters) == 2:
            result = is_guess_number(parameters[0], parameters[1], 3)
        elif len(parameters) == 3:
            result = is_guess_number(*parameters)

        if result:
            print("Поздравляем! Вы угадали число!")
        else:
            print("К сожалению, попытки закончились.")
    else:
        print("Введите от 1 до 3 аргументов.")

            

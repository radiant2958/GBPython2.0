# ✔ Создайте функцию-генератор. Функция генерирует N простых чисел, начиная с числа 2.
# Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».

def prime_number(number: int):
    if number<2:
        return False
    n = int(number**0.5)+1
    for i in range(2,n):
        if number % i == 0:
            return False
        
    return True

def gen_prime(number: int):
    result = 2
    while result < number:
        if prime_number(result):
            yield result
            
        result+=1 
print(list(gen_prime(10)))
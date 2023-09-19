# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY 
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна. 
# Для простоты договоримся, что год может быть в диапазоне [1, 9999]. Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь. 
# Проверку года на високосность вынести в отдельную защищённую функцию.

def date_valid(date: str) -> bool:

    day, month, year = map(int, date.split('.'))

    if 1 > year > 9999:
        return False
    
    if 1 > month > 12:
        return False
    
    if month in [1,3,5,7,8,10,12]:
        days = 31
    elif month in [4,6,9,11]:
        days = 30
    elif month == 2:
        if _is_leap_year(year):
            days = 29
        else:
            days = 28
    else:
        return False

    if not (1 <= day <= days):
        return False

    return True


def _is_leap_year(year: int) -> bool:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    return False


if __name__ == "__main__":
        print(date_valid("10.11.2030"))
        print(date_valid("0.01.2099"))
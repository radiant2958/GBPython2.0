# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. 
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. 
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. 
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.



from random import randint


def beating_quens(quens: list):
    for i in range(len(quens)):
        for j in range(i+1, len(quens)):

            x1, y1 = quens[i]
            x2, y2 = quens[j]

            if x1 == x2 or y1 == y2:
                return False
            
            if abs(x1 - x2) == abs(y1 - y2):
                return False
    return True

queens_coordinates = [(1, 1), (2, 5), (3, 8), (4, 6), (5, 3), (6, 7), (7, 2), (8, 4)]
print(beating_quens(queens_coordinates)) 

# Напишите функцию в шахматный модуль. 
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

def placement_queen() -> list:
    queens = []
    for i in range(8):
        while True:
            x = i + 1
            y = randint(1, 8)
            if (x, y) not in queens:
                queens.append((x, y))
                break
    return queens


def find_best_placement_queen(count: int) -> list:
    best_placement = []
    while len(best_placement)<count:
        placement = placement_queen()
        if beating_quens(placement):
            best_placement.append(placement)
    return best_placement

placements = find_best_placement_queen(4)
for idx, placement in enumerate(placements, 1):
    print(f"Расстановка {idx}: {placement}")

print(beating_quens(placement_queen())) 
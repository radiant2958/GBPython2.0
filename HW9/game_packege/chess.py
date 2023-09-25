
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


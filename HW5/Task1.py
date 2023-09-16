# Напишите функцию для транспонирования матрицы
def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transpos = [[] for _ in range(cols)]  

    for i in range(cols):
        for j in range(rows):
            transpos[i].append(matrix[j][i])

    return transpos


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


transposed = transpose(matrix)


def print_matrix(matrix):
    for row in matrix:
        for value in row:
            print(value, end=' ')
        print() 


print_matrix(transposed)






# Вывод матрицы
def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i]) - 1):
            print((matrix[i][j]), end=" ")
        print(" | ", matrix[i][len(matrix)])
    print('\n')


# Нахождение опорного элемента
def max_elem(matrix, j):
    res = [max(i, key=abs) for i in zip(*matrix)][j]
    return res


# Вычисление дискриминанта в треугольной матрице
def determinant(matrix):
    det = 1
    for i in range(len(matrix) - 1):
        det *= matrix[i][i]
    return det


# Вычетание строк
def sub(matrix, row_one, row_two, coef):
    for i in range(len(matrix) + 1):
        matrix[row_one][i] -= matrix[row_two][i] * coef
    return matrix

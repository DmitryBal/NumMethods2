import numpy as np
from func import sub, printMatrix, determinant, max_elem

SLAY = np.array([[-2.0, -1.0, -9.0, -5.0, 93.0],
                 [-4.0, 4.0, -2.0, 6.0, 16.0],
                 [0.0, 5.0, 7.0, -4.0, -80.0],
                 [0.0, 9.0, 7.0, 7.0, -119.0]])
n = len(SLAY)


# Перестановка текущей строки со строкой, содержащей опорный элемент
def swap(matrix, k):
    M = np.delete(matrix, np.s_[0:k], axis=0)
    elem = max_elem(M, k)
    # если r(A) < r(n)
    if elem == 0:
        print("CЛАУ несовместна. Решений нет")
        quit(1)
    for i in range(k, len(matrix)):
        if matrix[i][k] == elem and i != k:
            for j in range(len(matrix[i])):
                matrix[i][j], matrix[k][j] = matrix[k][j], matrix[i][j]
    return matrix


# Приведение к треугольной матрице
def triangle(matrix):
    for j in range(n):
        matrix = swap(matrix, j)
        for i in range(j + 1, n):
            c = matrix[i][j] / matrix[j][j]
            matrix = sub(matrix, i, j, c)
            printMatrix(matrix)
    return matrix


def searchSolution(a):
    n = len(a)
    print('Обратный ход Гауса:\n')
    printMatrix(a)
    for i in range(n-1,-1,-1):
        a[i]/=a[i][i]
        if i < n-1:
            a[i][n] -= sum([a*b for a,b in zip(a[i+1:n, n],a[i][i+1:n])])
            a[i][i+1:n] = 0
        printMatrix(a)
    return a[:,n]

# Метод Гаусса
def gauss(matrix):
    matrix = triangle(matrix)
    det = determinant(matrix)
    if det != 0:
        '''
        b = matrix[:, n]
        a = np.delete(matrix, np.s_[n:n + 1], axis=1)
        x = np.linalg.solve(a, b)  
        '''
        x = searchSolution(matrix)
        return x
    else:
        print("СЛАУ вырождена, т.к. определитель равен нулю")
        return 0


if __name__ == '__main__':
    printMatrix(SLAY)
    X = gauss(SLAY)
    for i in range(n):
        print(f'x{i + 1} = ', X[i])

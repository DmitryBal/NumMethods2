import numpy as np

a = np.array([[-6.0, 3.0, 0.0, 0.0, 0.0],
              [6.0, -23.0, -9.0, 0.0, 0.0],
              [0.0, 2.0, -7.0, -1.0, 0.0],
              [0.0, 0.0, 5.0, 15.0, -9.0],
              [0.0, 0.0, 0.0, 5.0, -11.0]])

b = np.array([-33.0, -107.0, 18.0, -69.0, -31.0])

n = len(a)
x = [0] * n


# Вывод матрицы
def printMatrix(a, d):
    for i in range(len(a)):
        for j in range(len(a[i]) - 1):
            print("{:5d}".format(int(a[i][j])), end="")
        print(" | ", int(d[i]))
    print('\n')


# Метод прогонки
def run_method(a, d):
    P = [0] * n
    Q = [0] * n
    b_1 = a[0][0]
    P[0] = -a[0][1] / b_1
    Q[0] = d[0] / b_1
    for i in range(1, n):
        a_i = a[i][i - 1]
        den = a[i][i] + a_i * P[i - 1]
        Q[i] = (d[i] - a_i * Q[i - 1]) / den
        if i != n - 1:
            P[i] = -a[i][i + 1] / den
    x[n - 1] = Q[n - 1]
    for i in range(1, n):
        index = n - i - 1
        x[index] = P[index] * x[index + 1] + Q[index]
    return x, P, Q


if __name__ == '__main__':
    printMatrix(a, b)
    x, P, Q = run_method(a, b)
    print('P = ', P)
    print('Q = ', Q)
    for i in range(n):
        print(f'x{i + 1} = ', x[i])

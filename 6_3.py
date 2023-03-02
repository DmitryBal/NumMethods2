import numpy as np

eps = 0.01
A = np.array([[-2.0, -7.0, -8.0, -2.0],
              [2.0, -17.0, -6.0, -2.0],
              [-7.0, -6.0, -23.0, -3.0],
              [3.0, -2.0, -7.0, -13.0]])
B = np.array([-51.0, 85.0, 71.0, 91.0])
n = len(A)


# Вывод матрицы
def printMatrix(a, b):
    for i in range(n):
        for j in range(len(a[i])):
            print((a[i][j]), end=" ")
        print(" | ", b[i])
    print('\n')


# Поиск максимального элемента в массиве отношений элементов, где все элементы взяты по модулю
def max_div(arr_1, arr_2):
    return max([np.absolute(i - j) for i, j in zip(arr_1, arr_2)], key=abs)


'''
# Нахождение нормы матрицы (||A||_1)
def max_row(a):
    _a = []
    for i in range(n):
        _a.append(sum(np.absolute(a[i, :])))
    return max(_a)
'''


# Преобразование матриц для итерационных методов
def new_ab(a, b):
    for i in range(n):
        b[i] /= a[i][i]
        a[i:i+1, ] = [k / a[i][i] for k in a[i:i+1, ]]
    return -a[~np.eye(a.shape[0], dtype=bool)].reshape(a.shape[0], -1), b


# декоратор для итерационных методов
def iteration(flag, method):
    def iteration_decorator(func):
        def wrapper(a, b, epsilon):
            print(method)
            k = 0
            _eps = epsilon
            # _a = max_row(a)
            # epsilon *= np.absolute((1-_a) / _a)
            x_new = np.zeros(n)
            while _eps > epsilon or k == 0:
                if k == 0:
                    x = b
                else:
                    x = x_new
                    x_new = np.zeros(n)
                for i in range(n):
                    # Метод Зейделя
                    if flag == 1:
                        x_new[i] = sum(x_new[0:i] * a[i, 0:i]) + sum(x[i + 1:n] * a[i, i:n])
                    # Метод простых итераций
                    else:
                        x_new[i] = sum(a[i, :] * np.delete(x, i))
                    x_new[i] += b[i]
                _eps = max_div(x_new, x)
                print('N = ', k)
                print('eps = ', _eps)
                print('x* =', x_new)
                print('-----------------------------------------------')
                k += 1
            return x_new
        return wrapper
    return iteration_decorator


# Метод Зейделя
@iteration(1, '\nМетод Зейделя:')
def zeidel(a, b, epsilon):
    pass


# Метод простых итераций
@iteration(0, '\nМетод простых итераций:')
def iteration(a, b, epsilon):
    pass


if __name__ == '__main__':
    printMatrix(A, B)
    _A, _B = new_ab(A, B)
    X_z = zeidel(_A, _B, eps)
    X_i = iteration(_A, _B, eps)
    print('Метод Зейделя: x =', X_z)
    print('Метод простых итераций: x =', X_i)
    print('Решение с помощью встроенной функции numpy.linalg.solve(): x =', np.linalg.solve(A, B))

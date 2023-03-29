import numpy as np
from numpy import polyval as f
from func import derivative, f_conv, find_AB
epsilon = 0.001
c = np.array([1.0, 0.0, 0.0, 0.0, 0.0, -5.0, -2.0])
n = len(c)


# Метод половинного деления
def half_del(arr, a_b, eps, name):
    print('\n')
    print(name)
    k = 1
    _a = a_b[0]
    _b = a_b[1]
    while (_b - _a) > eps:
        c_k = 0.5 * (_a + _b)
        if f(arr, _a)*f(arr, c_k) < 0:
            _b = c_k
        if f(arr, _b)*f(arr, c_k) < 0:
            _a = c_k
        print('N =', k)
        print(f'[a_{k}, b_{k}] = [', _a, ',', _b, ']')
        print(f'c_{k} =', c_k)
        print('---------------------------------------\n')
        k += 1
    return c_k, k


# Метод простой итерации / Метод Ньютона
def iteration(arr, _arr, x, eps, name):
    print(name)
    k = 0
    x_new = 0
    while np.absolute(x_new - x) > eps or k == 0:
        if name == 'Метод простой итерации':
            x = x_new
            x_new = f_conv(x)
        elif name == 'Метод Ньютона':
            if k != 0:
                x = x_new
            x_new = x - f(arr, x) / f(_arr, x)
        else:
            print('Выберете один из реализованных методов')
            return 0
        print('N =', k)
        print('x =', x_new)
        print('---------------------------------------\n')
        k += 1
    return x_new, k


# Метод касательных
def tangential(arr, x0, x1, eps, name):
    print(name)
    k = 0
    f_x0 = f(arr, x0)
    f_x1 = f(arr, x1)
    while abs(f_x1 - f_x0) > eps:
        det = (f_x1 - f_x0) / (x1 - x0)
        x = x1 - f_x1 / det
        x0 = x1
        x1 = x
        f_x0 = f_x1
        f_x1 = f(arr, x1)
        print('N =', k)
        print('x =', x)
        print('---------------------------------------\n')
        k += 1
    return x, k


if __name__ == '__main__':
    _c = np.append(c[0:n-1], c[n-1])
    print(_c)
    ab = find_AB(c, n)
    N = [0]*4
    X = [0]*4
    print('f(x) =', c[0], '* x^6 +', c[-2], '* x +', c[-1])
    title = ['Метод половинного деления', 'Метод простой итерации', 'Метод Ньютона', 'Метод касательных']
    X[0], N[0] = half_del(c, ab, epsilon, title[0])
    X[1], N[1] = iteration(c, _c, 2.5, epsilon, title[1])
    _c = derivative(c, n)
    X[2], N[2] = iteration(c, _c, 2.5, epsilon, title[2])
    X[3], N[3] = tangential(c, 2, 2.5, epsilon, title[3])
    print('\nepsilon =', epsilon)
    for i in range(4):
        print(title[i], 'x =', X[i], '=> f(x) =', f(c, X[i]), '\t| Количество итераций =', N[i])


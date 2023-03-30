import numpy as np
from sympy import diff, symbols
from numpy import cos, sin, log10 as lg, log as ln, exp as e

epsilon = 0.001
f_x = 'x^6 - 5*x - 2'
t = 2.5
t_0 = 2.0


ab = np.array([1.0, 2.0])
# Приближение функции f(x) = x^6 - 5x - 2
def f_conv(x):
    return (5*x + 2)**(1/6)


def transform(equation):
    equation = equation.replace(" - ", " + -")
    equation = equation.replace('e^x', 'e(x)')
    equation = equation.replace("^", "**")
    return equation.split(' + ')


def f(value, func=transform(f_x)):
    str_value = str(value)
    parts_with_values = (part.replace("x", str_value) for part in func)
    return sum((eval(part) for part in parts_with_values))


def _f(value, func=f_x):
    func = func.replace('e^x', 'exp(x)')
    x = symbols('x')
    return diff(func).evalf(subs={x: value})


# Метод половинного деления
def half_del(a_b, eps, name):
    print('\n')
    print(name)
    k = 1
    _a = a_b[0]
    _b = a_b[1]
    print('[a_0, b_0] = [', _a, _b, ']\n')
    c_k = 0.5 * (_a + _b)
    while (_b - _a) > eps:
        if f(_a)*f(c_k) < 0:
            _b = c_k
        if f(_b)*f(c_k) < 0:
            _a = c_k
        c_k = 0.5 * (_a + _b)
        print('N =', k)
        print(f'[a_{k}, b_{k}] = [', _a, ',', _b, ']')
        print(f'c_{k} =', c_k)
        print('---------------------------------------\n')
        k += 1
    return c_k, k


# Метод простой итерации / Метод Ньютона
def iteration(x, eps, name):
    print(name)
    k = 1
    x_new = 0
    while np.absolute(x_new - x) > eps or k == 0:
        if name == 'Метод простой итерации':
            x = x_new
            x_new = f_conv(x)
        elif name == 'Метод Ньютона':
            if k != 1:
                x = x_new
            x_new = x - f(x) / _f(x)
        else:
            print('error')
            return 0
        print('N =', k)
        print('x =', x_new)
        print('---------------------------------------\n')
        k += 1
    return x_new, k


# Метод касательных
def tangential(x0, x1, eps, name):
    print(name)
    k = 1
    f_x0 = f(x0)
    f_x1 = f(x1)
    while abs(f_x1 - f_x0) > eps:
        det = (f_x1 - f_x0) / (x1 - x0)
        x = x1 - f_x1 / det
        x0 = x1
        x1 = x
        f_x0 = f_x1
        f_x1 = f(x1)
        print('N =', k)
        print('x =', x)
        print('---------------------------------------\n')
        k += 1
    return x, k


if __name__ == '__main__':
    N = [0]*4
    X = [0]*4
    print('f(x) =', f_x)
    title = ['Метод половинного деления', 'Метод простой итерации', 'Метод Ньютона', 'Метод касательных']
    X[0], N[0] = half_del(ab, epsilon, title[0])
    X[1], N[1] = iteration(t, epsilon, title[1])
    X[2], N[2] = iteration(t, epsilon, title[2])
    X[3], N[3] = tangential(t_0, t, epsilon, title[3])
    print('\nepsilon =', epsilon)
    for i in range(4):
        print(title[i], 'x =', X[i], '=> f(x) =', f(X[i]), '\t| Количество итераций =', N[i]-1)


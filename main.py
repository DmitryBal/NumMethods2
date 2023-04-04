import numpy as np
from numpy import log10 as lg
from sympy import diff, symbols


def f_conv(x, y):
    return np.array([np.sqrt(2.0*lg(y) + 1.0), x/3.0 + 1.0/x])


def max_div(x1, y1, x2, y2):
    return max(abs(x2-x1), abs(y2-y1))


def transform(equation):
    equation = equation.replace(" - ", " + -")
    equation = equation.replace('e^x', 'e(x)')
    equation = equation.replace("^", "**")
    return equation.split(' + ')


def f(x_value, y_value, func):
    func = transform(func)
    res = []
    str_x = str(x_value)
    str_y = str(y_value)
    for part in func:
        parts_with_values = part.replace('x', str_x)
        res.append(parts_with_values.replace('y', str_y))
    return sum((eval(part) for part in res))


def _f(_x, _y, func):
    func = func.replace('lg', '(1/ln(10))*ln')
    x = symbols('x')
    y = symbols('y')
    return np.array([diff(func, x).subs([(x, _x), (y, _y)]), diff(func, y).subs([(x, _x), (y, _y)])])


def newton(x, y, f_1, f_2, eps):
    div = eps
    k = 1
    while div >= eps:
        print('N =', k)
        W = np.eye(2)
        W[0] = _f(x, y, f_1)
        W[1] = _f(x, y, f_2)
        print('W =', W)
        B = -np.array([f(x, y, f_1), f(x, y, f_2)])
        print('B =', B)
        _div = np.linalg.solve(W, B)
        div = max(abs(_div))
        x_new, y_new = np.array([x, y]) + _div
        print('x =', x_new, 'y =', y_new)
        print('epsilon =', div)
        print('-------------------------------')
        x, y = x_new, y_new
        k+=1
    return x, y, k-1


def simple(x, y, eps):
    _div = eps
    k = 1
    while _div >= eps:
        x_new, y_new = f_conv(x, y)
        _div = max_div(x, y, x_new, y_new)
        print('N =', k)
        print('x =', x_new, 'y =', y_new)
        print('epsilon =', _div)
        print('-------------------------------')
        x, y = x_new, y_new
        k += 1
    return x, y, k-1


if __name__ == '__main__':
    x0 = 1.1
    y0 = 1.1
    epsilon = 0.001
    print('x0, y0 = (', x0, y0, ')')
    f2 = 'x^2 - 3*x*y + 3'
    f1 = 'x^2 - 2*lg(y) - 1'
    print('f1(x,y) =', f1)
    print('f2(x,y) =', f2)
    print('\nМетод простых итераций:')
    X_s, Y_s, N_s = simple(x0, y0, epsilon)
    print('Метод Ньютона:')
    X_n, Y_n, N_n = newton(x0, y0, f1, f2, epsilon)
    print('\nepsilon =', epsilon)
    print('Метод простых итераций:', 'x =', X_s, '=> f1(x, y) =', f(X_s, Y_s, f1), '| f2(x, y) =', f(X_s, Y_s, f2), '\t| Количество итераций =', N_s)
    print('Метод Ньютона:\t\t', '\tx =', X_n, '=> f1(x, y) =', f(X_n, Y_n, f1), '| f2(x, y) =', f(X_n, Y_n, f2), '\t| Количество итераций =', N_n)
import numpy as np


# Нахождение коэффициентов производной от заданного многочлена
def derivative(arr, l):
    arr = np.delete(arr, l-1)
    for i in range(l-1):
        arr[i] *= (l-1-i)
    return arr


# Приближение функции f(x) = x^6 - 5x - 2
def f_conv(x):
    return (5*x + 2)**(1/6)


# нахождение интервала, в котором распологается один корень нелинейного многочлена
def find_AB(arr, l):
    arr = np.absolute(arr)
    a = 1 / (1 + max(arr[0:l-1]) / arr[-1])
    b = 1 + max(arr[1:l]) / arr[0]
    return np.array([a, b])

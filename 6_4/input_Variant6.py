ab = np.array([0.0, 1.0])
f_x = 'x*lg(x+1) + x^2 - 1'
# Приближение функции f(x) = x*lg(x+1) + x^2 - 1
def f_conv(x):
    return np.sqrt(1.0 - x*lg(x+1.0))

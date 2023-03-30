ab = np.array([1.0, 2.0])
f_x = '4^x - 5*x - 2'
# Приближение функции f(x) = 4^x - 5*x - 2
def f_conv(x):
    return 0.5*log2((5.0*x + 2.0))

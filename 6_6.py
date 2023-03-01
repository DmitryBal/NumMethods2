import numpy as np

eps = 0.01
A = np.array([[-8.0, 5.0, -7.0],
              [5.0, 1.0, 4.0],
              [-7.0, 4.0, 4.0]])
n = len(A)


# Нахождения максимамального по модулю элемента a_ij, где j > i
def max_elem(matrix):
    a_ij = [0] * n
    for i in range(n):
        for j in range(n):
            if j > i and np.abs(a_ij[0]) < np.abs(matrix[i][j]):
                a_ij = [matrix[i][j], i, j]
    return a_ij


# Функция нахождения sin и cos угла поворота
def phi(matrix, _max, _i, _j):
    _phi = 0.5 * np.arctan(2 * _max / (matrix[_i][_i] - matrix[_j][_j]))
    return [np.sin(_phi), np.cos(_phi)]


# Метод вращения Якоби
def method_turn(matrix):
    _max = max_elem(matrix)[0]
    x = np.eye(n)
    k = 0
    while np.abs(_max) > eps:
        _max, _i, _j = max_elem(matrix)
        print('k = ', k)
        print('\nmax|a_ij| = ', _max)
        sin, cos = phi(matrix, _max, _i, _j)
        print(f'sin(phi_{k}) = ', sin, f'cos(phi_{k}) = ', cos)
        H = np.eye(n)
        H[_i][_i] = H[_j][_j] = cos
        H[_i][_j] = -sin
        H[_j][_i] = sin
        print('\nH =', H, '\n')
        H_T = H.transpose()
        print('H^T =', H_T, '\n')
        x = np.matmul(x, H)
        matrix = np.matmul(np.matmul(H_T, matrix), H)
        print(f'A({k + 1}) = H({k})^T * A({k}) * H({k}) = ', matrix)
        print('-----------------------------------------------')
        k += 1
    for j in range(n):
        x[:, j] /= x[j][j]
    return matrix.diagonal(), x


if __name__ == '__main__':
    print('A = ', A)
    M, X = method_turn(A)
    print('Собственные значения:')
    for i in range(n):
        print(f'lamda_{i + 1} = ', M[i])
    print('\nСобственные вектора:')
    for j in range(n):
        print(f'X{j + 1} = ', X[:, j])

# 6_3 - Итерационные методы решения СЛАУ
[Теория](https://mathhelpplanet.com/static.php?p=chislennyye-metody-resheniya-slau)
## 6_3.py:
### def printMatrix(a, b):
  - Принимает на вход параметр: *a* - матрица вида **n** x **n**, *b* - столбец решений матрицы *а*
  - Выводит матрицу в более читаемом виде
### def max_div(arr_1, arr_2):
  - Принимает на вход два массива одинаковой длинны
  - Возвращает: максимальный по модулю элемент в массиве отношений массивов *arr_1* и *arr_2*
  - **В функции используется**:
      - Встроенная функция [zip()](https://pythonru.com/uroki/funkcija-zip-dlja-nachinajushhih)
### def new_ab(a, b):
   - Принимает на вход параметры: *a* - матрица вида **n** x **n**, *b* - столбец решений матрицы *а*
   - Каждую *i*-ую строку матрицы *a* делим на элемент -a[i][i], затем удаляем главную диагональ
   - Возвращает: матрицу *a* вида **n-1** x **n-1**, и столбец *b*, разделенный на главную диагональ матрицы *a*
   - **В функции используется**:
       - Встроенная функция [numpy.diagonal(a, offset=0, axis1=0, axis2=1)](https://numpy.org/doc/stable/reference/generated/numpy.diagonal.html)
       - masking: [a[~np.eye(a.shape[0], dtype=bool)].reshape(a.shape[0], -1)](https://stackoverflow.com/questions/46736258/deleting-diagonal-elements-of-a-numpy-array)
### def iteration(flag, a, b, epsilon):
   - Принимает на вход параметры: *a* - матрица вида **n** x **n**, *b* - столбец решений матрицы *а*, *epsilon* - погрешность и *flag* - флаг
     -  если *flag* = 1, то вычисляется с помощью метода Зейделя; 
     -  если *flag* = 0, то вычисляется с помощью метода простых итераций
   - Возвращает: *x* - решение системы *ax = b*
   - **В функции используется**:
       - Встроенная функция [numpy.zerros()](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html)
       - Встроенная функция [numpy.delete(arr, obj, axis=None)](https://numpy.org/doc/stable/reference/generated/numpy.delete.html)
       - Функция [max_div(arr_1, arr_2)](https://github.com/DmitryBal/NumMethods2/tree/main/6_3#def-max_divarr_1-arr_2)
  

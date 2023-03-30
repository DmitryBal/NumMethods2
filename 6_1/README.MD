# 6_1 - Метод Гаусса
## func.py:
### def printMatrix(matrix):
  - Принимает на вход параметр: *matrix* - матрица вида **n+1** x **n** 
  - Выводит матрицу в более читаемом виде
### def max_elem(matrix, j):
  - Принимает на вход параметры: *matrix* - матрица вида **n+1** x **n** и *j* - номер столбца
  - Возвращает: максимальный по модулю элемент в столбце
  - В функции используется функция **_zip_()** для перебора итерируемых объектов,  c оператором: * , который используется для распоковки кортежей. Более подробно: https://pythonru.com/uroki/funkcija-zip-dlja-nachinajushhih
### def determinant(matrix):
  - Принимает на вход параметр: *matrix* - матрица вида **n+1** x **n**
  - Возвращает: произведение элементов на главной диагонали
### def sub(matrix, row_one, row_two, coef):
  - Принимает на вход параметры: *matrix* - матрица вида **n+1** x **n**, *row_one* - строка из которой вычитают , *row_two* - строка которую вычитают, *coef* - коэффициент
  - Возвращает: матрицу с преобразованной строкой *row_one*
## main.py:
### def swap(matrix, k):
 - Принимает на вход параметры: *matrix* матрица и *k* - номер последней строки, которая была преобразован
 - Возвращает: матрицу, в которой k-строка заменена на строку, где элемент matrix[k][k] является опорным.
 - **В функции используется**:
     - Функция [max_elem(matrix, j)](https://github.com/DmitryBal/NumMethods2/tree/main/6_1#def-max_elemmatrix-j)
     - Встроенная функция [numpy.delete(arr, obj, axis=None)](https://note.nkmk.me/en/python-numpy-delete/)
 ### def triangle(matrix):
  - Принимает на вход параметр: *matrix* - матрица вида **n+1** x **n**
  - Возвращает: матрицу приведенную к верхнему треугольному виду
  - **В функции используется**:
      - Функция [sub(matrix, row_one, row_two, coef)](https://github.com/DmitryBal/NumMethods2/tree/main/6_1#def-submatrix-row_one-row_two-coef)
      - Функция [printMatrix(matrix)](https://github.com/DmitryBal/NumMethods2/tree/main/6_1#def-printmatrixmatrix)
      - Функция [swap(matrix, k)](https://github.com/DmitryBal/NumMethods2/tree/main/6_1#def-submatrix-row_one-row_two-coef)

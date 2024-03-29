# 6_1 - Метод Гаусса
[Теория](https://mathhelpplanet.com/static.php?p=chislennyye-metody-resheniya-slau)
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
 - Принимает на вход параметры: *matrix* - матрица вида **n+1** x **n** и *k* - номер последней строки, которая была преобразован
 - Возвращает: матрицу, в которой k-строка заменена на строку, где элемент matrix[k][k] является опорным.
 - **В функции используется**:
     - Функция [max_elem(matrix, j)](https://github.com/DmitryBal/NumMethods2/tree/main/6_1#def-max_elemmatrix-j)
     - Встроенная функция [numpy.delete(arr, obj, axis)](https://note.nkmk.me/en/python-numpy-delete/)
     - Если ранг матрицы A < ранга матрицы n, то Слау несовместна => используется встроенная команда выхода: [quit()](https://pythonguides.com/python-exit-command/)
 ### def triangle(matrix):
  - Принимает на вход параметр: *matrix* - матрица вида **n+1** x **n**
  - Возвращает: матрицу приведенную к верхнему треугольному виду
  - **В функции используется**:
      - Функция [sub(matrix, row_one, row_two, coef)](https://github.com/DmitryBal/NumMethods2/tree/main/6_1#def-submatrix-row_one-row_two-coef)
      - Функция [printMatrix(matrix)](https://github.com/DmitryBal/NumMethods2/tree/main/6_1#def-printmatrixmatrix)
      - Функция [swap(matrix, k)](https://github.com/DmitryBal/NumMethods2/tree/main/6_1#def-submatrix-row_one-row_two-coef)
### def gauss(matrix):
 - Принимает на вход параметр: *matrix* - матрица вида **n+1** x **n** 
 - Возвращает: массив корней Слау 
 - **В функции используется**:
     - Функция [def determinant(matrix)](https://github.com/DmitryBal/NumMethods2/tree/main/6_1#def-determinantmatrix)
     - Функция [def triangle(matrix)](https://github.com/DmitryBal/NumMethods2/tree/main/6_1#def-trianglematrix)
     - Встроенная функция [numpy.delete(arr, obj, axis)](https://note.nkmk.me/en/python-numpy-delete/)
     - Встроенная функция [numpy.linalg.solve(a, b)](https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html)
     

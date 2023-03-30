# 6_6 - Метод вращения Якоби
[Теория](https://mathhelpplanet.com/static.php?p=chislennyye-metody-resheniya-slau)
## def max_elem(matrix):
   - Принимает на вход параметр: *matrix* - матрица вида **n** x **n** 
   - Возвращает: максимальный по модулю элемент матрицы, в выделенной части матрицы (*j > i*) и его индексы:

![#f5f5f5](https://placehold.co/15x15/f5f5f5/f5f5f5.png) ![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png) ![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png) 

![#f5f5f5](https://placehold.co/15x15/f5f5f5/f5f5f5.png) ![#f5f5f5](https://placehold.co/15x15/f5f5f5/f5f5f5.png) ![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png) 

![#f5f5f5](https://placehold.co/15x15/f5f5f5/f5f5f5.png) ![#f5f5f5](https://placehold.co/15x15/f5f5f5/f5f5f5.png) ![#f5f5f5](https://placehold.co/15x15/f5f5f5/f5f5f5.png) 

## def phi(matrix, _max, _i, _j):
   - Принимает на вход параметры:  *matrix* - матрица вида **n** x **n** и *_max*, *i*, *j* - результат работы функции [def max_elem(matrix):](https://github.com/DmitryBal/NumMethods2/tree/main/6_6#def-max_elemmatrix)
   - Возвращает: sin, cos угла поворота
## def method_turn(matrix):
   - Принимает на вход параметр: *matrix* - матрица вида **n** x **n** 
   - Возвращает: собственные значения и вектора матрицы **a



# В квадратной матрице все элементы, не лежащие на главной диагонали увеличить в
# 2 раза.
import numpy as np
arr = np.array([[1, 4, 5],
                [8, 2, 5],
                [3, 9, 16]])
print(f'изначальная матрица: \n {arr}')
for i in range(len(arr)):
    for y in range(len(arr[i])):
        if i != y:
            arr[i][y] *= 2

print(f'увеличенная: \n {arr}')
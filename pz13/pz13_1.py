#В матрице найти максимальный положительный элемент, кратный 4.
import numpy as np
arr = np.array([[1, 4, 5],
                [8, 2, 5],
                [3, 9, 16]])
num = []
for rov in arr:
    for q in rov:
        if q % 4 == 0:
            num.append(q)

print('максмальный положительный эллемен кратный 4:',max(num))
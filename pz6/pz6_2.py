# Дан список A размера N. Сформировать новый список B того же размера, элементы
# которого определяются следующим образом:
#   BK = 2*AK, если AK < 5,
#   AK/2 в противном случае.
def spisok(arr):
    arr2 = []
    for i in arr:
        if i<5:
            b = i*2
        else:
            b = i/2
        arr2.append(b)
    return arr2

arr = [2,3,5,1,7]
arr2 = spisok(arr)
print(f'Изначальный список: {arr}')
print(f'Новый список: {arr2}')
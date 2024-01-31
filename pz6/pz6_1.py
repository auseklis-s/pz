# Дан целочисленный список размера N, не содержащий одинаковых чисел.
# Проверить, образуют ли его элементы арифметическую прогрессию. Если образуют,
# то вывести разность прогрессии, если нет — вывести 0.
def arithmetic(arr):
    n = len(arr)
    
    if n < 2:
        return 0 
    
    difference = arr[1] - arr[0]
    
    for i in range(2, n):
        if arr[i] - arr[i-1] != difference:
            return 0 
    
    return difference

my_list = [2, 4, 6, 8, 10] 
result = arithmetic(my_list)

if result != 0:
    print(f"Элементы образуют арифметическую прогрессию с разностью {result}.")
else:
    print("Элементы не образуют арифметическую прогрессию.")

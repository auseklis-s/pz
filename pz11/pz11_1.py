a = [2, 3, 6, 1, 9, 12, 111, 54, 21, 146, 21, 7, 325]
b = []
c = []
for i in a:
    if i % 2 == 0:
        b.append(i)
    else:
        c.append(i)

with open('file1.txt', 'w') as file:
    file.write('четные элементы:\n')
    file.write(str(b) + '\n')
    file.write('произведение четных елментов:\n')
    b1 = 1
    for y in b:
        b1 *= y
    file.write(str(b1)+ '\n')
    file.write('минимальный элемент:\n')
    file.write(str(min(b))) 

with open('file2.txt', 'w') as file:
    file.write('нечетные элементы:\n')
    file.write(str(c) + '\n')
    file.write('количество нечетные элементы:\n')
    file.write(str(len(c)) + '\n')
    file.write('сумма нечетные элементы:\n')
    file.write(str(sum(c)) + '\n')
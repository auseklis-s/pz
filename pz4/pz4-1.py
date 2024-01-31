#Даны целые положительные числа N и K. Найти сумму 1K + 2К + ... + NK
K=int(input("Введите число K:"))
N=int(input("Введиите число N:"))

if type(N) and type(K) == int:
    result=sum(i**K for i in range(1, N+1))
    print(result)
else:
   print('Вы ввели не числа!!!')
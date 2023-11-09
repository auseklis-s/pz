number = int(input("Введите трехзначное число:"))
if 100<=number<=999:
    third = number % 10
    number //= 10
    second = number % 10
    number //= 10
    first = number % 10
    if (first<second<third):
         print("Цифры образуют возрастающую последовательность:")
    elif (first>second>third):
         print("Цифры образуют убывающую последовательность:")
    else:
         print('Цифры не образуют последовательность')
else:
    print('Данное число не является трехзначным')

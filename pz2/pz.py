#Вариант 23. Дано целое число, большее 999. Используя одну операцию деления нацело и одну операцию взятия остатка от деления,
#найти цифру соответствующую разряду тысяч, в запеиси этого числа.
number = int(input('Введите число больше 999:'))
number2 = number//1000%10
print('Цифра соответствующая разряду тысяч:', number2)
# Описать функцию TrianglePS(a, P, S), вычисляющую по стороне a равностороннего
# треугольника его периметр P = 3*a и площадь S = a2 √3/4 (a — входной, P и S —
# выходные параметры; все параметры являются вещественными). С помощью этой
# функции найти периметры и площади трех равносторонних треугольников с данными сторонами.
import math
def TriangleP(a):
    return 3*a, 2*a*math.sqrt(3/4)

print('Привет, эта функция вычисляющую по стороне a равностороннего треугольника его периметр и площадь')
a = int(input("Введите сторону треугольника:"))
Per = TriangleP(a)
print(f"Периметр равена {Per[0]}\nПлощадь равна {Per[1]}")
import math
def TriangleP(a):
    return 3*a
def TriangleS(a):
    return 2*a*math.sqrt(3/4)

print('Привет, эта функция вычисляющую по стороне a равностороннего треугольника его периметр и площадь')
a,b,c = int(input("Введите сторону а:")), int(input("Введите сторону b:")), int(input("Введите сторону c:"))
if a==b==c:
    Per = TriangleP(a)
    Sqare = TriangleS(a)
    print(f"Периметр равна {Per}\nПлощадь равна {Sqare}")
else:
    print("Вы ввели не равносторонний треугольник!!!")
# Дано множество A из N точек (точки заданы своими координатами x, у). Среди всех
# точек этого множества, лежащих в первой или третьей четверти, найти точку,
# наиболее близкую к началу координат. Если таких точек нет, то вывести точку с
# нулевыми координатами.
import math

def closest_point(x_list, y_list):
    closest_distance = float('inf')
    closest_point = (0, 0)
    
    for i in range(len(x_list)):
        if x_list[i] >= 0 and y_list[i] >= 0:
            distance = math.sqrt(x_list[i] ** 2 + y_list[i] ** 2)
            if distance < closest_distance:
                closest_distance = distance
                closest_point = (x_list[i], y_list[i])
    
    if closest_point == (0, 0):
        return "Нет точек в первой или третьей четверти"
    
    return closest_point

x = [0.23, 0, 0.3, 1, 2, 8]
y = [0.243, 1, 0.1, 3, 1, 6]
print(f"Точки которые ближе все голежат к началу координат: {closest_point(x, y)}")

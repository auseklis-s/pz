# Дан словарь с произвольным количеством элементов. Выяснить
# имеется ли в нем элемент с ключом «фрукт = яблоко» и если он отсутствует, то
# добавить его в словарь. Вывести на экран первоначальный словарь и измененный.

produkt = {'машина': 'мерседес',
           'овощь': 'огурец',
           'инструмент': 'молоток',
           "фрукт": "яблоко"
           }

print(f'изначальный список {produkt}')

alfa = produkt['фрукт']

if 'фрукт' in produkt and alfa == 'яблоко':
    print("имеется элемент со значением 'фрукт': 'яблоко'")

else:
    produkt['фрукт'] = 'яблоко'
    print(f'измененный список {produkt}')

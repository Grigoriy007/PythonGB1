# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и
# выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
#
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Введите координаты точки X: '))
y = int(input('Введите координаты точки Y: '))

if x > 0 and y > 0:
    print(f'номер четверти плоскости, в которой находится точка c координатами X = {x} Y= {y} -> I')
elif x < 0 and y > 0:
    print(f'номер четверти плоскости, в которой находится точка c координатами X = {x} Y= {y} -> II')
elif x < 0 and y < 0:
    print(f'номер четверти плоскости, в которой находится точка c координатами X = {x} Y= {y} -> II')
elif x > 0 and y < 0:
    print(f'номер четверти плоскости, в которой находится точка c координатами X = {x} Y= {y} -> IV')
elif x == 0 and y == 0:
    print('Такого быть не может:)')

# Задание 2: Напишите задачу на вход принимает числа и находит максимальное из них
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

import random

my_list = []

for i in range(5):
    # my_list.append(int(input('Insert number: ')))
    my_list.append(random.randint(0, 100))  # Это рандомный набор чисел

print(my_list)

maxx = my_list[0]

for item in my_list:
    if item > maxx:
        maxx = item

# print(f'Maximal number: {maxx}')
print('Maximal number: ', maxx)

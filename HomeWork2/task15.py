# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE,
# максимум использование библиотеки Random для и получения случайного int

from random import randint

n = int(input('Введите число n (где n - количество чисел в списке): '))

my_list = []

for i in range(n):
    my_list.append(randint(1, 100))

print(my_list)

for a in range(n+10):
    index1 = randint(0, n - 1)
    index2 = randint(0, n - 1)
    value = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = value

print(f'Перемешанный список: {my_list}')



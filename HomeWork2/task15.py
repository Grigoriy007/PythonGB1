# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE,
# максимум использование библиотеки Random для и получения случайного int

from random import randint

n = int(input('Введите число n (где n - количество чисел в списке): '))

my_list = [randint(1, 100) for i in range(n)]  # list complication
print(f'Первоначальный список: {my_list}')

my_list = list(enumerate(my_list))  # enumerate

my_dict = {my_list[i][0]: my_list[i][1] for i in range(0, len(my_list))}

for i in my_dict:
    for j in my_dict:
        r_key1 = randint(0, n - 1)
        r_key2 = randint(0, n - 1)
        temp = my_dict[r_key1]
        my_dict[r_key1] = my_dict[r_key2]
        my_dict[r_key2] = temp

new_list = [my_dict[i] for i in range(n)]  # list complication

print(f'Перемешанный список: {new_list}')

# for a in range(n+10):
#     index1 = randint(0, n - 1)
#     index2 = randint(0, n - 1)
#     value = my_list[index1]
#     my_list[index1] = my_list[index2]
#     my_list[index2] = value
#
# print(f'Перемешанный список: {my_list}')

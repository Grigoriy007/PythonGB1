# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform

def fullList(inc_list, num):
    for i in range(num):
        inc_list.append(round(uniform(1, 10), 2))

def chageList(inc_list):
    for i in range(len(inc_list)):
        inc_list[i] = inc_list[i].split('.')
        inc_list[i][0] = '0.'
        inc_list[i] = inc_list[i][0] + inc_list[i][1]
    return inc_list

def findMaxMin(inc_list):
    max = inc_list[0]
    for val1 in inc_list:
        if inc_list[0] != 0:
            min = inc_list[0]
        break

    for val2 in inc_list:
        if val2 > max:
            max = val2
        if val2 < min and val2 != 0:
            min = val2
    sub = max - min
    return print(f'Максимальный элемент: {max}\nМинимальный элемент: {min}\nРазница максимального и минимального: {sub}')



number = int(input('Введите длину списка: '))
my_list = []
fullList(my_list, number)
print(f'Изначальный список: {my_list}')
my_list = list(map(str, my_list))
chageList(my_list)
my_list = list(map(float, my_list))
print(f'Список интовый: {my_list}')
findMaxMin(my_list)

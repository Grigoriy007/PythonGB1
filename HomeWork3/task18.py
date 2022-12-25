# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

def findOdd(list1, list2, size):
    for i in range(size):
        num = randint(1, 100)
        list1.append(num)
        if i % 2 == 1:
            list2.append(list1[i])
    return list1, list2

def findSumm(list2):
    sum = 0
    for i in list2:
        sum += i
    return sum


a = int(input('Введите длину спика чисел: '))
my_list1 = []
my_list2 = []
findOdd(my_list1, my_list2, a)
print(f' Изначальный список: {my_list1}')
print(f' Список с нечетными элементами (эти элементы на нечетных позициях): {my_list2}')
print(f' Сумма нечетных значений: {findSumm(my_list2)}')

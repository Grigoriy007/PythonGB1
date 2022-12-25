# 2.	Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

from random import randint


def fullList(list, num):
    for i in range(num):
        list.append(randint(1, 10))


def findAnswer(list1, list2):
    if len(list1) % 2 == 0:
        ind = 0
        while ind < len(list1) // 2:
            mul = list1[ind] * list1[-ind - 1]
            list2.append(mul)
            ind += 1
    else:
        ind = 0
        while ind < len(list1) / 2:
            mul = list1[ind] * list1[-ind - 1]
            multi_list.append(mul)
            ind += 1


number = int(input('Введите длину списка: '))
my_list = []
multi_list = []
fullList(my_list, number)
findAnswer(my_list, multi_list)
print(f'{my_list} => {multi_list}')

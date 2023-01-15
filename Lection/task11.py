# name = {}  так объявляется словарь
#  print(name_library.get(key)) вывод ключа словаря
#  name[key] = {} создание значения ключа
#
# my_dict = {}  # словарь
#
# my_dict[23423] = {'name': 'Валера', 'age': 34, 'work': 'GB'}
# my_dict[1] = 'Один'
# my_dict ['43'] = True
#
# print(my_dict)
# print(my_dict.get(23))  # чтобы не сломалась программа из-за неправильной введенной цифры
#
#  в [] скобках пишется ключ
#
# print(my_dict.get('43'))
#
#  for item in my_dict.keys(): видно только ключи
#  for item in my_dict.values(): видно только значения
#
#
#  for item in my_dict.items():     # видно и ключи и значения
#     print(item)
#
#  for key, value in my_dict.items():     # проверка ключа и значения, и если есть например True, вывести ключ
#     if value == True:
#      print(key)
#
# print(my_dict)
# my_dict.pop(1)     # удаление элемента из словаря
# print(my_dict)

# Для натурального n создать словарь ключ-значение,
# состоящий из элементов последовательности 3n + 1.
# Пример:
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


num = int(input('Введите целое число: '))

my_dict = {}

for n in range(1, num+1):
    my_dict[n] = 3*n + 1
print(f'При N = {num}: ', end=' ')
print(my_dict)







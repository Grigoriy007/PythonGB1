#  Напишите программу, которая определит позицию второго вхождения
# строки в списке либо сообщит, что её нет.
#
# *Пример:*
#
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1


my_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
index_list = []
my_count = 0

print(my_list)

numb = input('Введите искомый элемент: ')

for i in range(len(my_list)):
    if numb == my_list[i]:
        index_list.append(i)

else:
    if len(index_list) < 2:
        print('Второго вхождения нет')
    else:
        print(f'Индекс второго вхождения: {index_list[1]}')

print(index_list)

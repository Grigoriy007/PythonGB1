# Задача 3. Напишите программу которая будет на вход принимать число N и выводить числа от -N до N

number = int(input('Add number: '))

my_list = []

for i in range(-number, number+1):
    my_list.append(i)

print(*my_list, sep=', ')
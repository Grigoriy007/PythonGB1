# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# *Пример:*
# - Для N = 5: 1, -3, 9, -27, 81

num = int(input('Введите число: '))

result = []

for i in range(num):
    result.append((-3)**i)

print(f"Для N = {num}: ", end='')
print(*result, sep=', ')

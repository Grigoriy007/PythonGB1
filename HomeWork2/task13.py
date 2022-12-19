# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

num = float(input('Введите число: '))

if num < 0:
    num = num * -1
num = str(num)
size = len(num)
result = []
sum = 0
for i in range(size):
    result.extend(num[i])
    if num[i] != str("."):
        sum += int(num[i])

print(f'Сумма цифр равна: {int(sum)}')



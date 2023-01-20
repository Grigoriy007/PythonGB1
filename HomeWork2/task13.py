# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

num = float(input('Введите число: '))

if num < 0:
    num = num * -1
num = str(num)
size = len(num)
sum = 0
summa = lambda a, b: a + b # Lambda

result = [num[i] for i in range(size)] # List complication

for i in result:
    if i != '.':
        p = int(i)
        sum = summa(sum, p)

print(f'Сумма цифр равна: {int(sum)}')



# Задайте список из n чисел последовательности (1 + 1/n)**n, выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

n = int(input('Введите число n (где n - количество чисел в списке): '))

result = [round((1+1/i)**i, 2) for i in range(1, n+1)] # List complication
sum = 0
summa = lambda a, b: a + b # Lambda

for i in result:
    sum = summa(sum, i)

print(result)
print(f'Сумма {sum}')


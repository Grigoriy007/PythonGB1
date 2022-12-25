# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

size = int(input('Задайте количество чисел Фибоначчи: '))

fibo1 = []
fibo2 = []
fibo1.append(0)
fibo1.append(1)
fibo2.append(0)
fibo2.append(1)

for i in range(size-1):
    numFib1 = fibo1[i] + fibo1[i+1]
    fibo1.append(numFib1)
    numFib2 = fibo2[i] - (fibo2[i + 1])
    fibo2.append(numFib2)

print(f'Список Фибонначи: {fibo1}')

for n in range(1, len(fibo1)):
    fibo1.insert(0, fibo2[n])

print(f'Список НегаФибонначи: {fibo2}')
print(f'Объединенный: {fibo1}')

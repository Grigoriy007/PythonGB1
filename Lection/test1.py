from random import randint

days = int(input('Введите количество рассматриваемых дней: '))

temp = []
long = []

for t in range(days):
    num = round(randint(-50, 51))
    temp.append(num)

print(temp)

count = 0
for i in temp:

    if i > 0:
        count = count + 1
    if i <= 0:
        long.append(count)
        count = 0

max = long[0]

for findMax in long:
    if findMax > max:
        max = findMax

print(long)
print(max)
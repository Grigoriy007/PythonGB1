# 1. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
# Пример:
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;

ex = '2 - 3    *4- 10    /2'
ex = ex.replace(' ', '')
ex = ex.replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ')
ex = ex.split()

while len(ex) > 1:
    i = 0
    while '*' in ex or '/' in ex:
        if ex[i] == '*':
            ex[i-1] = int(ex[i-1]) * int(ex[i+1])
            ex.pop(i)
            ex.pop(i)
        elif ex[i] == '/':
            ex[i - 1] = int(ex[i - 1]) / int(ex[i + 1])
            ex.pop(i)
            ex.pop(i)
        else:
            i += 1
    i = 0
    while '+' in ex or '-' in ex:
        if ex[i] == '+':
            ex[i-1] = int(ex[i-1]) + int(ex[i+1])
            ex.pop(i)
            ex.pop(i)
        elif ex[i] == '-':
            ex[i - 1] = int(ex[i - 1]) - int(ex[i + 1])
            ex.pop(i)
            ex.pop(i)
        else:
            i += 1


print(ex)
# Задача 4 программа будет принимать на вход дробь и показывать первую дробную часть числа

# number = float(input('Add a number: '))

# if number == int(number):
#     print('Целое')
# else:
#     print(int(number*10)%10)

number = input('Add a number: ')

number = number.split('.')

if len(number) < 2:
    print('Целое')

else:
    print(number[1][0])
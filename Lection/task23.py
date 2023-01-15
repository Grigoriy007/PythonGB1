# my_dict = {}
# n = int(input('Ввведите число: '))
#
# for i in range(1, n + 1):
#     my_dict[i] = 3 * i + 1
#
# print(my_dict)
# my_dict[2] = 'двойка'
# my_dict['2'] = 'тройка'
# print(my_dict)

# equetion = 'A*x*2 + B*x + C = 0'
new_equetion = 'x **2 - x + 6 = 0'
# disk = B**2 - 4 * A * C

def equetion(string: str):
    eq = []
    string = string.replace(' ', '').replace('=0', '').replace('+', ' ').replace('-', ' -').split(' ')
    for item in string:
        if item.startswith('x'):
            eq.append(1)
        elif item.startswith('-x'):
            eq.append(-1)
        else:
            eq.append(int(item.split('*x')[0]))
    return eq

a, b, c = equetion(new_equetion)
print(a)
print(b)
print(c)

equetion(new_equetion)
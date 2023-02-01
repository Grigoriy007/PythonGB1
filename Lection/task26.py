# В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного,
# чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

string = '1 3 4 5 6 8 9 11 13'
# my_list = string.split()
# for i in range(len(my_list)):
# my_list[i]=int(my_list[i])


my_list = list(map(int, string.split()))

for i in range(1, len(my_list)):
    if my_list[i] - 1 != my_list[i - 1]:
        print(my_list[i] - 1)

# my_list = list(map(int, string.split()))
#
# for i in range(len(my_list)-1):
#     if my_list[i]+1 == my_list[i+1]-1:
#         print(my_list[i]+1
# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# *Пример:*
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

my_list = [1, 2, 3, 5, 1, 5, 3, 10]

nums = {}

for item in my_list:
    nums[item] = nums.get(item, 0) + 1
    print(nums)

for key,value in nums.items():
    if value == 1:
        print(key)


# my_list = [1, 2, 3, 5, 1, 5, 3, 10]
# new_list = [x for x in my_list if my_list.count(x) == 1]
# print(my_list)
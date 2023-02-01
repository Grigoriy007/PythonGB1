# from random import randint as RI
# my_list = [RI(1, 10) for i in range(10)]
# my_list = {i:i**2 for i in range(10)}
# print(my_list)

# Напишите программу удаляющую из текста все слова содержащие абв

orig_text = 'Питон - наабверное самый лучший из худшиабвх языков'

# orig_list = []
#
# for i in orig_text.split():
#     if not 'абв' in i:
#         orig_list.append(i)
#
# print(' '.join(orig_list))

print((' '.join(list(filter(lambda x: 'абв' not in x, orig_text.split())))))

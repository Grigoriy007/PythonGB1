path = r'text.txt'


with open(path, 'r', encoding='UTF-8') as file:
    new_file = file.readlines()
# file.close()

for i in range(len(new_file)):
    new_file[i] = int(new_file[i].replace(r'\n', ''))
    # print(new_file[i])

print(new_file)
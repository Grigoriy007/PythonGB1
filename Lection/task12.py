# Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другую.

text = 'Напишите программу, в которой пользователь будет задавать две строки, ' \
       'а программа - определять количество вхождений одной строки в другую.'
print(text)

search = input('Введите искомый элемент: ')
text = text.split()
count = 0

for word in text:
    for char in word:
        if search == char:
            count += 1

print(f"В заданном тексте подстрока '{search}' встречается {count} раз")

# count = text.count(search) спец метод для посчета количетва раз


# for i in range(len(text)):                     # цикл по срезам
#         if search.lower() == text[i: i +len(search)].lower():
#             count += 1
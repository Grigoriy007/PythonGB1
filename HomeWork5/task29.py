# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc


text = list('aaaaaaaaaaaaaabbbcccccccccccr')
new_text = []

print(f'Изначальные данные: {text}')

count = 1
for i in range(1, len(text)):
    if text[i] == text[i-1]:
        count += 1
    else:
        new_text.append(''.join((str(count), text[i-1])))
        count = 1
new_text.append(''.join((str(count), text[i])))

new_text = ''.join(new_text)

print(f'Сжатые данные: {new_text}')

size = len(new_text)
data_recovery = []
j = 0

while j < size:
    s_int = ''
    a = new_text[j]
    while '0' <= a <= '9':
        s_int += a
        j += 1
        if j < size:
            a = new_text[j]
        else:
            break
    if s_int != '':
        long = int(s_int)
    b = new_text[j]
    for n in range(long):
        data_recovery.append(b)
    j += 1

data_recovery = ''.join(data_recovery)
print(f'Восстановленные данные: {data_recovery}')





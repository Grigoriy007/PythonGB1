# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

from random import randint

def FirstPlayer(konf):
    while konf > 0:
        choise1 = int(input('Введите количество конфет, которые Первый игрок собирается взять со стола: '))
        print(f'Первый игрок выбрал убрать со стола {choise1} конфет')
        if choise1 > konf:
            print(f'Вы выбрали количество конфет, превышающее то, что лежит на столе')
            return FirstPlayer(konf)
        elif choise1 > 28 or choise1 <= 0:
            print(f'Вы выбрали недопустимое значение, это запрещено условиями игры')
            return FirstPlayer(konf)
        konf -= choise1
        if konf == 0:
            winner = print(f'Победил Первый игрок')
            break
        print(f'Количество конфет, оставшихся на столе после выбора Первого игрока: {konf}')
        choise2 = randint(1, 28)
        if konf <= 28: choise2 = konf
        if konf <= 57 and konf >= 30:
            choise2 = konf - 29
        print(f'Второй игрок выбрал убрать со стола {choise2} конфет')
        konf -= choise2
        if konf == 0:
            winner = print(f'Победил Второй игрок')
            break
        print(f'Количество конфет, оставшихся на столе после выбора Второго игрока: {konf}')
    return winner

def SecondPlayer(konf):
    while konf > 0:
        choise2 = randint(1, 28)
        if konf <= 28: choise2 = konf
        if konf <= 57 and konf >= 30:
            choise2 = konf - 29
        print(f'Второй игрок выбрал убрать со стола {choise2} конфет')
        konf -= choise2
        if konf == 0:
            winner = print(f'Победил Второй игрок')
            break
        print(f'Количество конфет, оставшихся на столе после выбора Второго игрока: {konf}')
        choise1 = int(input('Введите количество конфет, которые Первый игрок собирается взять со стола: '))
        print(f'Первый игрок выбрал убрать со стола {choise1} конфет')
        if choise1 > konf:
            print(f'Вы выбрали количество конфет, превышающее то, что лежит на столе')
            return SecondPlayer(konf)
        elif choise1 > 28:
            print(f'Вы выбрали количество конфет более 28, это запрещено условиями игры')
            return SecondPlayer(konf)
        elif choise1 > 28 or choise1 <= 0:
            print(f'Вы выбрали недопустимое значение, это запрещено условиями игры')
            return SecondPlayer(konf)
        konf -= choise1
        if konf == 0:
            winner = print(f'Победил Первый игрок')
            break
        print(f'Количество конфет, оставшихся на столе после выбора Первого игрока: {konf}')
    return winner


candy = int(input('Введите количество конфет: '))
print(f'Количество конфет на столе: {candy}')
first_player = 1
second_player = 2
draw = randint(1, 2)
if draw == first_player:
    print(f'Первым ходит Первый игрок (Вы)')
    FirstPlayer(candy)
if draw == second_player:
    print(f'Первым ходит Второй игрок')
    SecondPlayer(candy)


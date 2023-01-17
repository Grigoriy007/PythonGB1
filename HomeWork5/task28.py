# Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом

from random import randint


def visual_tictactoe(any_list):
    print('-------------')
    for i in range(3):
        print('|', any_list[0 + i * 3], '|', any_list[1 + i * 3], '|', any_list[2 + i * 3], '|')
        print('-------------')


def hod_human_X(any_list):
    hod_X = input('Введите ячейку, на которую вы хотите поставить X: ')
    try:
        hod_X = int(hod_X)
    except:
        print('Некорректный ввод. Введите заново простое число')
        return hod_human_X(any_list)
    if 0 <= hod_X >= 10:
        print('Некорректный ввод. Введите простое число от 1 до 9')
        return hod_human_X(any_list)
    if str(any_list[hod_X - 1]) not in 'XO':
        any_list[hod_X - 1] = 'X'
    else:
        print('Данная ячейка занята')
        hod_human_X(any_list)
    return any_list


def hod_bot_O(my_list):
    tuple_victory = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for j in tuple_victory:
        for i in tuple_victory:
            if my_list[i[0]] == my_list[i[1]] == 'O' and str(my_list[i[2]]) not in 'XO':
                my_list[i[2]] = 'O'
                print(f'Ход бота {i[2] + 1}')
                return my_list
                break
            elif my_list[i[1]] == my_list[i[2]] == 'O' and str(my_list[i[0]]) not in 'XO':
                my_list[i[0]] = 'O'
                print(f'Ход бота {i[0] + 1}')
                return my_list
                break
            elif my_list[i[0]] == my_list[i[2]] == 'O' and str(my_list[i[1]]) not in 'XO':
                my_list[i[1]] = 'O'
                print(f'Ход бота {i[1] + 1}')
                return my_list
                break
        if my_list[j[0]] == my_list[j[1]] and str(my_list[j[2]]) not in 'XO':
            my_list[j[2]] = 'O'
            print(f'Ход бота {j[2] + 1}')
            return my_list
            break
        if my_list[j[1]] == my_list[j[2]] and str(my_list[j[0]]) not in 'XO':
            my_list[j[0]] = 'O'
            print(f'Ход бота {j[0] + 1}')
            return my_list
            break
        if my_list[j[0]] == my_list[j[2]] and str(my_list[j[1]]) not in 'XO':
            my_list[j[1]] = 'O'
            print(f'Ход бота {j[1] + 1}')
            return my_list
            break
    enter_hod = randint(0, 8)
    if str(my_list[enter_hod]) not in 'XO':
        my_list[enter_hod] = 'O'
    else:
        return bot(my_list)
    print(f'Ход бота {enter_hod+1}')
    return my_list


def control_win(any_list):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if any_list[each[0]] == any_list[each[1]] == any_list[each[2]]:
            return any_list[each[0]]


def main_game(any_list):
    visual_tictactoe(any_list)
    draw = randint(1, 2)
    for i in range(len(any_list)):
        if draw == 1:
            any_list = hod_human_X(any_list)
            visual_tictactoe(any_list)
            if i == 4:
                print('Ничья!')
                break
            if i > 0:
                tmp = control_win(any_list)
                if tmp:
                    print(f'{tmp} победил!!!')
                    break
            any_list = hod_bot_O(any_list)
            visual_tictactoe(any_list)
        else:
            any_list = hod_bot_O(any_list)
            visual_tictactoe(any_list)
            if i == 4:
                print('Ничья!')
                break
            if i > 0:
                tmp = control_win(any_list)
                if tmp:
                    print(f'{tmp} победил!!!')
                    break
            any_list = hod_human_X(any_list)
            visual_tictactoe(any_list)


tictactoe = list(range(1, 10))
main_game(tictactoe)
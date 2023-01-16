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


def hod_bot_O(any_list):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if any_list[each[0]] == any_list[each[1]]:
            if any_list[each[0]] == any_list[each[1]] == 'O':
                if str(any_list[each[2]]) not in 'XO':
                    any_list[each[2]] = 'O'
                    print(f'Бот выбрал ячейку: {each[2] + 1}')
                    return any_list
                    break
            else:
                if str(any_list[each[2]]) not in 'XO':
                    any_list[each[2]] = 'O'
                    print(f'Бот выбрал ячейку: {each[2] + 1}')
                    return any_list
                    break

        if any_list[each[1]] == any_list[each[2]]:
            if any_list[each[1]] == any_list[each[2]] == 'O':
                if str(any_list[each[0]]) not in 'XO':
                    any_list[each[0]] = 'O'
                    print(f'Бот выбрал ячейку: {each[0] + 1}')
                    return any_list
                    break
            else:
                if str(any_list[each[0]]) not in 'XO':
                    any_list[each[0]] = 'O'
                    print(f'Бот выбрал ячейку: {each[0] + 1}')
                    return any_list
                    break

        if any_list[each[0]] == any_list[each[2]]:
            if any_list[each[0]] == any_list[each[2]] == 'O':
                if str(any_list[each[1]]) not in 'XO':
                    any_list[each[1]] = 'O'
                    print(f'Бот выбрал ячейку: {each[1] + 1}')
                    return any_list
                    break
            else:
                if str(any_list[each[1]]) not in 'XO':
                    any_list[each[1]] = 'O'
                    print(f'Бот выбрал ячейку: {each[1] + 1}')
                    return any_list
                    break

    hod_O = randint(1, 9)
    if str(any_list[hod_O - 1]) not in 'XO':
        any_list[hod_O - 1] = 'O'
    else:
        return hod_bot_O(any_list)
    print(f'Бот выбрал ячейку: {hod_O}')
    return any_list


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
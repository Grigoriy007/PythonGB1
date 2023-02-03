import game
from loader import dp
from aiogram.types import Message
from random import randint
import time


@dp.message_handler(commands=['start'])
async def mes_start(message: Message):
    for duel in game.total:
        if message.from_user.id == duel[0]:
            await message.answer('Ты уже начал игру! Играй давай!')
            break
    else:
        await message.answer(f'Привет, {message.from_user.full_name}. '
                             f'Мы будем играть в конфеты.')
        await message.answer(f'По умолчанию количество конфет, лежащих на столе определено в размере 150. Если тебя это устраивает кликни на /DA'
                             f'\nЕсли не устраивает, ты можешь сам выбрать количество конфет, для этого введи /ch (количество конфет). '
                             f'Количество вводится через пробел')

@dp.message_handler(commands=['DA'])
async def mes_start_ch1(message: Message):
    await message.answer('Что ж, количество конфет установлено в размере по умолчанию - 150 штук')
    time.sleep(1)
    await message.answer('Теперь давай определим, кто ходит первый: Ты или я')
    time.sleep(1)
    draw_duel = draw()
    if draw_duel == 1:
        await message.answer('По результатам жеребьевки первым ходишь ты:) Бери от 1 до 28 конфеты...')
        my_game = [message.from_user.id, message.from_user.first_name, 150]
        game.total.append(my_game)
    if draw_duel == 2:
        await message.answer('По результатам жеребьевки хожу я, ну держись:) ')
        time.sleep(1)
        move = first_move_bot(150)
        await message.answer(f'Бот Виталий взял {move[0]} конфет и '
                             f'на столе осталось {move[1]}\n'
                             f'Теперь твой ход...')
        my_game = [message.from_user.id, message.from_user.first_name, move[1]]
        game.total.append(my_game)


@dp.message_handler(commands=['ch'])
async def mes_start_ch2(message: Message):
    count = message.text.split()[1]
    total_candy = int(count)
    await message.answer(f'Ты установил количество конфет в размере: {total_candy}.')
    time.sleep(1)
    await message.answer('Теперь давай определим, кто ходит первый: Ты или я')
    time.sleep(1)
    draw_duel = draw()
    if draw_duel == 1:
        await message.answer('По результатам жеребьевки первым ходишь ты:) Бери от 1 до 28 конфеты...')
        my_game = [message.from_user.id, message.from_user.first_name, total_candy]
        game.total.append(my_game)
    if draw_duel == 2:
        await message.answer('По результатам жеребьевки хожу я, ну держись:) ')
        time.sleep(1)
        move = first_move_bot(total_candy)
        await message.answer(f'Бот Виталий взял {move[0]} конфет и '
                             f'на столе осталось {move[1]}\n'
                             f'Теперь твой ход...')
        my_game = [message.from_user.id, message.from_user.first_name, move[1]]
        game.total.append(my_game)


def draw():
    draw_process = randint(1, 2)
    return draw_process

def first_move_bot(duel:int):
    remains = duel
    bot_take = randint(1, 28) if duel > 28 else duel
    if duel <= 57 and duel >= 30:
        bot_take = duel - 29
    remains -= bot_take
    return bot_take, remains



from loader import dp, bot
from aiogram import types


total = 150



@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    await message.answer(f'Привет {message.from_user.first_name}! Давненько тебя не видел!')

@dp.message_handler(commands=['OOP'])
async def mes_OOP(message: types.Message):
    await message.answer('Да что вы говорите!')

# @dp.message_handler(commands=['set'])
# async def mes_set(message: types.Message):
#     global total
#     count = message.text.split()[1]
#     total = int(count)
#     await message.answer(f'Установили новое количество конфет в размере: {total}')

@dp.message_handler(text=['лох'])
async def mes_loh(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer('Так говорить нельзя!')


@dp.message_handler()
async def mes_all(message: types.Message):
    global total
    if message.text.isdigit():
        total -= int(message.text)
        await bot.send_message(message.from_user.id, f'Конфет на столе осталось - {total}')
    else:
        await bot.send_message(message.from_user.id, f'Введи ка ты число майн фройнд')
    # await message.answer(f'Гляди, что поймал - {message.text}')
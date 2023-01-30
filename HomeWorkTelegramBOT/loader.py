from aiogram import Bot, Dispatcher
import os

# bot = Bot('6118091631:AAH5AvzmOWnY8MtDO80CEdC-z8JkyP4WYf0')
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot)

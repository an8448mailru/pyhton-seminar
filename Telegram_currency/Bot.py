from aiogram import Bot, Dispatcher, executor, types
import logging
from os import getenv
import pars
# Токен вашего бота
bot = Bot(token=getenv('TOKEN'))
# Диспетчер для работы бота
Dp = Dispatcher(bot)
# Логирование бота
logging.basicConfig(level=logging.INFO)

@Dp.message_handler(commands='start')
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['/dollar', '/euro']
    keyboard.add(*buttons)
    await message.answer("Привет", reply_markup=keyboard)

@Dp.message_handler(commands='dollar')
async def dollar(message: types.Message):
    await message.answer(f'Курс доллара: {pars.dollar()}')

@Dp.message_handler(commands='euro')
async def euro(message: types.Message):
    await message.answer(f'Курс евро: {pars.euro()}')


# Запуск бота
executor.start_polling(Dp, skip_updates=True)
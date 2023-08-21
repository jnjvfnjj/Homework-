from aiogram import Bot, Dispatcher, types,  executor

bot = Bot(token= '6019368294:AAG6Qy3xEtHTy5vbo1D5MW07sA_sz-Tkz-4')
dp = Dispatcher(bot)

import random
num = str(random.randint(1,3))
print(num)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer(': Я загадал число от 1 до 3 угадайте: ')

@dp.message_handler()
async def one(message:types.Message):
    if message.text == num:
        await message.answer('Правильно вы отгадали')
        await message.answer_photo('https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg')
    else:
        await message.answer_photo('https://media.makeameme.org/created/sorry-you-lose.jpg')

executor.start_polling(dp)
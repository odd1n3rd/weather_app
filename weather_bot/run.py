#чобы работало
import asyncio
import logging
#чобы телеграм работало
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
#чобы именно мой бот работало
from config import TOKEN
#чобы была погода
from weather import getweather
bot = Bot(token = TOKEN)
dp = Dispatcher()


@dp.message(Command('wthr'))
async def get_weather(message: Message):
    await message.answer(f'ну жди дождя, а температура {get_weather}')


@dp.message(CommandStart)
async def cmd_start(message: Message):
    await message.answer('хуй')


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('end')
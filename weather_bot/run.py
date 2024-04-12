#чобы работало
import asyncio
import logging
#чобы телеграм работало
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
#чобы именно мой бот работало
from config import TOKEN
from handlers import rtr

bot = Bot(token = TOKEN)
dp = Dispatcher()


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    dp.include_router(rtr)
    await dp.start_polling(bot)


if __name__ == '__main__':
#    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('end')
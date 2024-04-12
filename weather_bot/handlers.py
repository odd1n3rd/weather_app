from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
#чобы была погода
from weather import getweather

router = Router()

@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer('Привет! Я тестовый бот, могу подсказать тебе погоду, \
                         температуру за окном или на другом конце света)\
                         Напиши название города и я пришлю тебе информацию')

@router.message(F.text)
async def get_weather(message: Message):
    try:
        await message.answer(f'температура {getweather(message.text)[1]}')
    except:
        await message.answer('кажется кто-то хочет меня наебать, не пройдет')





# @rtr.message(Command('wthr'))
# async def get_weather(message: Message):
#     await message.answer(f'ну жди дождя, а температура {getweather()[1]}')
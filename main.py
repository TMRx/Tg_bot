import asyncio
import signal
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('TOKEN')

if not TOKEN:
    raise ValueError("TOKEN не знайдено в змінних середовища!")

bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher()


@dp.message(CommandStart()) 
async def start_cmd(message: types.Message) -> None: 
    await message.answer('Its command start')


@dp.message()
async def echo(message: types.Message) -> None:
    text: str | None = message.text

    if text in ['hi', 'привіт', 'hello', 'Привіт' ]:
        await message.answer('І тобі привіт!')
    elif text in ['Бувай', 'бувай']:
        await message.answer('І тобі бувай!')
    else:
        await message.answer(message.text)        


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
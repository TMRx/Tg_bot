import asyncio
import signal
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Hi!')


async def main():
    loop = asyncio.get_event_loop()

    stop_event = asyncio.Event()

    def shutdown():
        print("Shutting down...")
        stop_event.set()

    loop.add_signal_handler(signal.SIGINT, shutdown)
    loop.add_signal_handler(signal.SIGTERM, shutdown)

    print("""Starting bot""")
    await dp.start_polling(bot, shutdown_event=stop_event)
    print("Bot stopped")


if __name__ == '__main__':    
    asyncio.run(main())
    
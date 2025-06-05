from aiogram import types, Router
from aiogram.filters import CommandStart, Command

user_private_router = Router()


@user_private_router.message(CommandStart()) 
async def start_cmd(message: types.Message) -> None: 
    await message.answer("Привіт, я віртуальний помічник")
         

@user_private_router.message(Command('menu'))
async def menu_cmd(message: types.Message) -> None:
    await message.answer("Ось меню:")        

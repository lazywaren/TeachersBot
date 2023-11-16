from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

# Инициализируем роутер уровня модуля
router = Router()


@router.message(Command(commands='admin'))
async def admin_start(message: Message):
    await message.reply("Hello, admin!")

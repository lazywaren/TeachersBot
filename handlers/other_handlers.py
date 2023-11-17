from aiogram import Router
from aiogram.types import Message


# Инициализируем роутер уровня модуля
router = Router()


@router.message()
async def send_echo(message: Message):
    await message.reply(text='Неизвестная команда, пропишите /start для того, чтобы ознакомиться с функционалом бота')
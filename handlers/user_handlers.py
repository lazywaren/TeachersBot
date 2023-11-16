from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

# Инициализируем роутер уровня модуля
router = Router()


@router.message(Command(commands='start'))
async def process_start_command(message: Message):
    await message.answer('Добро пожаловать. Для того, чтобы увидеть список доступных команд, введите /help')


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )


@router.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)

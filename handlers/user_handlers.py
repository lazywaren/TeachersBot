from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.filters import Command


async def user_start(message: Message):
    await message.reply("Hello, user!")


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")

    # Этот хэндлер будет срабатывать на команду "/start"

    @dp.message(Command(commands=["start"]))
    async def process_start_command(message: Message):
        await message.answer('Добро пожаловать. Для того, чтобы увидеть список доступных команд, введите /help')

    # Этот хэндлер будет срабатывать на команду "/help"

    @dp.message(Command(commands=['help']))
    async def process_help_command(message: Message):
        await message.answer(
            'Напиши мне что-нибудь и в ответ '
            'я пришлю тебе твое сообщение'
        )

    # Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
    # кроме команд "/start" и "/help"

    @dp.message()
    async def send_echo(message: Message):
        await message.reply(text=message.text)
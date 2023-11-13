from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from environs import Env
from filters.isadmin import isadmin

env = Env()
env.read_env()

bot_token = env('BOT_TOKEN')
admin_id = env.int('ADMIN_ID')

bot = Bot(token=bot_token)
dp = Dispatcher()

# Этот хэндлер будет срабатывать на команду "/start"


@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


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
    if isadmin(message):
        await message.reply(text="Привет, админ")
    else:
        await message.reply(text=message.text)


if __name__ == '__main__':
    dp.run_polling(bot)

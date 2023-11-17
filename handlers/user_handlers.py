from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from keyboards.keyboards import keyboard
from keyboards.inlinekeyboards import inlinekeyboard

# Инициализируем роутер уровня модуля
router = Router()


@router.message(Command(commands='start'))
async def process_start_command(message: Message):
    await message.answer(text='''<b>Добро пожаловать.</b>
Здесь вы можете найти бесплатные пособия, которые помогут вам быстрее и эффективнее учить английский.
Помимо этого вы можете приобрести авторские методическия пособия по различным темам, включая популярные фильмы, сериалы и видео.
Для доступа к бесплатным пособиям, нажмите <b><u>Бесплатные пособия📚</u></b>
Для доступа к авторским пособиям, нажмите <b><u>Авторские пособия👩🏻‍🏫</u></b>
Для пополнения баланса, а также доступа к уже купленным пособиям, воспользуйтесь кнопкой <b><u>Личный кабинет🏠</u></b>
Если у вас возникли какие-либо вопросы по функционалу бота, нажмите <b><u>Поддержка👥</u></b>
    ''',
    parse_mode='HTML',
    reply_markup=keyboard)


@router.message(F.text == 'Бесплатные пособия📚')
async def process_freebooks_answer(message: Message):
    await message.answer(
        text='Список доступных для скачивания пособий, для того чтобы выбрать пособие, нажмите на соответствующее название:',
        reply_markup=inlinekeyboard
    )


@router.message(F.text == 'Авторские пособия👩🏻‍🏫')
async def process_paidbooks_answer(message: Message):
    await message.answer(
        text='Здесь будет список авторских пособий'
    )


@router.message(F.text == 'Личный кабинет🏠')
async def process_account_answer(message: Message):
    await message.answer(
        text='Здесь будет личный кабинет'
    )


@router.message(F.text == 'Поддержка👥')
async def process_help_answer(message: Message):
    await message.answer(
        text="Если у вас возникли какие-либо вопросы, напишите <b>Администратору</b> : @WaREN_god",
        parse_mode="HTML"
    )


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(
        'Хендлер для обработки команды /help'
    )

@router.callback_query(F.data == 'button_1_is_pressed')
async def button_1_is_pressed(callback : CallbackQuery):
    await callback.answer()

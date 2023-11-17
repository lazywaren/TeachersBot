from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from sources.sources import get_available_books

available_books = get_available_books()

inline_keyboard = []

for index, book in enumerate(available_books):
    inline_keyboard.append([InlineKeyboardButton(text=book, callback_data=f'button_{index}_is_pressed')])

inlinekeyboard = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
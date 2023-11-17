from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)


FreeBooksButton = KeyboardButton(text='Бесплатные пособия📚')
PaidBooksButton = KeyboardButton(text='Авторские пособия👩🏻‍🏫')
PersonalAccount = KeyboardButton(text='Личный кабинет🏠')
HelpButton = KeyboardButton(text='Поддержка👥')

keyboard = ReplyKeyboardMarkup(keyboard=[[FreeBooksButton, PaidBooksButton],
                                        [PersonalAccount, HelpButton]],
                                        resize_keyboard=True,
                                        one_time_keyboard=False)
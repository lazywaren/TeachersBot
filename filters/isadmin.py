from environs import Env
from aiogram.types import Message

env = Env()
env.read_env()

admin_id = env.int('ADMIN_ID')


def isadmin(message: Message):
    if message.from_user.id == admin_id:
        return True
    else:
        return False

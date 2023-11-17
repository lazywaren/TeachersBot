import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage, Redis

from config_data.config import Config, load_config
from handlers import user_handlers, admin_handlers, other_handlers
from keyboards.set_menu import set_main_menu

logger = logging.getLogger(__name__)


async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)s:%(lineno)d #%(levelname)-8s "
        "[%(asctime)s] - %(name)s - %(message)s",
    )

    logger.info("Starting bot")

    config: Config = load_config(".env")

    bot_token = config.tg_bot.token
    # bot_admin = config.tg_bot.ADMIN_ID

    redis = Redis(host='localhost')

    storage = RedisStorage(redis=redis)

    bot = Bot(bot_token, parse_mode='HTML')
    dp = Dispatcher(storage=storage)

    # Регистриуем роутеры в диспетчере
    dp.include_router(admin_handlers.router)
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    await set_main_menu(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped")

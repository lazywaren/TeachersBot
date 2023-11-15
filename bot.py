import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage, Redis

from config_data.config import Config, load_config
from handlers import user_handlers


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

    bot = Bot(bot_token)
    dp = Dispatcher(storage=storage)

    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped")

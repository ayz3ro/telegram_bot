import asyncio

from aiogram import Dispatcher
from bot_token import bot
from bot.handlers.command import router as command_router
from bot.handlers.start_callback import router as callback_router


async def main():
    dp = Dispatcher()
    dp.include_routers(command_router, callback_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')

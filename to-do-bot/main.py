import asyncio
from aiogram import Bot, Dispatcher
from handlers import common, tasks


# Запуск бота
async def main():
    bot = Bot(token="secret")
    dp = Dispatcher()
    dp.include_router(common.router_common)
    dp.include_router(tasks.router_tasks)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

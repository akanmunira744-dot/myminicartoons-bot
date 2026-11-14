import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Сәлем! ❤️ Мен MyMiniCartoons ботымын!\n\n"
        "Мен арқылы болашақта:\n"
        "🎬 Мультфильм жасай аласың\n"
        "🖼️ Суретті жандандыра аласың\n"
        "🎥 Видео жасай аласың\n\n"
        "Жақында кездескенше!"
    )


@dp.message()
async def messages(message: Message):
    await message.answer(
        "Хабарламаңды алдым! ❤️\n"
        "Жаңа функциялар жақында қосылады."
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

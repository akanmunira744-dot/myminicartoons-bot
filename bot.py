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
        "🎬 Мультфильм жасау\n"
        "🖼️ Суретті жандандыру\n"
        "🎥 Видео жасау\n\n"
        "Қай функцияны таңдайсың?"
    )

@dp.message()
async def reply(message: Message):
    await message.answer(
        "Керемет! ❤️ Жаңа функциялар жақында қосылады."
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

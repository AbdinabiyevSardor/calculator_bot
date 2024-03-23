import aiogram
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram import F
from aiogram.types import Message
from aiogram import types
import asyncio
import logging
import sys
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import ContentType, File, Message
TOKEN = "6747702351:AAHovbu0HzQGsoY2LrgMPuCeWChXVTfqUD8"

dp = Dispatcher()
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

@dp.message(CommandStart())
async def start_command(message:Message):

    await message.answer(text="Assalomu alaykum! Misolni yozing")

@dp.message(F.text)
async def calculator_aiogram(message: Message):
    try:
        await message.answer(text=f"{message.text} = <b>{eval(message.text)}</b>")
    
    except ZeroDivisionError:
        await message.answer(text=f"Nolga bo'lish mumkin emas!!!")
    
    except:
        await message.answer(text="Iltimos, misol yozing!!!")
    
    
    
async def main() -> None:
    global bot
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


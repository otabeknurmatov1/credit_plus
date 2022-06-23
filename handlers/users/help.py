from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from filters import isPrivate
from loader import dp


@dp.message_handler(isPrivate(), CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam",
            "/admin - Admin bilan bog'lanish",
            "/til - Tilni o'zgartirish")
    
    await message.answer("\n".join(text))

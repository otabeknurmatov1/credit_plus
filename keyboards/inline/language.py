from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

lang = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="O'zbek 🇺🇿", callback_data="uzbeklang"),
            InlineKeyboardButton(text="Русскый 🇷🇺", callback_data="ruslang"),
        ],
    ]
)

changlang = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="O'zbek 🇺🇿", callback_data="changeuz"),
            InlineKeyboardButton(text="Русскый 🇷🇺", callback_data="changeru"),
        ],
    ]
)
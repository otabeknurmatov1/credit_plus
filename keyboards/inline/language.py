from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

lang = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="O'zbek ๐บ๐ฟ", callback_data="uzbeklang"),
            InlineKeyboardButton(text="ะ ัััะบัะน ๐ท๐บ", callback_data="ruslang"),
        ],
    ]
)

changlang = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="O'zbek ๐บ๐ฟ", callback_data="changeuz"),
            InlineKeyboardButton(text="ะ ัััะบัะน ๐ท๐บ", callback_data="changeru"),
        ],
    ]
)
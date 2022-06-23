from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

numUz = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="📲 Telefon raqamni yuborish", request_contact=True),
        ],
    ],
    resize_keyboard=True,
)

numRu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="📲 Отправить номер телефона", request_contact=True),
        ],
    ],
    resize_keyboard=True,
)
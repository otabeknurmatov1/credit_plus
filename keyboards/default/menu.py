from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menuUz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Biz haqimizda"),
        ],
        [
            KeyboardButton(text="Kredit rasmiylashtirish"),
        ],
        [
            KeyboardButton(text="Kredit olish va tolash shartlar")
        ],
        [
            KeyboardButton(text="To'lovlar")
        ]
    ],
    resize_keyboard=True
)

menuRu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="О нас"),

        ],
        [
            KeyboardButton(text="Заявка на получение ссуды"),
        ],
        [
            KeyboardButton(text="Условия кредита и погашения")
        ],
        [
            KeyboardButton(text="Платежи")
        ]
    ],
    resize_keyboard=True
)

backUz = ReplyKeyboardMarkup(
    keyboard=[
        [
          KeyboardButton(text="◀️ Ortga qaytish")
        ],
    ],
    resize_keyboard=True
)

backRu = ReplyKeyboardMarkup(
    keyboard=[
        [
          KeyboardButton(text="◀️ Назад")
        ],
    ],
    resize_keyboard=True
)
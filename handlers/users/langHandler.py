from aiogram import types
from aiogram.types import CallbackQuery

from filters import isPrivate
from keyboards.default.menu import menuUz, menuRu
from keyboards.inline.language import lang, changlang
from loader import dp


@dp.message_handler(isPrivate(), commands="til")
async def change_lang(msg: types.Message):
    await msg.reply(
        "O'zgartirmoqchi bo'lgan tilingizni kiritishingiz mumkin 😊\n\nВы можете ввести язык, который хотите изменить 😊",
        reply_markup=changlang)


@dp.callback_query_handler(text="changeuz")
async def change_uz(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Til muvaffaqiyatli o'zgartirildi ☺️", reply_markup=menuUz)


@dp.callback_query_handler(text="changeru")
async def change_ru(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Язык успешно изменен ☺️", reply_markup=menuRu)

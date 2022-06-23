from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.types import CallbackQuery

from filters import isPrivate
from keyboards.default.menu import menuUz
from keyboards.default.num import numUz
from keyboards.inline.language import lang, changlang
from loader import dp
from states.PD import userData


@dp.message_handler(isPrivate(), commands="start")
async def form_start(msg: types.Message):
    await msg.answer("🇺🇿Assalomu alaykum Xurmatli mijoz!\nO’zingizga qulay tilni tanlang ☺️: \n\n🇷🇺Здравствуйте Уважаемый клиент!\nВыберите язык, который вам подходит ☺:️", reply_markup=lang)
    await msg.answer(reply_markup=ReplyKeyboardRemove())


@dp.callback_query_handler(text="uzbeklang")
async def form_start(call: CallbackQuery):
    await call.answer("Siz O'zbek tilini tanladingiz!", show_alert=True)
    await call.answer(cache_time=60)
    await call.message.answer("Iltimos <b>ismingiz</b> va <b>familyangizni</b> kiriting kiriting", reply_markup=None)
    await userData.name.set()


@dp.message_handler(state=userData.name)
async def full_name(msg: types.Message, state: FSMContext):
    fullName = msg.text
    await state.update_data({
        "name": fullName,
    })
    await msg.answer("Iltimos telefon raqamingizni yuboring.", reply_markup=numUz)
    await userData.next()


@dp.message_handler(content_types=types.ContentTypes.CONTACT ,state=userData.phoneNumber)
async def full_name(msg: types.Message, state: FSMContext):
    number = msg.text
    await state.update_data({
        "number": number,
    })

    data = await state.get_data()
    user_name = data.get("name")
    user_number = data.get("number")

    await msg.answer(f"Xush kelibsiz xurmatli <b>{user_name}</b>")
    await msg.answer(f"Pastdagi tugmalarni bosib o'zingiz hohlagan savolga-javob olishingiz mumkin\n\nAgarda admin bilan bog'lanishni hohlasangiz /admin buyrug'ini bosing!", reply_markup=menuUz)
    await state.finish()

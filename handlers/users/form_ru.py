from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboards.default.menu import menuUz, menuRu
from keyboards.default.num import numRu
from keyboards.inline.language import lang
from loader import dp
from states.PD import userData, userDataRu

@dp.callback_query_handler(text="ruslang")
async def form_start(call: CallbackQuery):
    await call.answer("Вы выберали Русскый язык!", show_alert=True)
    await call.answer(cache_time=60)
    await call.message.delete()
    await call.message.answer("Пожалуйста, введите свое <b>имя</b> и <b>фамилию</b>", reply_markup=None)
    await userDataRu.nameRu.set()


@dp.message_handler(state=userDataRu.nameRu)
async def full_name(msg: types.Message, state: FSMContext):
    fullName = msg.text
    await state.update_data({
        "name": fullName,
    })
    await msg.answer("Пожалуйста, пришлите свой номер телефона...", reply_markup=numRu)
    await userDataRu.next()


@dp.message_handler(content_types=types.ContentTypes.CONTACT, state=userDataRu.phoneNumberRu)
async def full_name(msg: types.Message, state: FSMContext):
    number = msg.text
    await state.update_data({
        "number": number,
    })

    data = await state.get_data()
    user_name = data.get("name")
    user_number = data.get("number")

    await msg.answer(f"Добро пожаловать, <b>{user_name}</b>")
    await msg.answer(f"Вы можете получить нужный вопрос и ответ, нажав кнопки ниже \n\nЕсли вы хотите связаться с администратором нажмите /admin!", reply_markup=menuRu)
    await state.finish()

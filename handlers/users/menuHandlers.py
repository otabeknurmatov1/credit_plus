from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.default.menu import menuUz, backUz, backRu, menuRu
from loader import dp


@dp.message_handler(text="Biz haqimizda")
async def about_us(msg: Message):
    await msg.answer("Tez orada ma'lumot yukalanadi...", reply_markup=backUz)

@dp.message_handler(text="Kredit rasmiylashtirish")
async def about_us(msg: Message):
    await msg.answer("Tez orada ma'lumot yukalanadi...", reply_markup=backUz)

@dp.message_handler(text="Kredit olish va tolash shartlar")
async def about_us(msg: Message):
    await msg.answer("Tez orada ma'lumot yukalanadi...", reply_markup=backUz)

@dp.message_handler(text="To'lovlar")
async def about_us(msg: Message):
    await msg.answer("Tez orada ma'lumot yukalanadi...", reply_markup=backUz)

@dp.message_handler(text="◀️ Ortga qaytish")
async def about_us(msg: Message):
    await msg.answer("<b>Xizmat turini tanlang...</b>", reply_markup=menuUz)

# Ru version
@dp.message_handler(text="О нас")
async def about_us(msg: Message):
    await msg.answer("Информация будет загружена в ближайшее время...", reply_markup=backRu)

@dp.message_handler(text="Заявка на получение ссуды")
async def about_us(msg: Message):
    await msg.answer("Информация будет загружена в ближайшее время...", reply_markup=backRu)

@dp.message_handler(text="Условия кредита и погашения")
async def about_us(msg: Message):
    await msg.answer("Информация будет загружена в ближайшее время...", reply_markup=backRu)

@dp.message_handler(text="Платежи")
async def about_us(msg: Message):
    await msg.answer("Информация будет загружена в ближайшее время...", reply_markup=backRu)

@dp.message_handler(text="◀️ Назад")
async def about_us(msg: Message):
    await msg.answer("<b>Выберите вид услуги...</b>", reply_markup=menuRu)
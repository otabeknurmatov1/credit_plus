from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushurish"),
            types.BotCommand("til", "Tilni o'zgartirish"),
            types.BotCommand("admin", "Admin bilan bog'lanish"),
            types.BotCommand("help", "Yordam"),
        ]
    )

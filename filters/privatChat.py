from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class isPrivate(BoundFilter):
    async def check(self, msg: types.Message):
        return msg.chat.type == types.ChatType.PRIVATE

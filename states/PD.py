from aiogram.dispatcher.filters.state import State, StatesGroup


class userData(StatesGroup):
    name = State()
    phoneNumber = State()


class userDataRu(StatesGroup):
    nameRu = State()
    phoneNumberRu = State()

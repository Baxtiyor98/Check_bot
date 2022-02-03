from aiogram.dispatcher.filters.state import State, StatesGroup


class Homework(StatesGroup):
    name = State()
    file = State()
    send = State()
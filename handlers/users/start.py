from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters.group_filter import IsGroup
from filters.private_filter import IsPrivate
from aiogram.dispatcher.storage import FSMContext
from states.states import Homework

from loader import dp

@dp.message_handler(IsGroup(),ADMINS,CommandStart(),state='*')
async def bot_start(message: types.Message):
    await message.reply(f"Assalom alaykum! {message.from_user.first_name}\nGuruh vazifalari nazorat qilinmoqda")
    return ''

@dp.message_handler(IsGroup(),CommandStart(),state='*')
async def bot_start(message: types.Message):
    await message.reply(f"Assalom alaykum! {message.from_user.first_name}\nChatga o'tib vazifalarni yuboring😎\nHar kuni vazifalarni yubormasangiz dangasalar ro'yhatiga qo'shib qo'yaman")
    return ''

@dp.message_handler(IsPrivate(),CommandStart(),state='*')
async def bot_start(message: types.Message,state:FSMContext):
    await message.answer(f"Assalom alaykum!\nIltimos, ismingizni kiriting:")
    await state.finish()
    await Homework.name.set()

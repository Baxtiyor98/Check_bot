from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import ADMINS
from filters.group_filter import IsGroup
from filters.private_filter import IsPrivate
from aiogram.dispatcher.storage import FSMContext
from states.states import Homework
from aiogram.types.reply_keyboard import ReplyKeyboardRemove

from loader import dp

@dp.message_handler(IsGroup(),CommandStart(),state='*')
async def bot_start(message: types.Message):
    user = types.User.get_current()
    if str(user.id) in ADMINS:
        await message.reply(f"Assalom alaykum! {message.from_user.first_name}\nGuruh vazifalari nazorat qilinmoqda")
    else:
        await message.reply(f"Assalom alaykum! {message.from_user.first_name}\nChatga o'tib vazifalarni yuboring😎\nHar kuni vazifalarni yubormasangiz dangasalar ro'yhatiga qo'shib qo'yaman")
    return ''

@dp.message_handler(IsPrivate(),CommandStart(),state='*')
async def bot_start(message: types.Message,state:FSMContext):
    a = await message.answer('.',reply_markup=ReplyKeyboardRemove())
    await a.delete()
    await message.answer(f"Assalom alaykum!\nIltimos, ismingizni kiriting:")
    await state.finish()
    await Homework.name.set()

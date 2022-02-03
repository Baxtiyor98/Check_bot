from aiogram import types
from filters.private_filter import IsPrivate

from loader import dp


# Echo bot
@dp.message_handler(IsPrivate,state=None)
async def bot_echo(message: types.Message):
    await message.answer(_(f"{message.from_user.first_name} user tomonidan xato foydalanish!!!\nChatga o'tib vazifalarni yuboring😎"))

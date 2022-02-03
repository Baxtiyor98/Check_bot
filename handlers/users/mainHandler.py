from aiogram import types
from aiogram.types.message import Message
from data.config import ADMINS
from aiogram.dispatcher.storage import FSMContext
from states.states import Homework
from keyboards.default.send import continueKey
import datetime
from loader import dp,bot

@dp.message_handler(content_types=types.ContentTypes.TEXT,state=Homework.name)
@dp.message_handler(state=Homework.name)
async def get_name(message:Message, state:FSMContext):
    user = types.User.get_current()
    await state.update_data({
        'name':message.text,
        'id':user.id
        })
    await message.answer(f"{message.text}, iltimos uy vazifalarini python file shaklida yuboring(main.py). Fayllar yuborilganidan so'ng 🔼 Yuklash 🔼 tugmasini bosing",reply_markup=continueKey)
    await Homework.file.set()

@dp.message_handler(content_types=types.ContentTypes.TEXT,state=Homework.file)
@dp.message_handler(content_types=types.ContentTypes.DOCUMENT,state=Homework.file)
async def get_files(message:Message, state:FSMContext):
    user = types.User.get_current()
    data = await state.get_data()
    try:
        if int(data['id'])==int(user.id) and message.document.file_name[-2:]=='py':
            try:
                files = data['file']
            except:
                files = []
            files.append(message.document.file_id)
            await state.update_data({
                'file':files
                })
        else:
            await message.reply('Qabul qilinmadi❌❌❌\nPython file yuboring(main.py)')
    except:
        pass
    if int(data['id'])==int(user.id) and message.text=='🔼 Yuklash 🔼':
        try:
            if data['file']:
                for i in data['file']:
                    await bot.send_document(chat_id=ADMINS[0],document=i)
                await bot.send_message(chat_id=ADMINS[0],text=f"{data['name']}ning uy vazifalari👆👆👆\nYuborilgan:{datetime.datetime.now}")
                await message.answer('Vazifalar yuborildi✅✅✅')
                files = []
                await state.update_data({
                    'file':[]
                    })
            else:
                await message.reply('Hali file yubormadingiz!!!')
        except:
            await message.answer('Hali file yubormadingiz!!!')
            return ''


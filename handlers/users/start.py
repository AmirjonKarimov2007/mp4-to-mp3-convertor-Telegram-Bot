import logging
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery
from filters import IsUser, IsSuperAdmin, IsGuest
from filters.admins import IsAdmin
from keyboards.inline.main_menu_super_admin import main_menu_for_super_admin, main_menu_for_admin
from loader import db,dp,bot
import asyncpg
logging.basicConfig(level=logging.INFO)

@dp.callback_query_handler(text="start")
async def bot_echo(call: CallbackQuery):
    await call.answer(cache_time=1)
    user = call.from_user
    await call.message.delete()
    try:
        await db.add_user(user_id=user.id, name=user.first_name)
    except:
        pass

    await bot.send_message(chat_id=user.id, text="<b>✅Botdan bemalol foydalanishingiz mumkin.</b>")

@dp.message_handler(IsAdmin(), CommandStart(), state="*")
async def bot_start_admin(message: types.Message):
    await message.answer(f"Assalom alaykum Admin, {message.from_user.full_name}!",
                         reply_markup=main_menu_for_admin)
@dp.message_handler(IsSuperAdmin(), CommandStart(), state="*")
async def bot_start_super_admin(message: types.Message):
    await message.answer(f"<b>Assalom alaykum Bosh Admin, <a href='tg://user?id={message.from_user.id}'>{message.from_user.full_name}</a>!</b>",
                         reply_markup=main_menu_for_super_admin)

@dp.message_handler(IsGuest(), CommandStart(), state="*")
async def bot_start(message: types.Message):
    user = message.from_user
    username = message.from_user.username
    try:
        await db.add_user(user_id=user.id,username=username, name=user.first_name)
    except asyncpg.exceptions.UniqueViolationError:
        await db.select_user(user_id=message.from_user.id)
    except Exception as ex:
        print(f"IsGuest:{ex}")

    if 2 == len(message.text.split(' ')) > 0:
        return await idsave(message, message.text.split(' ')[1])
    user_id = message.from_user.first_name
    await message.reply(f"<b>👋🏻 Assalomu Aleykum {user_id} botimizga Xush kelipsiz!</b>")

@dp.message_handler(IsUser(), CommandStart(), state="*")
async def bot_start(message: types.Message):
    user = message.from_user
    username = message.from_user.username
    try:
        await db.add_user(user_id=user.id,username=username, name=user.first_name)
    except asyncpg.exceptions.UniqueViolationError:
        await db.select_user(user_id=message.from_user.id)
    except Exception as ex:
        print(f"IsUser:{ex}")

    if 2 == len(message.text.split(' ')) > 0:
        return await idsave(message, message.text.split(' ')[1])
    user_id = message.from_user.first_name
    user_id = message.from_user.first_name
    await message.reply(f"<b>👋🏻 Assalomu Aleykum {user_id} botimizga Xush kelipsiz!</b>")


async def idsave(message: types.Message, text=None):
    try:
        argument = message.get_args()

        if text == None:
            text = message.text or argument
        if text.isdigit():
            IDTXT1 = await db.select_files(id=text)
            if len(IDTXT1) > 0:
                IDTXT = IDTXT1[0]
                if IDTXT[1] == 'document':
                    await message.answer_document(IDTXT[2], caption=IDTXT[3])
                elif IDTXT[1] == 'video':
                    await message.answer_video(IDTXT[2], caption=IDTXT[3])
                elif IDTXT[1] == 'photo':
                    await message.answer_photo(IDTXT[2], caption=IDTXT[3])
                elif IDTXT[1] == 'audio':
                    await message.answer_audio(IDTXT[2], caption=IDTXT[3])
                elif IDTXT[1] == 'voice':
                    await message.answer_voice(IDTXT[2], caption=IDTXT[3])
            else:
                await message.answer("Hech narsa topilmadi 😔")
    except:
        await message.answer("Xatolik yuzaga keldi, qayta urinb ko'ring 😔")
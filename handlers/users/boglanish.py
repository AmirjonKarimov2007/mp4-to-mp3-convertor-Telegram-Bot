from aiogram import types
from aiogram.utils.callback_data import CallbackData
from aiogram.types import Message, CallbackQuery
from loader import dp, bot
from keyboards.inline.boglanish_button import check
from data.config import ADMINS
from aiogram.types import ReplyKeyboardRemove


@dp.message_handler(text="📞Bog'lanish")
async def yes_or_no(message: types.Message):
  await message.answer("Rostdan ham admin bilan bog'lanishni hohlaysizmi?",
                       reply_markup=check)


@dp.message_handler(text='admincall')
@dp.callback_query_handler(text='ha')
async def yes_or_no(call: CallbackQuery):
  await bot.send_message(ADMINS[-1],
                         f"@{call.from_user.username} siz bilan boglanmoqchi")
  await call.message.answer('Adminga boglanish buyicha arizangiz yetkazildi',
                            reply_markup=ReplyKeyboardRemove(selective=None))
  await call.message.edit_reply_markup()
  await call.message.delete()


@dp.callback_query_handler(text='Yoq')
@dp.message_handler(text="📞Bog'lanish")
async def yes_or_no(call: CallbackQuery):
  await call.message.delete()

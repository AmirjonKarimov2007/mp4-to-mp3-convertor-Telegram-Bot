import logging

import asyncpg
from aiogram import types
from data.config import CHANNELS
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from keyboards.inline.subscrtion import channels
from loader import bot, dp,db
from aiogram import types
from utils.misc import subscription
from keyboards.default.boglanish_button import boglanish
import time
check = InlineKeyboardMarkup(row_width=1)

@dp.message_handler(commands=['start'])
@dp.callback_query_handler(text='/start')
async def show_channels(call: types.CallbackQuery):
    try:
        user = await db.add_user(
            telegram_id=call.from_user.id,
            full_name=call.from_user.full_name,
            username=call.from_user.username,
        )
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=call.from_user.id)

    await call.answer('Botga xush kelipsiz',reply_markup=boglanish)
    check = InlineKeyboardMarkup(row_width=1)
    result = str()
    for channel in CHANNELS:
        status = await subscription.check(user_id=call.from_user.id,
                                          channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            result += (f"Assalomu Aleykum {call.from_user.full_name} Botimizga xush kelipsiz")

        else:
            invite_link = await channel.export_invite_link()
            check.insert(InlineKeyboardButton(text=f"🤖{channel.title}", url=invite_link))
            check.insert(InlineKeyboardButton(text="✅Tekshirish",callback_data='check_subs'))
            result += (f"<b>{channel.title}</b> kanaliga obuna bo'lmagansiz. "
                       f"<a href='{invite_link}'>Obuna bo'ling</a>\n\n")

    await call.answer(result, disable_web_page_preview=True, reply_markup=check)




@dp.callback_query_handler(text="check_subs")
async def checker(call: types.CallbackQuery):
    check = InlineKeyboardMarkup(row_width=1)
    await call.answer()
    await call.message.edit_reply_markup()
    await call.message.delete()
    result = str()
    for channel in CHANNELS:
        status = await subscription.check(user_id=call.from_user.id,
                                          channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            result += (f"Assalomu Aleykum {call.from_user.full_name} Botimizga xush kelipsiz")
            check = ''
        else:
            invite_link = await channel.export_invite_link()
            check.insert(InlineKeyboardButton(text=f"🤖{channel.title}",url=invite_link))
            result += (f"<b>{channel.title}</b> kanaliga obuna bo'lmagansiz. "
                       f"<a href='{invite_link}'>Obuna bo'ling</a>\n\n")
            print(channel)
            check.insert(InlineKeyboardButton(text='✅Tekshirish',callback_data='check_subs'))
    await call.message.answer(result, disable_web_page_preview=True,reply_markup=check)

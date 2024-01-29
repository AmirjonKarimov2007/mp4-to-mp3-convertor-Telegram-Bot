import logging
from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from data.config import CHANNELS
from utils.misc import subscription
from loader import bot

check = InlineKeyboardMarkup(row_width=1)
class BigBrother(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, data: dict):
        if update.message:
            message = update.message.from_user.id
            user = update.message.from_user.id
            if update.message.text in ['/start', '/help']:
                return
        elif update.callback_query:
            user = update.callback_query.from_user.id
            if update.callback_query.data == "check_subs":
                return
        else:
            return
        check = InlineKeyboardMarkup(row_width=1)


        result = str()
        final_status = True
        for channel in CHANNELS:
            status = await subscription.check(user_id=user,
                                              channel=channel)
            final_status *= status
            channel = await bot.get_chat(channel)
            if status:
                pass
            else:
                invite_link = await channel.export_invite_link()
                check.insert(InlineKeyboardButton(text=f"🤖{channel.title}", url=invite_link))
                result += (f"<b>{channel.title}</b> kanaliga obuna bo'lmagansiz. "
                           f"<a href='{invite_link}'>Obuna bo'ling</a>\n\n")
            check.insert(InlineKeyboardButton(text='✅Tekshirish', callback_data='check_subs'))

        if not final_status:
            await update.message.answer(result, disable_web_page_preview=True,reply_markup=check)
            raise CancelHandler()
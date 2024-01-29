from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from data.config import CHANNELS

channels = InlineKeyboardMarkup(row_width=2)
tekshirish = (InlineKeyboardButton(text="Tekshirish",callback_data='check_subs'))
channels.insert(tekshirish)
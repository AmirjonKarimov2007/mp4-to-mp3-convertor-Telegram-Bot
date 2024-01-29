from aiogram import types
from aiogram.types import ReplyKeyboardRemove,ReplyKeyboardMarkup,KeyboardButton
from loader import dp

boglanish = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text="📞Bog'lanish")
    ],],
    resize_keyboard=True
)

check = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✅Ha"),
            KeyboardButton(text="❌Yo'q")
        ],
    ],
    resize_keyboard=True
)

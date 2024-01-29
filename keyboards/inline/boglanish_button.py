from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
check = InlineKeyboardMarkup(row_width=2)

check.insert(InlineKeyboardButton(text="✅Ha", callback_data='ha'))
check.insert(InlineKeyboardButton(text="❌Yo'q", callback_data='Yoq'))

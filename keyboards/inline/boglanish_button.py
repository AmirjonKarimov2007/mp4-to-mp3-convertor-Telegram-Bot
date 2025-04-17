from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
check = InlineKeyboardMarkup(row_width=2)

check.insert(InlineKeyboardButton(text="✅Ha", callback_data='ha'))
check.insert(InlineKeyboardButton(text="❌Yo'q", callback_data='Yoq'))

startkeyboard = InlineKeyboardMarkup(row_width=2)
startkeyboard.insert(InlineKeyboardButton(text="✅Fiverr",url='fiverr.com/amirjonkarimov'))
startkeyboard.insert(InlineKeyboardButton(text="🔰Linkedin",url='https://www.linkedin.com/in/amirjon-karimov'))
startkeyboard.insert(InlineKeyboardButton(text="🌐Instagram",url='instagram.com/amirjonkarimov.blog'))
startkeyboard.insert(InlineKeyboardButton(text="📹You tube",url='https://www.youtube.com/@AmirjonKarimovBlog'))
# amirjondeploy@gmail.com
# Karimoff2007@gmail.com
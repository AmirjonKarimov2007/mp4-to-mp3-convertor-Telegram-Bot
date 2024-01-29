import io
from loader import dp, db, bot
from aiogram import types
from data.config import ADMINS
from utils.db_api import db_commands
from aiogram.types import ParseMode
from aiogram.types.web_app_info import WebAppInfo
users = ()
@dp.message_handler(commands=['users'],user_id=ADMINS)
async def send_table(message: types.Message):
    global users  # Declare 'users' as a global variable
    # Fetch data from PostgreSQL database
    users_data = await db.select_all_users()

    # Format the table using Markdown
    if users_data:
        headers = [""]
        rows = [headers] + [
            [str(user.get('id')), user.get('full_name'), str(user.get('username')),
             user.get('telegram_id')] for user in users_data
        ]
        table_text = "\n\n".join([" | ".join(map(str, row)) for row in rows])

        for user in users_data:
            id = user.get('id', 'N/A')
            fullname = user.get('full_name',)
            username = user.get('username')
            telegram_id = user.get('telegram_id')
            formatted_user = f"{id}  | {fullname} | @{username} | {telegram_id}"
            users += (formatted_user,)

        await message.answer(f"`{table_text}`", parse_mode=types.ParseMode.MARKDOWN)

    else:
        await message.answer("No users found in the database.")
@dp.message_handler(commands='reklama',user_id=ADMINS)
async def reklama(message: types.Message):
    users = await db.select_all_users()
    for user in users:
        text = f"Assalomu Aleykum Xurmatli foydalanuvchilar sizlarga bizning yangi telegram botimizni taqdim qilmoqchimiz.\n" \
               f"Umid qilamizki siz u botdan kerakli maqsadlarda foydalanasiz!\n" \
               f"Qo'llab quvvatlash uchun:\n" \
               f"9860070151866938"
        await bot.send_message(user['telegram_id'],text)
@dp.message_handler(commands='remove_user')
async def remove_user(message: types.Message):
    rm_user = await db.delete_user(5816753017)
    await message.answer('foydalanuvchi ochirildi')

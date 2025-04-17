import datetime
from aiogram import types
from aiogram.dispatcher import FSMContext
from filters.admins import IsAdmin,IsSuperAdmin
from keyboards.inline.main_menu_super_admin import main_menu_for_admin
from loader import dp, db

@dp.callback_query_handler(text="stat")
async def stat(call : types.CallbackQuery):
    stat = await db.stat()
    stat = str(stat)
    for x in stat:
        dta = (x)
        datas = datetime.datetime.now()
        yil_oy_kun = (datetime.datetime.date(datetime.datetime.now()))
        soat_minut_sekund = f"{datas.hour}:{datas.minute}:{datas.second}"
        await call.message.delete()
        await call.message.answer(f"<b>👥 Bot foydalanuvchilari soni: {(x)} nafar\n</b>"
                                  f"<b>⏰ Soat: {soat_minut_sekund}\n</b>"
                                  f"<b>📆 Sana: {yil_oy_kun}</b>",reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("◀️ Orqaga",callback_data="backadm")))


@dp.callback_query_handler(IsAdmin(), text="backadm", state="*")
async def back_to_main_menu_method(call: types.CallbackQuery,state: FSMContext):
    await call.answer(cache_time=1)
    await call.message.edit_text(text="Admin paneldasiz", reply_markup=main_menu_for_admin)
    await state.finish()

users = ()
@dp.message_handler(IsSuperAdmin(),commands=['users'])
async def send_table(message: types.Message):
    global users  # Declare 'users' as a global variable
    # Fetch data from PostgreSQL database
    users_data = await db.select_all_users()

    # Format the table using Markdown
    if users_data:
        headers = [""]
        rows = [headers] + [
            [str(user.get('id')), user.get('name'), str(user.get('username')),
             user.get('user_id')] for user in users_data
        ]
        table_text = "\n\n".join([" | ".join(map(str, row)) for row in rows])

        for user in users_data:
            id = user.get('id', 'N/A')
            fullname = user.get('name',)
            username = user.get('username')
            telegram_id = user.get('user_id')
            formatted_user = f"{id}  | {fullname} | @{username} | {telegram_id}"
            users += (formatted_user,)

        await message.answer(f"`{table_text}`", parse_mode=types.ParseMode.MARKDOWN)

    else:
        await message.answer("No users found in the database.")
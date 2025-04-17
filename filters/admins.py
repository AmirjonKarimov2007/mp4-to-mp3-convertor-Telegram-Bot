from aiogram import types

from aiogram.dispatcher.filters import BoundFilter
from data.config import ADMINS
from loader import db

#Dasturchi @Mrgayratov kanla @Kingsofpy
class IsSuperAdmin(BoundFilter):
    async def check(self, message: types.Message):
        user_id = message.from_user.id

        if str(user_id) in ADMINS:
            return True
        else:
            return False
#Dasturchi @Mrgayratov kanla @Kingsofpy
class IsAdmin(BoundFilter):
    async def check(self, message: types.Message):
        user_id = int(message.from_user.id)  # Convert user ID to integer
        admin = await db.is_admin(user_id=user_id)
        if admin:  # Check if admin is not None or False
            return True
        else:
            return False

#Dasturchi @Mrgayratov kanla @Kingsofpy
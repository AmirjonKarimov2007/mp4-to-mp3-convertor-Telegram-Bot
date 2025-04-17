
from loader import db,dp,bot

from aiogram import types

from random import choice
@dp.channel_post_handler(content_types=types.ContentType.ANY)
async def reaction(message: types.Message):
    reactions = ["👍", "❤", "🔥", "🥰", "👏", "🎉"]
    reaction = f'("type": "emoji", "emoji": "{choice(reactions)}")'.replace('(', '{').replace(')', '}')
    await bot.request(
        method="setMessageReaction",
        data={
            "chat_id": message.chat.id,
            "message_id": message.message_id,
            "reaction": f'[{reaction}]'
        }
    )

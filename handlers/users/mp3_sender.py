import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram import executor
from moviepy.editor import VideoFileClip


from loader import dp,bot

@dp.message_handler(content_types=types.ContentType.VIDEO)
async def handle_video(message: types.Message):
    video_file_id = message.video.file_id

    video_file_path = f'{video_file_id}.mp4'
    video_file = await bot.get_file(video_file_id)
    await video_file.download(destination_file=video_file_path)

    audio_file_path = f'{video_file_id}.mp3'
    video_clip = VideoFileClip(video_file_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(audio_file_path)
    audio_clip.close()
    video_clip.close()

    audio_file = types.InputFile(audio_file_path)
    await message.delete()
    text = "<b><a href='t.me/videotoaudiorobot'>📹@VideotoAudiorobot</a> orqali yuklab olindi🚀 📥</b>"
    audio_title = f"{message.from_user.first_name}"

    await bot.send_audio(
        chat_id=message.from_user.id,
        audio=audio_file,
        caption=text,
        title=audio_title
    )
    os.remove(video_file_path)
    os.remove(audio_file_path)
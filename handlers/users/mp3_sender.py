import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram import executor
from moviepy.editor import VideoFileClip

# Replace 'YOUR_BOT_TOKEN' with your actual bot token

from loader import dp,bot

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.reply("Send me a video file, and I will convert it to audio and send it back as an MP3 file.")
@dp.message_handler(content_types=types.ContentType.VIDEO)
async def handle_video(message: types.Message):
    video_file_id = message.video.file_id

    # Download the video file
    video_file_path = f'{video_file_id}.mp4'
    video_file = await bot.get_file(video_file_id)
    await video_file.download(destination_file=video_file_path)

    # Convert video to audio
    audio_file_path = f'{video_file_id}.mp3'
    video_clip = VideoFileClip(video_file_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(audio_file_path)
    audio_clip.close()
    video_clip.close()

    # Send the audio file
    audio_file = types.InputFile(audio_file_path)
    await message.reply_audio(audio=audio_file)

    # Clean up: remove temporary files
    os.remove(video_file_path)
    os.remove(audio_file_path)

# import requests
# from instagrapi import Client
# from loader import bot
# import aiofiles

# # Create a client instance
# async def upload_instagram(file_id,content_type,photo,caption):
#     if content_type== 'photo':
#         photo = photo 
#         file_id = file_id
#         photo_file = await bot.download_file_by_id(file_id)
#         with open(f"{file_id}.jpg", 'wb') as photo_file_local:
#             photo_file_local.write(photo_file.read())
#     cl = Client()

#     caption = caption
#     caption += "\n"
#     username = "amirjonkarimov.blog"
#     password = "Karimoff2007"
#     cl.login(username, password)

#     media = cl.photo_upload(path=f"{file_id}.jpg",caption=caption)
#     cl.logout()
#     # Upload the downloaded image
#     # media = cl.video_upload(path="/home/amirjon/Documents/123.mp4", caption="#hashtag #using #python")




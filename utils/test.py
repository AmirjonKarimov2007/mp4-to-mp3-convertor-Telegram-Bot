from moviepy.editor import *
mp4_file = 'video.mp4'
mp3_file = 'audio.mp3'
videoClip = VideoFileClip(mp4_file)
audoclip = videoClip.audio
audoclip.write_audiofile(mp3_file)
audoclip.close()
videoClip.close()
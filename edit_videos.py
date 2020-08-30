from moviepy.editor import *
import moviepy.video.fx.all as vfx
import os
from datetime import datetime

def edit_video(paths):
    clips=[]
    for i in range(0, len(paths)):
        clip = VideoFileClip(paths[i])
        clip.resize((460, 720))
        clips.append(clip) 
    final = concatenate_videoclips(clips, method='compose')
    today = datetime.now().strftime("%M_%H_%d_%m_%Y")
    save_location = "/tmp/top_clips_" + today + ".mp4"
    final.write_videofile(save_location, temp_audiofile='temp-audio.m4a', remove_temp=True, codec="libx264", audio_codec="aac", fps=24, threads=4)
    print('complete')
    print(save_location)
    return save_location

# edit_video([])
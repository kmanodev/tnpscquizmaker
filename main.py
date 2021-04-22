# importing editor from movie py
from moviepy.editor import *

imagelist=['1.png','1.png','1.png','1.png']
# creating a Image sequence clip with fps = 1
clip = ImageSequenceClip(imagelist, fps = 1)

# showing clip
audioclip = AudioFileClip("a.mp3").subclip(0,len(imagelist))
videoclip = clip.set_audio(audioclip)
videoclip.write_videofile('a.mp4')
print(len(imagelist))
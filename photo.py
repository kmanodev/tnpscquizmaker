from PIL import Image,ImageDraw,ImageFont
from moviepy.editor import *


def createvideo(imagelist):
    imagelist=['1.png','1.png','1.png','1.png']
    # creating a Image sequence clip with fps = 1
    clip = ImageSequenceClip(imagelist, fps = 1)

    # showing clip
    audioclip = AudioFileClip("a.mp3").subclip(0,len(imagelist))
    videoclip = clip.set_audio(audioclip)
    videoclip.write_videofile('a.mp4')
    print('video generated scessfully')





def createimage():
    width=1280
    height=720
    shape = [(10,80), (width - 100, height- 550)]
    shape1= [(10,200), (width - 100, height- 470)]
    shape2= [(10,300), (width - 100, height- 370)]
    shape3= [(10,400), (width - 100, height- 270)]
    shape4= [(10,500), (width - 100, height- 170)]

    fnt=ImageFont.truetype('tamil.ttf',40)
    img=Image.open('input.jpg')
    #img=Image.new(mode='RGB',size=(width,height),color='yellow')
    drawtext=ImageDraw.Draw(img)
    drawtext.rounded_rectangle(shape,fill='#2D76D4',outline='red',radius=50)
    drawtext.text((15,100),'வழிமுறைகளுக்கு இங்கு கிளிக் செய்யவும் ?',font=fnt,fill='white',language='ta-IN')

    drawtext.rounded_rectangle(xy=shape1, radius=50, fill="#2D76D4")
    drawtext.rounded_rectangle(xy=shape2, radius=50, fill="#2D76D4")
    drawtext.rounded_rectangle(xy=shape3, radius=50, fill="#2D76D4")
    drawtext.rounded_rectangle(xy=shape4, radius=50, fill="#2D76D4")
    drawtext.multiline_text((360,200),'இங்கு கிளிக் செய்யவும் ?',font=fnt,fill='#EEE1E1',language='ta-IN')
    drawtext.text((360,300),'இங்கு கிளிக் செய்யவும் ?',font=fnt,fill='#ECE7E7',language='ta-IN')
    drawtext.text((360,400),'இங்கு கிளிக் செய்யவும் ?',font=fnt,fill='#ECE7E7',language='ta-IN')
    drawtext.text((360,500),'\u0ba4\u0bae\u0bbf\u0bb4\u0bcd ?',font=fnt,fill='#ECE7E7',language='ta-IN')


    img.save('1.png')
    img.show()
createimage()
imagelist=['1.png','1.png','1.png']
#createvideo(imagelist)

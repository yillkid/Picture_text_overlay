from PIL import Image, ImageFont, ImageDraw
import shutil
import os

font = ImageFont.truetype("/usr/share/fonts/truetype/arphic/uming.ttc", 25)

def mark_text(img, overlay_text):
    width, height = img.size
    draw = ImageDraw.Draw(img)
    draw.text((width-40,0), overlay_text, (255,0,0), font=font)
    draw = ImageDraw.Draw(img)
    return img

# Clean output
shutil.rmtree('output', ignore_errors=True, onerror=None)
os.mkdir('output')

counter = 1
for filename in sorted(os.listdir('input')):
    img = Image.open('input/' + filename)
    img = mark_text(img, "#" + str(counter))
    img.save("output/" + filename)
    counter = counter + 1

from PIL import Image, ImageDraw, ImageFont
bgcolor=eval(input("enter the rgb color"))
txtcolor=eval(input("enter the text color"))
text=input("enter the text")
img = Image.new('RGB', (420, 420), color =bgcolor)
fnt = ImageFont.truetype('MetalMacabre.ttf', 60) # font-size 1/2 of image W & H
d = ImageDraw.Draw(img)
d.text((20,105), text, font=fnt, fill=txtcolor) # location: 1/6Left, 1/4T
img.save('image.png')
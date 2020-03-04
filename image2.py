from PIL import Image, ImageDraw, ImageFont
bgcolor=eval(input("enter the  rgb color"))
txtcolor=eval(input("enter the text color"))
text=input("enter the text")
img=Image.new("RGB", (420, 420), color=bgcolor)
fnt=Imagefont.truetype("SecretFeeling.ttf", 80)
draw=ImageDraw.Draw(img)
draw.text((10,10(5), text, font=fnt, fill=txtcolor)
img.save("image2.png")
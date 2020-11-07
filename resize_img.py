from PIL import Image
import glob
import os
import sys

lst_imgs = [i for i in glob.glob("*.jpg")]
img_size = sys.argv

if not "resized" in os.listdir():
    os.mkdir("resized")

if len(sys.argv) > 1:
    img_size = int(sys.argv[1])
else:
    img_size = 360

for i in lst_imgs:
    img = Image.open(i)
    w,h = img.size
    min_dim = min(h,w)
    top = int((h - min_dim)/2)
    left = int((w - min_dim)/2)
    img = img.crop((left, top, left+min_dim, top+min_dim)).resize((img_size,img_size), Image.ANTIALIAS)
    img.save("resized\\" + i[:-4] + "_resized.jpg")

print("All Done")
os.startfile("resized")
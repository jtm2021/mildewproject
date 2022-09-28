from PIL import Image
import os, sys

path = os.getcwd() +  "/inputs/mildew_dataset/cherry-leaves/train/powdery_mildew/"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((100,100), Image.ANTIALIAS)
            imResize.save(f + '.JPG', 'JPEG', quality=90)

resize()
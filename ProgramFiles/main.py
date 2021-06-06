import sys
import os
sys.path.append(os.path.abspath("Functions"))

from ImageHandler import IsFilePng
from ImageHandler import ConvertImage

imageName = input("Type png file name: ")
newImageName = input("Type new png file name: ")

pngState = IsFilePng(imageName)

if pngState == True:
    hexString = ConvertImage(imageName)
    
else:
    print("This is not a png file! Try another file.")

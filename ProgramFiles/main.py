import sys
import os
sys.path.append(os.path.abspath("Functions"))

from ImageHandler import IsFilePng
from ImageHandler import ConvertImage
from AnalizeIhdrChunk import AnalizeIhdrChunk
from AnalizePlteChunk import AnalizePlteChunk
from ReadIdatChunk import ReadIdatChunk
from FindIend import FindIend

imageName = input("Type png file name: ")
newImageName = input("Type new png file name: ")

pngState = IsFilePng(imageName)

if pngState == True:
    hexString = ConvertImage(imageName)
    AnalizeIhdrChunk(hexString)
    AnalizePlteChunk(hexString, imageName)
    ReadIdatChunk(hexString, imageName)
    FindIend(hexString)
else:
    print("\nThis is not a png file! Try another file.")

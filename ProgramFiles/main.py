import sys
import os
sys.path.append(os.path.abspath("Functions"))

from ImageHandler import IsFilePng
from ImageHandler import ConvertImage
from ImageHandler import SavePngImage
from ImageHandler import ShowImage
from AnalizeIhdrChunk import AnalizeIhdrChunk
from AnalizePlteChunk import AnalizePlteChunk
from ReadIdatChunk import ReadIdatChunk
from FindIendChunk import FindIendChunk
from FindTimeChunk import FindTimeChunk
from FindGamaChunk import FindGamaChunk
from FindTextChunk import FindTextChunk
from RemoveAncillaryChunks import RemoveAncillaryChunks
from FindExifChunk import findEXIF

imageName = input("Type png file name: ")
newImageName = input("Type new png file name: ")

pngState = IsFilePng(imageName)

if pngState == True:

    hexString = ConvertImage(imageName)
    AnalizeIhdrChunk(hexString)
    AnalizePlteChunk(hexString, imageName)
    ReadIdatChunk(hexString, imageName)
    FindIendChunk(hexString)

    FindTimeChunk(hexString)
    FindGamaChunk(hexString)
    FindTextChunk(hexString)

    hexString = RemoveAncillaryChunks(hexString)
    SavePngImage(hexString, newImageName)
    findEXIF(newImageName)
    ShowImage(newImageName)
else:
    print("\nThis is not a png file! Try another file.")
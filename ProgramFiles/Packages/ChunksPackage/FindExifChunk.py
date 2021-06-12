from PIL import Image
from PIL.ExifTags import TAGS

def FindExifChunk(newImageName):
    filePath = '../NewImages/{}'
    image = Image.open(filePath.format(newImageName))

    print("\n##################################### eXIf CHUNK ######################################\n")

    for tag, value in image.info.items():
        key = TAGS.get(tag, tag)
        print(key + " " + str(value))

    print("\n#######################################################################################")
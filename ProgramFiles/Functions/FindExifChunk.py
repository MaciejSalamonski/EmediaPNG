from PIL import Image
from PIL.ExifTags import TAGS

def findEXIF (newImageName):
    filePath = '../NewImages/{}'
    image = Image.open(filePath.format(newImageName))

    print("\nExif CHUNK: ")

    for tag, value in image.info.items():
        key = TAGS.get(tag, tag)
        print(key + " " + str(value))
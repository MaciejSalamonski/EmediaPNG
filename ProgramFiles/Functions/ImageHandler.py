def IsFilePng(imageName):
    startOfFourBytesPngHeader = 0
    endOfFOurBytesPngHeader = 16
    pngHeader = "89504e470d0a1a0a"
    sampleImagesPath = '../SampleImages/{}'
    readBinaryFlag = 'rb'

    with open(sampleImagesPath.format(imageName), readBinaryFlag) as imageName:
        hexString = imageName.read().hex()
    if hexString[startOfFourBytesPngHeader:endOfFOurBytesPngHeader] == pngHeader:
        return True
    else:
        return False

def ConvertImage(imageName):
    sampleImagesPath = '../SampleImages/{}'
    readBinaryFlag = 'rb'

    with open(sampleImagesPath.format(imageName), readBinaryFlag) as imageName:
        return imageName.read().hex()
import cv2

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

def SavePngImage(hexString: str, newImageName: str):
    writeAndBinaryFlag = 'wb'

    data = bytes.fromhex(hexString)
    filePath = '../NewImages/' + newImageName

    with open(filePath, writeAndBinaryFlag) as newImage:
        newImage.write(data)
    newImage.close()

def ShowImage(imageName):
    filePath = '../NewImages/{}'

    image = cv2.imread(filePath.format(imageName))
    cv2.imshow(filePath.format(imageName), image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
import cv2

def ConvertImage(imageName):
    readBinaryFlag = 'rb'
    sampleImagesPath = '../SampleImages/{}'

    with open(sampleImagesPath.format(imageName), readBinaryFlag) as imageName:
        return imageName.read().hex()

def IsFilePng(imageName):
    endOfFOurBytesPngHeader = 16
    pngHeader = "89504e470d0a1a0a"
    startOfFourBytesPngHeader = 0
    
    hexString = ConvertImage(imageName)

    if hexString[startOfFourBytesPngHeader:endOfFOurBytesPngHeader] == pngHeader:
        return True
    else:
        return False

def SavePngImage(hexString: str, newImageName: str):
    filePath = '../NewImages/' + newImageName
    writeAndBinaryFlag = 'wb'

    data = bytes.fromhex(hexString)

    with open(filePath, writeAndBinaryFlag) as newImage:
        newImage.write(data)
    newImage.close()

def ShowImage(imageName):
    filePath = '../NewImages/{}'

    image = cv2.imread(filePath.format(imageName))
    cv2.imshow(filePath.format(imageName), image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
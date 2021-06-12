from enum import Enum

class ColorType(Enum):
    GREYSCALE = 0
    TRUECOLOR = 2
    INDEXEDCOLOR = 3
    GREYSCALE_WITH_ALPHA = 4
    TRUECOLOR_WITH_ALPHA = 6

class CompressionMethod(Enum):
    DEFLATE_INFLATE = 0

class FilterMethod(Enum):
    NONE = 0
    SUB = 1
    UP = 2
    AVERAGE = 3
    PAETH = 4

class InterlaceMethod(Enum):
    NULL = 0
    ADAM7 = 1

def AnalizeIhdrChunk(hexString):
    IhdrHeader = "49484452"
    posistionOfIhdrChunk = hexString.find(IhdrHeader)

    if posistionOfIhdrChunk != -1:
        fourBytesInHex = 8
        hexBase = 16
        oneByteInHex = 2

        print("\n##################################### IHDR CHUNK ######################################")

        startOfWidthPosition = posistionOfIhdrChunk + fourBytesInHex
        endOfWidthPosition = startOfWidthPosition + fourBytesInHex
        hexWidth = hexString[startOfWidthPosition:endOfWidthPosition]
        decWidth = int(hexWidth, hexBase)

        startOfHeightPosition = endOfWidthPosition
        endOfHeightPosition = startOfHeightPosition + fourBytesInHex
        hexHeight = hexString[startOfHeightPosition:endOfHeightPosition]
        decHeight = int(hexHeight, hexBase)

        startOfBitDepth = endOfHeightPosition
        endOfBitDepth = startOfBitDepth + oneByteInHex
        hexBitDepth = hexString[startOfBitDepth:endOfBitDepth]
        decBitDepth = int(hexBitDepth, hexBase)

        startOfColorType = endOfBitDepth
        endOfColorType = startOfColorType + oneByteInHex
        hexColorType = hexString[startOfColorType:endOfColorType]
        decColorType = int(hexColorType, hexBase)

        startOfCompressionMethod = endOfColorType
        endOfCompressionMethod = startOfCompressionMethod + oneByteInHex
        hexCompressionMethod = hexString[startOfCompressionMethod:endOfCompressionMethod]
        decCompressionMethod = int(hexCompressionMethod, hexBase)

        startOfFilterMethod = endOfCompressionMethod
        endOfFilterMethod = startOfFilterMethod + oneByteInHex
        hexFilterMethod = hexString[startOfFilterMethod:endOfFilterMethod]
        decFilterMethod = int(hexFilterMethod, hexBase)

        startOfInterlaceMethod = endOfFilterMethod
        endOfInterlaceMethod = startOfInterlaceMethod + oneByteInHex
        hexInterlaceMethod = hexString[startOfInterlaceMethod:endOfInterlaceMethod]
        decInterlaceMethod = int(hexInterlaceMethod, hexBase)
    

        dataOutput = "\nWidth: " + str(decWidth)\
                     + "\nHeight: " + str(decHeight)\
                     + "\nBit depth: " + str(decBitDepth)\
                     + "\nColor type: " + str(ColorType(decColorType).name)\
                     + "\nComperssion method: " + str(CompressionMethod(decCompressionMethod).name)\
                     + "\nFilther method: " + str(FilterMethod(decFilterMethod).name)\
                     + "\nInterlace method: " + str(InterlaceMethod(decInterlaceMethod).name)
        print(dataOutput)

        print("\n#######################################################################################\n")
    else:
        print("\n##################################### IHDR CHUNK ######################################")
        print("\nIHDR chunk not found.")
        print("\n#######################################################################################\n")
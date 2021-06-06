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
        oneByteInHex = 2
        fourBytesInHex = 8
        hexBase = 16

        print("\nIHDR CHUNK:\n ")

        startOfWidthPosition = posistionOfIhdrChunk + fourBytesInHex
        endOfWidthPosition = startOfWidthPosition + fourBytesInHex
        hexWidth = hexString[startOfWidthPosition:endOfWidthPosition]
        decWidth = int(hexWidth, hexBase)
        widthOutput = "Width: " + str(decWidth)
        print(widthOutput)

        startOfHeightPosition = endOfWidthPosition
        endOfHeightPosition = startOfHeightPosition + fourBytesInHex
        hexHeight = hexString[startOfHeightPosition:endOfHeightPosition]
        decHeight = int(hexHeight, hexBase)
        heightOutput = "Height: " + str(decHeight)
        print(heightOutput)

        startOfBitDepth = endOfHeightPosition
        endOfBitDepth = startOfBitDepth + oneByteInHex
        hexBitDepth = hexString[startOfBitDepth:endOfBitDepth]
        decBitDepth = int(hexBitDepth, hexBase)
        bitDepthOutput = "Bit depth: " + str(decBitDepth)
        print(bitDepthOutput)

        startOfColorType = endOfBitDepth
        endOfColorType = startOfColorType + oneByteInHex
        hexColorType = hexString[startOfColorType:endOfColorType]
        decColorType = int(hexColorType, hexBase)
        colorTypeOutput = "Color type: " + str(ColorType(decColorType).name)
        print(colorTypeOutput)

        startOfCompressionMethod = endOfColorType
        endOfCompressionMethod = startOfCompressionMethod + oneByteInHex
        hexCompressionMethod = hexString[startOfCompressionMethod:endOfCompressionMethod]
        decCompressionMethod = int(hexCompressionMethod, hexBase)
        compressionMethodOutput = "Comperssion method: " + str(CompressionMethod(decCompressionMethod).name)
        print(compressionMethodOutput)

        startOfFilterMethod = endOfCompressionMethod
        endOfFilterMethod = startOfFilterMethod + oneByteInHex
        hexFilterMethod = hexString[startOfFilterMethod:endOfFilterMethod]
        decFilterMethod = int(hexFilterMethod, hexBase)
        filterMethodOutput = "Filther method: " + str(FilterMethod(decFilterMethod).name)
        print(filterMethodOutput)

        startOfInterlaceMethod = endOfFilterMethod
        endOfInterlaceMethod = startOfInterlaceMethod + oneByteInHex
        hexInterlaceMethod = hexString[startOfInterlaceMethod:endOfInterlaceMethod]
        decInterlaceMethod = int(hexInterlaceMethod, hexBase)
        interlaceMethodOutput = "Interlace method: " + str(InterlaceMethod(decInterlaceMethod).name)
        print(interlaceMethodOutput)
    
    else:
        print("\nIHDR chunk not found.")
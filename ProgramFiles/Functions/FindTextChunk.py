import codecs

def FindTextChunk(hexString):
    textHeader = "74455874"
    positionOfTextChunk = hexString.find(textHeader)

    if positionOfTextChunk != -1:
        fourBytesInHex = 8
        hexBase = 16
        hexFlag = 'hex'
        decodeFlag = 'utf-8'

        print("\ntEXt CHUNK:\n ")

        startOfTextDataLength = positionOfTextChunk - fourBytesInHex
        endOfTextDataLength = positionOfTextChunk
        hexTextDataLength = hexString[startOfTextDataLength:endOfTextDataLength]
        decTextDataLength = int(hexTextDataLength, hexBase)

        startOfTextData = positionOfTextChunk + fourBytesInHex
        endOfTextData = startOfTextData + decTextDataLength * 2
        textData = codecs.decode(hexString[startOfTextData:endOfTextData], hexFlag).decode(decodeFlag)
        dataOutput = "tEXt data: " + str(textData)
        print(dataOutput)
    else:
        print("\ntEXt chunk not found.")
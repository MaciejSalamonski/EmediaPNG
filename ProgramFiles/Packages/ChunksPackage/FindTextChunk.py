import codecs

def FindTextChunk(hexString):
    textHeader = "74455874"
    positionOfTextChunk = hexString.find(textHeader)

    if positionOfTextChunk != -1:
        decodeFlag = 'utf-8'
        fourBytesInHex = 8
        hexBase = 16
        hexFlag = 'hex'
        twoCharactersInHex = 2

        print("\n##################################### tEXt CHUNK ######################################")

        startOfTextDataLength = positionOfTextChunk - fourBytesInHex
        endOfTextDataLength = positionOfTextChunk
        hexTextDataLength = hexString[startOfTextDataLength:endOfTextDataLength]
        decTextDataLength = int(hexTextDataLength, hexBase)

        startOfTextData = positionOfTextChunk + fourBytesInHex
        endOfTextData = startOfTextData + decTextDataLength * twoCharactersInHex
        textData = codecs.decode(hexString[startOfTextData:endOfTextData], hexFlag).decode(decodeFlag)
        dataOutput = "\ntEXt data: " + str(textData)
        print(dataOutput)
        print("\n#######################################################################################\n")
    else:
        print("\n##################################### tEXt CHUNK ######################################")
        print("\ntEXt chunk not found.")
        print("\n#######################################################################################\n")
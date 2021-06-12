def AnalizePlteChunk(hexString, imageName):
    PlteHeader = "504c5445"
    positionOfPlteChunk = hexString.find(PlteHeader)

    if positionOfPlteChunk != -1:
        fourBytesInHex = 8
        hexBase = 16
        plteChunkDataPath = '../ChunksData/plteData.txt'
        writeFlag = 'w'
        paleteEntryCounter = 0
        chunkDivisiedByThree = 3
        oneByteInHex = 2

        print("\nPLTE CHUNK:\n ")

        startOfPlteDataLength = positionOfPlteChunk - fourBytesInHex
        endOfPlteDataLength = positionOfPlteChunk
        hexPlteChunkLength = hexString[startOfPlteDataLength:endOfPlteDataLength]
        decPlteChunkLength = int(hexPlteChunkLength, hexBase)

        plteChunkDataFile = open(plteChunkDataPath, writeFlag)
        writeData = str(imageName) + " PLTE chunk data:\n"
        plteChunkDataFile.write(writeData) 

        colorsPosition = positionOfPlteChunk + fourBytesInHex
        while paleteEntryCounter < (decPlteChunkLength / chunkDivisiedByThree):
            hexRed = hexString[colorsPosition:(colorsPosition + oneByteInHex)]
            decRed = int(hexRed, hexBase)
            colorsPosition += oneByteInHex

            hexGreen = hexString[colorsPosition:(colorsPosition + oneByteInHex)]
            decGreen = int(hexGreen, hexBase)
            colorsPosition += oneByteInHex

            hexBlue = hexString[colorsPosition:(colorsPosition + oneByteInHex)]
            decBlue = int(hexBlue, hexBase)
            colorsPosition += oneByteInHex

            writeData = "Palete entry "\
                        + str(paleteEntryCounter)\
                        + " RED: "\
                        + str(decRed)\
                        + " GREEN: "\
                        + str(decGreen)\
                        + " BLUE: "\
                        + str(decBlue)
            plteChunkDataFile.write(writeData + '\n')
            paleteEntryCounter += 1

        plteChunkDataFile.close()
        print("Entires saved in ChunksData directory - file plteData.txt\n")
    else:
        print("\nPLTE chunk not found.")
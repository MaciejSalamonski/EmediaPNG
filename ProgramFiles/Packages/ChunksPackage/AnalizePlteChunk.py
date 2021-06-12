def AnalizePlteChunk(hexString, imageName):
    plteHeader = "504c5445"
    positionOfPlteChunk = hexString.find(plteHeader)

    if positionOfPlteChunk != -1:
        chunkDivisiedByThree = 3
        fourBytesInHex = 8
        hexBase = 16
        oneByteInHex = 2
        paleteEntryCounter = 0
        plteChunkDataPath = '../ChunksData/plteData.txt'
        writeFlag = 'w'

        print("\n##################################### PLTE CHUNK ######################################")

        startOfPlteDataLength = positionOfPlteChunk - fourBytesInHex
        endOfPlteDataLength = positionOfPlteChunk
        hexPlteChunkLength = hexString[startOfPlteDataLength:endOfPlteDataLength]
        decPlteChunkLength = int(hexPlteChunkLength, hexBase)

        plteChunkDataFile = open(plteChunkDataPath, writeFlag)
        writeData = str(imageName) + "PLTE chunk data:\n"
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
        print("\nPLTE data saved in ChunksData directory - file plteData.txt")
        print("\n#######################################################################################\n")
    else:
        print("\n##################################### PLTE CHUNK ######################################")
        print("\nPLTE chunk not found.")
        print("\n#######################################################################################\n")
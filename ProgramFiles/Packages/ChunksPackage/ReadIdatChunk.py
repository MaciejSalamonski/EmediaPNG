def ReadIdatChunk(hexString, imageName):
    idatHeader = "49444154"
    positionOfIdatChunk = hexString.find(idatHeader)

    if positionOfIdatChunk != -1:
        currentIdatDataLength = 0
        fourBytesInHex = 8
        hexBase = 16
        idatChunkDataPath = '../ChunksData/idatData.txt'
        oneByteInHex = 2
        writeFlag = 'w'

        print("\n##################################### IDAT CHUNK ######################################")

        startOfIdatDataLength = positionOfIdatChunk - fourBytesInHex
        endOfIdatDataLength = positionOfIdatChunk 
        hexIdatChunkLength = hexString[startOfIdatDataLength:endOfIdatDataLength]
        decIdatChunkLength = int(hexIdatChunkLength, hexBase)

        idatChunkDataFile = open(idatChunkDataPath, writeFlag)
        writeData = str(imageName) + " IDAT chunk data:\n"
        idatChunkDataFile.write(writeData)

        startOfIdatData = positionOfIdatChunk + fourBytesInHex
        while currentIdatDataLength < decIdatChunkLength:
            hexData = hexString[startOfIdatDataLength:(startOfIdatDataLength + oneByteInHex)]
            startOfIdatDataLength += oneByteInHex

            writeData = str(hexData) + " "
            idatChunkDataFile.write(writeData)

            currentIdatDataLength += 1
        
        idatChunkDataFile.close()
        print("\nIDAT data saved in ChunksData directory - file idatData.txt")
        print("\n#######################################################################################\n")
    else:
        print("\n##################################### IDAT CHUNK ######################################")
        print("\nIDAT chunk not found.")
        print("\n#######################################################################################\n")
def ReadIdatChunk(hexString, imageName):
    idatHeader = "49444154"
    positionOfIdatChunk = hexString.find(idatHeader)

    if positionOfIdatChunk != -1:
        fourBytesInHex = 8
        oneByteInHex = 2
        hexBase = 16
        idatChunkDataPath = '../ChunksData/idatData.txt'
        writeFlag = 'w'
        currentIdatDataLength = 0

        print("IDAT CHUNK:\n ")

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
        print("IDAT data saved in ChunksData directory - file idatData.txt\n")
    
    else:
        print("\nIDAT chunk not found.")
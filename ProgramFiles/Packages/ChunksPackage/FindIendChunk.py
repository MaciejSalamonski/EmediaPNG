def FindIendChunk(hexString):
    iendHeader = "49454e44"
    positionOfIendChunk = hexString.find(iendHeader)

    if positionOfIendChunk != -1:
        fourBytesInHex = 8
        hexBase = 16

        print("IEND CHUNK:\n ")

        startOfIendDataLength = positionOfIendChunk - fourBytesInHex
        endOfIendDataLength = positionOfIendChunk 
        hexIendChunkLength = hexString[startOfIendDataLength:endOfIendDataLength]
        decIendChunkLength = int(hexIendChunkLength, hexBase)
        iendChunkLengthOutput = "Iend chunk length: "\
                                + str(decIendChunkLength)\
                                + '\n'
        print(iendChunkLengthOutput)
    else:
        print("\nIEND chunk not found.")
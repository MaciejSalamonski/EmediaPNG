def FindIend(hexString):
    iendHeader = "49454e44"
    positionOfIendHeader = hexString.find(iendHeader)

    if positionOfIendHeader != -1:
        fourBytesInHex = 8
        hexBase = 16

        print("IEND CHUNK:\n ")

        startOfIendDataLength = positionOfIendHeader - fourBytesInHex
        endOfIendDataLength = positionOfIendHeader 
        hexIendChunkLength = hexString[startOfIendDataLength:endOfIendDataLength]
        decIendChunkLength = int(hexIendChunkLength, hexBase)
        iendChunkLengthOutput = "Iend chunk length: "\
                                + str(decIendChunkLength)\
                                + '\n'
        print(iendChunkLengthOutput)
    else:
        print("\nIEND chunk not found.")
def FindIendChunk(hexString):
    iendHeader = "49454e44"
    positionOfIendChunk = hexString.find(iendHeader)

    if positionOfIendChunk != -1:
        fourBytesInHex = 8
        hexBase = 16

        print("\n##################################### IEND CHUNK ######################################")

        startOfIendDataLength = positionOfIendChunk - fourBytesInHex
        endOfIendDataLength = positionOfIendChunk 
        hexIendChunkLength = hexString[startOfIendDataLength:endOfIendDataLength]
        decIendChunkLength = int(hexIendChunkLength, hexBase)
        iendChunkLengthOutput = "\nIEND chunk length: "\
                                + str(decIendChunkLength)
        print(iendChunkLengthOutput)
        print("\n#######################################################################################\n")
    else:
        print("\n##################################### IEND CHUNK ######################################")
        print("\nIEND chunk not found.")
        print("\n#######################################################################################\n")
def FindGamaChunk(hexString):
    gamaHeader = "67414d41"
    positionOfGamaChunk = hexString.find(gamaHeader)

    if positionOfGamaChunk != -1:
        fourBytesInHex = 8
        hexBase = 16

        print("\ngAMA CHUNK: ")

        startOfGamaData = positionOfGamaChunk + fourBytesInHex
        endOfGamaData = startOfGamaData + fourBytesInHex
        hexGama = hexString[startOfGamaData:endOfGamaData]
        decGama = int(hexGama, hexBase)

        dataOutput = "\nImage gama: " + str(decGama)
        print(dataOutput)
    else:
        print("\ngAMA chunk not found.")
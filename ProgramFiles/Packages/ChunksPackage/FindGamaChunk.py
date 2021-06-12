def FindGamaChunk(hexString):
    gamaHeader = "67414d41"
    positionOfGamaChunk = hexString.find(gamaHeader)

    if positionOfGamaChunk != -1:
        fourBytesInHex = 8
        hexBase = 16

        print("\n##################################### gAMA CHUNK ######################################")

        startOfGamaData = positionOfGamaChunk + fourBytesInHex
        endOfGamaData = startOfGamaData + fourBytesInHex
        hexGama = hexString[startOfGamaData:endOfGamaData]
        decGama = int(hexGama, hexBase)

        dataOutput = "\nImage gAMA: " + str(decGama)
        print(dataOutput)
        print("\n#######################################################################################\n")
    else:
        print("\n##################################### gAMA CHUNK ######################################")
        print("\ngAMA chunk not found.")
        print("\n#######################################################################################\n")
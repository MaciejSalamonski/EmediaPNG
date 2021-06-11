def RemoveAncillaryChunks(hexString: str):
    constChunkLengthInBytes = 12
    fourBytesInHex = 8
    hexBase = 16
    startPosition = 0
    twoCharsForOneByteInHexString = 2

    bkgdHeader = "624b4744"
    chrmHeader = "6348524d"
    dsigHeader = "64534947"
    exifHeader = "65584966"
    gamaHeader = "67414d41"
    histHeader = "68495354"
    iccpHeader = "69434350"
    itxtHeader = "69545874"
    physHeader = "70485973"
    sbitHeader = "73424954"
    spltHeader = "73504c54"
    srgbHeader = "73524742"
    sterHeader = "73544552"
    textHeader = "74455874"
    timeHeader = "74494d45"
    trnsHeader = "74524e53"
    ztxtHeader = "7a545874"

    constChunkLength = constChunkLengthInBytes * twoCharsForOneByteInHexString
    chunksHeaders = [bkgdHeader, chrmHeader, dsigHeader, exifHeader, gamaHeader,
                     histHeader, iccpHeader, itxtHeader, physHeader, sbitHeader,
                     spltHeader, srgbHeader, sterHeader, textHeader, timeHeader,
                     trnsHeader, ztxtHeader]

    for chunkHeader in chunksHeaders:
        positionOfAncillaryChunk = hexString.find(chunkHeader)

        if positionOfAncillaryChunk != -1:
            startOfChunkDataLength = positionOfAncillaryChunk - fourBytesInHex
            endOfChunkDataLength = positionOfAncillaryChunk
            hexChunkDataLength = hexString[startOfChunkDataLength:endOfChunkDataLength]
            decChunkDataLength = int(hexChunkDataLength, hexBase)
            chunkDataLength = decChunkDataLength * twoCharsForoneByteInHexString
            hexStringFirstPart = hexString[startPosition:startOfChunkDataLength]
            hexStringSecondPart = hexString[(startOfChunkDataLength \
                                             + chunkDataLength \
                                             + constChunkLength):]
            hexString = hexStringFirstPart + hexStringSecondPart

    return hexString
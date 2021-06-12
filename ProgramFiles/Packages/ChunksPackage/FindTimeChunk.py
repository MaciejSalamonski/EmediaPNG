def FindTimeChunk(hexString):
    timeHeader = "74494d45"
    positionOfTimeChunk = hexString.find(timeHeader)

    if positionOfTimeChunk != -1:
        fourBytesInHex = 8
        hexBase = 16
        oneByteInHex = 2
        twoBytesInHex = 4

        print("\n##################################### tIME CHUNK ######################################")

        startOfYearData = positionOfTimeChunk + fourBytesInHex
        endOfYearData = startOfYearData + twoBytesInHex
        hexYear = hexString[startOfYearData:endOfYearData]
        decYear = int(hexYear, hexBase)

        startOfMonthData = endOfYearData
        endOfMonthData = startOfMonthData + oneByteInHex
        hexMonth = hexString[startOfMonthData:endOfMonthData]
        decMonth = int(hexMonth, hexBase)

        startOfDayData = endOfMonthData
        endOfDayData = startOfDayData + oneByteInHex
        hexDay = hexString[startOfDayData:endOfDayData]
        decDay = int(hexDay, hexBase)

        startOfHourData = endOfDayData
        endOfHourData = startOfHourData + oneByteInHex
        hexHour = hexString[startOfHourData:endOfHourData]
        decHour = int(hexHour, hexBase)

        startOfMinuteData = endOfHourData
        endOfMinuteData = startOfMinuteData + oneByteInHex
        hexMinute = hexString[startOfMinuteData:endOfMinuteData]
        decMinute = int(hexMinute, hexBase)

        startOfSecondData = endOfMinuteData
        endOfSecondData = startOfSecondData + oneByteInHex
        hexSecond = hexString[startOfSecondData:endOfSecondData]
        decSecond = int(hexSecond, hexBase)

        dataOutput = "\nYear: " + str(decYear)\
                     + "\nMonth: " + str(decMonth)\
                     + "\nDay: " + str(decDay)\
                     + "\nHour:" + str(decHour)\
                     + "\nMinute: " + str(decMinute)\
                     + "\nSecond: " + str(decSecond)
        print(dataOutput)
        print("\n#######################################################################################\n")
    else:
        print("\n##################################### tIME CHUNK ######################################")
        print("\ntIME chunk not found.")
        print("\n#######################################################################################\n")
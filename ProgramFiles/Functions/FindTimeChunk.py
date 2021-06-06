def FindTimeChunk(hexString):
    timeHeader = "74494d45"
    positionOfTimeHeader = hexString.find(timeHeader)

    if positionOfTimeHeader != -1:
        fourBytesInHex = 8
        twoBytesInHex = 4
        oneByteInHex = 2
        hexBase = 16

        print("tIME CHUNK:\n ")

        startOfYearData = positionOfTimeHeader + fourBytesInHex
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

        dataOutput = "Year: " + str(decYear)\
                     + "\nMonth: " + str(decMonth)\
                     + "\nDay: " + str(decDay)\
                     + "\nHour:" + str(decHour)\
                     + "\nMinute: " + str(decMinute)\
                     + "\nSecond: " + str(decSecond)
        print(dataOutput)

    else:
        print("\ntIME chunk not found.")
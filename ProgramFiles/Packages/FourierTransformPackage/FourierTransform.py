import cv2
import numpy
from ImageHandler import ShowImage

def FourierTransform(imageName):
    filePath = '../NewImages/{}'
    logarithmConstant = 20
    oneRow = 1

    image = cv2.imread(filePath.format(imageName), cv2.IMREAD_GRAYSCALE)

    discreteFourierTransform = numpy.fft.fft2(image)
    shiftedZeroFrequencyComponentToSpectrumCenter = numpy.fft.fftshift(discreteFourierTransform)
    
    magnitudeSpectrum = logarithmConstant * numpy.log(numpy.abs(shiftedZeroFrequencyComponentToSpectrumCenter))
    phaseSpectrum = numpy.angle(shiftedZeroFrequencyComponentToSpectrumCenter)

    magnitudeSpectrumArray = numpy.asarray(magnitudeSpectrum, dtype = numpy.uint8)
    imageAndMagnitudeSpectrum = numpy.concatenate((image, magnitudeSpectrumArray), axis = oneRow)

    phaseSpectrumArray = numpy.asarray(phaseSpectrum, dtype = numpy.uint8)
    imageAndPhaseSpectrum = numpy.concatenate((image, phaseSpectrumArray), axis = oneRow)

    cv2.namedWindow("Magnitude spectrum")
    cv2.imshow("Magnitude spectrum", imageAndMagnitudeSpectrum)

    cv2.namedWindow("Phase spectrum")
    cv2.imshow("Phase spectrum", imageAndPhaseSpectrum)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
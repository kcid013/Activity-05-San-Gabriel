import cv2 as cv
import numpy as np
import process as pr

img = cv.imread("cat.jpg")

print("""
[1] - check if grayscale
[2] - show pixel value
[3] - modify a pixel value
[4] - set image dimension
[5] - set image total pixel count
[6] - show image data type""")

opt = int(input("select: "))

if opt == 1:
    imageLen = len(img.shape)
    pr.processClass.checkGrayscale(imageLen)
    cv.imshow("test", img)
    cv.waitKey(0)

elif opt == 2:
    pr.processClass.showPixelValue(img)

elif opt == 3:
    pr.processClass.modifyPixelValue(img)

elif opt == 4:
    pr.processClass.dimension(img)

elif opt == 5:
    pr.processClass.pixelCount(img)

elif opt == 6:
    pr.processClass.imgDataType(img)
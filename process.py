import cv2 as cv
import numpy as np


class processClass():
    def checkGrayscale(imageLen):
        if imageLen == 2:
            print("Image is grayscaled")
            exit(0)

    def showPixelValue(img):
        x = int(input("value of x-axis: "))
        y = int(input("value of y-axis: "))
        color = int(input("[0] - blue, [1] - green, [2] - red: "))
        print(img.item(x, y, color))

    def modifyPixelValue(img):
        x = int(input("value of x-axis: "))
        y = int(input("value of y-axis: "))
        print(img[x, y])
        for i in range(0, 3, 1):
            color = int(input("[0] - blue, [1] - green, [2] - red: "))
            value = int(input("value: "))
            img.itemset((x, y, color), value)
        print(img[x, y])
        cv.imshow("test", img)
        cv.waitKey(0)

    def dimension(img):
        x = 500
        y = 100
        print(img.shape)
        print(f"""
            total image pixel in x-axis: {img.shape[0]}
            total image pixel in y-axis: {img.shape[1]}
            compared value in x-axis: {x}
            compared value in y-axis: {y}
            """)

        if x <= img.shape[0] and y <= img.shape[1]:
            print("value is on the boundaries")
        else:
            print("value is out of the boundaries")

    def pixelCount(img):
        x = 100
        y = 100
        fixedValue = x * y
        totalNumberOfPixel = img.shape[0] * img.shape[1]

        print(f"""
           total fixed variable: {fixedValue}
           total image pixels: {totalNumberOfPixel}""")

        if fixedValue > totalNumberOfPixel:
            print("higher")
        elif fixedValue < totalNumberOfPixel:
            print("lower")
        else:
            print("equal")

    def imgDataType(img):
        print(img.dtype)
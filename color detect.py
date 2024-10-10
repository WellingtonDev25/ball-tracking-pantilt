import cv2
from cvzone.ColorModule import ColorFinder

img = cv2.imread('img.jpg')
colorFinder = ColorFinder(True)

while True:
    imgColor,mask = colorFinder.update(img)

    cv2.imshow('IMG',imgColor)
    if cv2.waitKey(1)==27:
        break




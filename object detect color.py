import cv2
import cvzone
from cvzone.ColorModule import ColorFinder
import numpy as np

video = cv2.VideoCapture(0)

myColorFinder = ColorFinder(False)
# hsvValues = {'hmin': 0, 'smin': 10, 'vmin': 255, 'hmax': 59, 'smax': 255, 'vmax': 255}
hsvValues = {'hmin': 3, 'smin': 25, 'vmin': 211, 'hmax': 26, 'smax': 255, 'vmax': 255}

while True:
    _,img = video.read()
    imgColor,mask = myColorFinder.update(img,hsvValues)
    imgContour, contours = cvzone.findContours(img,mask,minArea=500)
    if contours:
        cx,cy = contours[0]['center']
        x,y,w,h = contours[0]['bbox']
        cv2.circle(img,(cx,cy),5,(0,255,0),-1)
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),5)


    cv2.imshow('Video', img)
    if cv2.waitKey(1)==27:
        break
import cv2
import cvzone
from cvzone.ColorModule import ColorFinder

video = cv2.VideoCapture(1)

myColorFinder = ColorFinder(False)
hsvValues = {'hmin': 5, 'smin': 47, 'vmin': 247, 'hmax': 17, 'smax': 202, 'vmax': 255}

while True:
    _,img = video.read()
    imgColor,mask = myColorFinder.update(img,hsvValues)
    imgContour, contours = cvzone.findContours(img,mask,minArea=700)
    if contours:
        cx,cy = contours[0]['center']
        x,y,w,h = contours[0]['bbox']
        cv2.circle(img,(cx,cy),5,(0,255,0),-1)
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),5)

    cv2.imshow('Video', img)
    if cv2.waitKey(1)==27:
        break
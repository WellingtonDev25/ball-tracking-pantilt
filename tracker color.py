import cv2
from pyfirmata import Arduino,SERVO
from time import sleep
from cvzone.ColorModule import ColorFinder
import cvzone

port = 'COM7'
pinH = 8
pinV = 7
board = Arduino(port)

board.digital[pinH].mode = SERVO
board.digital[pinV].mode = SERVO

myColorFinder = ColorFinder(False)
hsvValues = {'hmin': 0, 'smin': 10, 'vmin': 255, 'hmax': 59, 'smax': 255, 'vmax': 255}

def rotateServo(pin,angle):
    board.digital[pin].write(angle)
    sleep(0.015)

video = cv2.VideoCapture(1)

quadroCentro = 70

positionX = 50
positionY = 70

rotateServo(pinH, positionX)
rotateServo(pinV, positionY)

while True:
    _,img = video.read()
    imgShow = img.copy()

    hVideo, wVideo, _ = img.shape
    cv2.line(imgShow, (0, int(hVideo / 2)), (wVideo, int(hVideo / 2)), (0, 255, 0), 2)
    cv2.line(imgShow, (int(wVideo / 2), 0), (int(wVideo / 2), hVideo), (0, 255, 0), 2)

    imgColor,mask = myColorFinder.update(img,hsvValues)
    imgContour, contours = cvzone.findContours(img,mask,minArea=800)

    if contours:
        cx,cy = contours[0]['center']
        x,y,w,h = contours[0]['bbox']
        cv2.circle(imgShow,(cx,cy),5,(0,255,0),-1)
        cv2.rectangle(imgShow,(x,y),(x+w,y+h),(255,0,255),5)

        ctX = int(wVideo / 2)
        ctY = int(hVideo / 2)

        cv2.rectangle(imgShow, (ctX-70, ctY-70), (ctX + 70, ctY + 70), (255, 0, 255), 5)

        ##movimento eixo X
        if cx < (ctX-quadroCentro):
            positionX +=1
            if positionX <= 180 and positionX >= 1:
                rotateServo(pinH, positionX)
        elif cx > (ctX+quadroCentro):
            positionX -=1
            if positionX <= 180 and positionX >= 1:
                rotateServo(pinH, positionX)

        #movimento eixo Y
        if cy > (ctY+quadroCentro):
            positionY +=1
            if positionY <=180 and positionY>=1:
                rotateServo(pinV, positionY)
        elif cy < (ctY-quadroCentro):
            positionY -=1
            if positionY <= 180 and positionY >= 1:
                rotateServo(pinV, positionY)

    cv2.imshow('img', imgShow)

    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break




import cv2

video = cv2.VideoCapture(1)
id = 0

while True:
    check,img = video.read()

    cv2.imshow('Img',img)
    if cv2.waitKey(20) & 0xFF == ord('s'):
        cv2.imwrite(f'img.jpg',img)
        id+=1

    if cv2.waitKey(1) ==27:
        break

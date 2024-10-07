import cv2
from scipy import ndimage

video = cv2.VideoCapture(0)
id = 0
while True:
    check,img = video.read()
    # rotated = ndimage.rotate(img, 90)

    cv2.imshow('Img',img)
    if cv2.waitKey(20) & 0xFF == ord('s'):
        cv2.imwrite(f'Imagens/img{id}.jpg',img)
        id+=1

    if cv2.waitKey(1) ==27:
        break

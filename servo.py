from pyfirmata import Arduino,SERVO
import time

board = Arduino('COM7')
pin = 7
board.digital[pin].mode = SERVO

def rotateServo(angle):
    board.digital[pin].write(angle)
    time.sleep(0.015)

while True:
    x = input('digite o ângulo')
    rotateServo(int(x))


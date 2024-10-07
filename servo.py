from pyfirmata import Arduino,SERVO
import time

board = Arduino('COM3')
pin = 8
board.digital[pin].mode = SERVO

def rotateServo(angle):
    board.digital[pin].write(angle)
    time.sleep(0.015)

while True:
    x = input('digite o ângulo')
    rotateServo(int(x))

# while True:
#     for x in range(0,180):
#         rotateServo(x)
#     for x in range(180,0,-1):
#         rotateServo(x)
from gpiozero import Motor
from time import sleep

rightwheel_front = Motor(25, 16)
rightwheel_back = Motor(20, 21)
leftwheel_front = Motor(5, 6)
leftwheel_back = Motor(19, 26)

try:
    while True:
        leftwheel_front.forward(speed=1)
        leftwheel_back.forward(speed=1)
        rightwheel_front.forward(speed=1)
        rightwheel_back.forward(speed=1)
        sleep(3)
        
        leftwheel_front.backward(speed=0.5)
        leftwheel_back.backward(speed=0.5)
        rightwheel_front.backward(speed=0.5)
        rightwheel_back.backward(speed=0.5)
        sleep(3)

except KeyboardInterrupt:
    print("stop")
finally:
    leftwheel_front.stop()
    leftwheel_back.stop()
    rightwheel_front.stop()
    rightwheel_back.stop()

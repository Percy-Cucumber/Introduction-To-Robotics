# Import Libraries
from ev3dev.auto import *
import time


# Define Motors & Sensors
leftmotor = LargeMotor(OUTPUT_D)
rightmotor = LargeMotor(OUTPUT_A)

btn = Button()

us = UltrasonicSensor(INPUT_3)
us.mode = 'US-DIST-CM'

ls = Sensor(INPUT_2)
ls.mode = 'CAL'

cs1 = ColorSensor(INPUT_4)
cs1.mode = 'COL-REFLECT'

cs2 = ColorSensor(INPUT_1)
cs2.mode = 'COL-REFLECT'


# Declare Variables
basespeed = 1000
turnSpeed = 1000
ultrasonicthreshold = 1

olderror = 0
oldtime = time.time()
integral = 0

KP = 2
KD = 0
KI = 1


# Program
# Sound.play('sounds/take-on-me.wav')

while btn.any() ==False:                                                                # beginning of the loop for the whole program
    print('LightSensor', ls.value(0), ls.value(1), ls.value(2), ls.value(3), ls.value(4), ls.value(5), ls.value(6), ls.value(7))
    time.sleep(.5)
    print('ColorSensor', cs1.value(0), cs2.value(0))
    print('UltraSonic', us.value(0))

    error = ((ls.value(0) + ls.value(1) + ls.value(2) + ls.value(3)) / 4) - ((ls.value(4) + ls.value(5) + ls.value(6) + ls.value(7)) / 4)
    dt = time.time() - oldtime
    changeerror = (error - olderror) / dt
    integral = integral + error * dt
    olderror = error
    oldtime = time.time()

    leftspeed = basespeed + KP * error + KD * changeerror + KI * integral
    rightspeed = basespeed - KP * error - KD * changeerror - KI * integral

    if leftspeed > 1000:
        leftspeed = 1000
    if leftspeed < -1000:
        leftspeed = -1000
    if rightspeed > 1000:
        rightspeed = 1000
    if rightspeed < -1000:
        rightspeed = -1000

    leftmotor.run_forever(speed_sp=leftspeed)
    rightmotor.run_forever(speed_sp=rightspeed)


# End Sequence
leftmotor.stop(stop_action='brake')
rightmotor.stop(stop_action='brake')

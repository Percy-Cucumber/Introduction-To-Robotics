# Import Libraries
from ev3dev.auto import *
import time


#Define Stuff
leftmotor = LargeMotor(OUTPUT_A)
rightmotor = LargeMotor(OUTPUT_D)
btn = Button()

ls = Sensor(INPUT_4)
ls.mode = 'CAL'

gyro = GyroSensor(INPUT_1)
gyro.mode = 'GYRO-RATE'
time.sleep(0.5)
gyro.mode = 'GYRO-ANG'

oldvalue = 0
oldtime = time.time()
integral = 0
basespeed = 500
KP = 10
KD = 1
KI = 1ot@192.168.1.112


#Program
Sound.play('sounds/champions.wav')

while btn.any() == False:
    error = gyro.value()-0
    dt = time.time()-oldtime

    changeerror = (gyro.value()-oldvalue)/(dt)
    integral = integral + error*dt

    oldvalue = gyro.value()
    oldtime = time.time()

    print('Error:', error, 'deg', 'Integral:', integral, 'deg s', 'Rate:', changeerror, 'deg/s')

    leftspeed = basespeed - KP*error - KD*changeerror - KI*integral
    rightspeed = basespeed + KP*error + KD*changeerror + KI*integral

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

leftmotor.stop(stop_action='brake')
rightmotor.stop(stop_action='brake')
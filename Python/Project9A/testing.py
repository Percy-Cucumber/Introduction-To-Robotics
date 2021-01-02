#Import Libraries
from ev3dev.auto import *
import time


#Declare Motors
lm = LargeMotor(OUTPUT_A)
rm = LargeMotor(OUTPUT_D)


#Declare Object
btn = Button()


#Declare Sensors
gyro = GyroSensor(INPUT_1)
gyro.mode = 'GYRO-RATE'
time.sleep(0.5)
gyro.mode = 'GYRO-ANG'


#Functions
def ds(bs,dh,kp,drr):
    st = time.time()
    while time.time() - st < drr:
        error = gyro.value() - dh
        lp = bs - kp * error
        rp = bs + kp * error

        if lp > 1000:
            lp = 1000
        if lp < -1000:
            lp = -1000
        if rp > 1000:
            rp = 1000
        if rp < -1000:
            rp = -1000

        lm.run_forever(speed_sp=lp)
        rm.run_forever(speed_sp=rp)
        print(gyro.value(), lp, rp)

    Sound.beep().wait()
    lm.stop(stop_action='brake')
    rm.stop(stop_action='brake')

def turn(sp,deg,KP,tim):
    error = gyro.value() - dh
    lp = bs - kp * error
    rp = bs + kp * error

    if lp > 1000:
        lp = 1000
    if lp < -1000:
        lp = -1000
    if rp > 1000:
        rp = 1000
    if rp < -1000:
        rp = -1000

    lm.run_forever(speed_sp=lp)
    rm.run_forever(speed_sp=rp)
    print(gyro.value(), lp, rp)


#Program
print('START')

for i in range (0,4):
    ds(500,0+=90,10,3)                               #speed, desired heading, KP, time
    turn(500,90+=90, 0.75,0.25)                       #speed, degrees, KP, time

print('DONE')
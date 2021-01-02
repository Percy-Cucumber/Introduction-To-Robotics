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


#Program
print('START')

ds(500,0,10,3)                                #drive straight with: base speed = 500, desired heading = 0, KP = 10, and desired run time = 3 seconds
ds(500,90,7.5,0.25)                           #furn 90° at base power = 5, KP = 7.5, and desired run time of 0.25

ds(500,90,10,3)
ds(500,180,7.5,0.25)

ds(500,180,10,3)
ds(500,270,7.5,0.25)

ds(500,270,10,3)
ds(500,360,7.5,0.25)

print('DONE')
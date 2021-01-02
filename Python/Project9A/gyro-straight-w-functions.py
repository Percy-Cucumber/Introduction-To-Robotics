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
def ds(bs,dh,kp,drr):                         #ds = drive straight
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

        lm.run_forever(speed_sp=lp)           # lm = left motor
        rm.run_forever(speed_sp=rp)           # rm = right motor
        print(gyro.value(), lp, rp)           # writes gyro's measured angle, power to left motor, and power to right motor)

    Sound.beep().wait()                       # when a button on the brick is pressed, the robot makes a beepins sound and cuts power to the motors
    lm.stop(stop_action='brake')
    rm.stop(stop_action='brake')


#Program
print('START')

ds(500,0,10,5)                                #drive straight with: base speed = 500, desired heading = 0, KP = 10, and desired run time = 5 seconds

print('DONE')
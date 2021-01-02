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


#Declare Variables
bs = 500                                        #bs = base speed
dh = 0                                          #dh = desired heading
kp = 10                                         #kp = how violently it corrects its trajectory


#Program
print('START')

while btn.any()==False:                         #if button NOT pressed, do everything that is indented
        error = gyro.value() - dh
        lp = bs - kp * error                    #lp = left power
        rp = bs + kp * error                    #rp = right power

        if lp > 1000                            #makes sure that we can't send a power greater than 1000 (100%) can NOT be sent to the motor
            lp = 1000
        if lp < -1000
            lp = -1000
        if rp > 1000
            rp = 1000
        if rp < -1000
            rp = 1000

        lm.run_forever(speed_sp=lp)             #lm = left motor
        rm.run_forever(speed_sp=rp)             #rm = right motor
        print(gyro.value(), lp, rp)             #writes gyro's measured angle, power to left motor, and power to right motor)

Sound.beep().wait()                             #when a button on the brick is pressed, the robot makes a beepins sound and cuts power to the motors
lm.stop(stop_action='brake')
rm.stop(stop_action='brake')

print('DONE')

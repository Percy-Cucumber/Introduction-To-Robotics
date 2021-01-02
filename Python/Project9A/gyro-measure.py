#Import Libraries
from ev3dev.auto import *
import time


#Declare Motors
leftmotor = LargeMotor(OUTPUT_A)
rightmotor = LargeMotor(OUTPUT_D)


#Declare Sensors
gyro = GyroSensor(INPUT_1)
gyro.mode = 'GYRO-RATE'                                #starting the gyro mode in rate and then swapping to angle mode resets the gyro
time.sleep(0.5)
gyro.mode = 'GYRO-ANG'                                 #makes the gyro measure the angle


#Program
print('START')

leftmotor.run_timed(time_sp=10000, speed_sp=100)
rightmotor.run_timed(time_sp=10000, speed_sp=100)

for i in range(0,5):                                   #measures the gyro value five times
    print(gyro.value())                                #writes the angle value that the gyro measures into terminal
    time.sleep(1)                                      #pause for 1 second before taking next gyro reading

print('DONE')

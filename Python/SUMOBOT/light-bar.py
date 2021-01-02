# Import Libraries
from ev3dev.auto import *
import time

LeftMotor = LargeMotor(OUTPUT_D)
RightMotor = LargeMotor(OUTPUT_A)

ls = Sensor(INPUT_2)
ls.mode = 'CAL'

lsLEFT = (ls.value(0)+ls.value(1)+ls.value(2)+ls.value(3))/4
lsRIGHT = (ls.value(4)+ls.value(5)+ls.value(6)+ls.value(7))/4

# Defining Values
white = 50
highpower = 1000
lowpower = 500
backtime = 0.5

# Program
if lsLEFT > white and lsRIGHT < white:
    LeftMotor.run_timed(time_sp=backtime, speed_sp=highpower)
    RightMotor.run_timed(time_sp=backtime, speed_sp=highpower)
    RightMotor.run_forever(speed_sp=highpower)
    LeftMotor.run_forever(speed_sp=lowpower)
if lsRIGHT > white and lsLEFT < white:
    LeftMotor.run_timed(time_sp=backtime, speed_sp=highpower)
    RightMotor.run_timed(time_sp=backtime, speed_sp=highpower)
    RightMotor.run_forever(speed_sp=lowpower)
    LeftMotor.run_forever(speed_sp=highpower)
if lsLEFT > white and lsRIGHT) > white:
    RightMotor.run_forever(speed_sp=highpower)
    LeftMotor.run_forever(speed_sp=highpower)

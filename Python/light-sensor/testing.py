# Import Libraries
from ev3dev.auto import *

#Define Motors & Sensors
leftmotor = LargeMotor(OUTPUT_A)
rightmotor = LargeMotor(OUTPUT_D)
btn = Button()
ls = Sensor(INPUT_4)

ls.mode = 'CAL'

darkness = 75
base = 50
kp = 0.25

#Program
while btn.any() == False:
    _ls = ((ls.value(0)) + (ls.value(1)) + (ls.value(2)) + (ls.value(3)))
    total_ls = (_ls + (ls.value(4)) + (ls.value(5)) + (ls.value(6)) + (ls.value(7))) / 8
    leftmotor.run_forever(speed_sp=(50 + 0.25)*(total_ls-darkness))
    rightmotor.run_forever(speed_sp=(50 - 0.25)*(total_ls-darkness))

    if leftspeed > 1000:
        leftspeed = 1000
    if leftspeed < -1000:
        leftspeed = -1000
    if rightspeed > 1000:
        rightspeed = 1000
    if rightspeed < -1000:
        rightspeed = -1000


leftmotor.stop(stop_action='brake')
rightmotor.stop(stop_action='brake')
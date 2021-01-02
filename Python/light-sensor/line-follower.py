#Import
from ev3dev.auto import*
import time


#Motors & Sensors
leftmotor = LargeMotor(OUTPUT_A)
rightmotor = LargeMotor(OUTPUT_D)
btn = Button()

ls = Sensor(INPUT_4)
ls.mode = 'CAL'


#Variables
_ls = ((ls.value(0)) + (ls.value(1)) + (ls.value(2)) + (ls.value(3)) + (ls.value(4)))
total_ls = ((_ls) + (ls.value(5)) + (ls.value(6)) + (ls.value(7)))/8
old_time = time.time()
integral = 0
base_speed = 100
KP = 5
KD = 0.25
KI = 0.1


#Program
while btn.any() == False:

    left_ls = ((ls.value(0)) + (ls.value(1)) + (ls.value(2)) + (ls.value(3))) / 4
    right_ls = ((ls.value(4)) + (ls.value(5)) + (ls.value(6)) + (ls.value(7))) / 4

    left_error = left_ls - total_ls
    right_error = right_ls - total_ls
    error = left_error - right_error

    total_time = time.time() - old_time

    change_error = error/total_time

    integral = integral + error*total_time

    left_speed = base_speed + KP*error + KD*change_error + KI*integral
    right_speed = base_speed - KP*error - KD*change_error - KI*integral

    if left_speed > 1000:
        left_speed = 1000
    if left_speed < -1000:
        left_speed = -1000
    if right_speed > 1000:
        right_speed = 1000
    if right_speed < -1000:
        right_speed = -1000

    leftmotor.run_forever(speed_sp=left_speed)
    rightmotor.run_forever(speed_sp=right_speed)


#Ending
leftmotor.stop(stop_action= 'brake')
rightmotor.stop (stop_action= 'brake')

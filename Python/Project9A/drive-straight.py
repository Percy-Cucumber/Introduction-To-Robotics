from ev3dev.auto import *                           #import ev3 and time (or anything I will need in my code later on) so it is available farther down the road
import time

leftmotor = LargeMotor(OUTPUT_A)                    #assaign names for the drive motors
rightmotor = LargeMotor(OUTPUT_D)

print('START')                                      #prints "START" in the terminal so I know that the program has started

leftmotor.run_timed(time_sp=1000, speed_sp=100)     #command to turn motors on at 10% power for 1 second (power goes to 1000 and time is in miliseconds)
rightmotor.run_timed(time_sp=1000, speed_sp=100)
leftmotor.wait_while('running')                     #makes the robot wait until the motors stop turning before it progresses to the next step
rightmotor.wait_while('running')

print('DONE')                                       #prints "DONE" in the terminal so I know that program is finished running


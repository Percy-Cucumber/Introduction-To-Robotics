# Import Libraries
from ev3dev.auto import *
import time


# Declare Motors
LeftMotor = LargeMotor(OUTPUT_D)
RightMotor = LargeMotor(OUTPUT_A)

# Declare Sensors
cs1 = ColorSensor(INPUT_4)
cs1.mode = 'COL-REFLECT'

cs2 = ColorSensor(INPUT_1)
cs2.mode = 'COL-REFLECT'

us = UltrasonicSensor(INPUT_3); assert us.connected
us.mode = 'US-DIST-CM'

l = LargeMotor(OUTPUT_A)
r = LargeMotor(OUTPUT_D)

ls = Sensor(INPUT_2)
ls.mode = 'CAL'

# Declare Object
btn = Button()

# Define Functions
def findrobot(threshold, backleftthresh, backrightthresh, frontthresh):
    print('SEEKING ENEMY')
    while us.value(0) > threshold and btn.check_buttons(buttons=['left', 'right']) == False and detectline(backleftthresh, backrightthresh, frontthresh) == 0:
        RightMotor.run_forever(speed_sp=-800)
        LeftMotor.run_forever(speed_sp=800)
    distance = us.value(0) / 10
    print(distance, 'cm')

def charge(threshold, backleftthresh, backrightthresh, frontthresh):
    print('ATTACKING ENEMY')
    while us.value(0) < threshold and btn.check_buttons(buttons=['left', 'right']) == False and detectline(backleftthresh, backrightthresh, frontthresh) == 0:
        LeftMotor.run_forever(speed_sp=-1000)
        RightMotor.run_forever(speed_sp=-1000)

def avoidline(backleftthresh, backrightthresh, frontthresh):
    while detectline(backleftthresh, backrightthresh, frontthresh) != 0:

        if detectline(backleftthresh, backrightthresh, frontthresh) in set([1,2,3]):
            while detectline(backleftthresh, backrightthresh, frontthresh) in set([1,2,3]):
                RightMotor.run_forever(speed_sp=-1000)
                LeftMotor.run_forever(speed_sp=-1000)
            currenttime = time.time()
            while time.time() - currenttime < 1 and detectline(backleftthresh, backrightthresh, frontthresh) == 0:
                RightMotor.run_forever(speed_sp=-1000)
                LeftMotor.run_forever(speed_sp=-1000)

        if detectline(backleftthresh, backrightthresh, frontthresh) in set([4,5,6]):
            while detectline(backleftthresh, backrightthresh, frontthresh) in set([4,5,6]):
                RightMotor.run_forever(speed_sp=1000)
                LeftMotor.run_forever(speed_sp=1000)
            currenttime = time.time()
            while time.time() - currenttime < 1 and detectline(backleftthresh, backrightthresh, frontthresh) == 0:
                RightMotor.run_forever(speed_sp=1000)
                LeftMotor.run_forever(speed_sp=1000)

        if detectline(backleftthresh, backrightthresh, frontthresh) in set([7,8]):
            while detectline(backleftthresh, backrightthresh, frontthresh) in set([7,8]):
                RightMotor.run_forever(speed_sp=-1000)
                LeftMotor.run_forever(speed_sp=1000)
            currenttime = time.time()
            while time.time() - currenttime < 1 and detectline(backleftthresh, backrightthresh, frontthresh):
                RightMotor.run_forever(speed_sp=-1000)
                LeftMotor.run_forever(speed_sp=-1000)

def detectline(backleftthresh, backrightthresh, frontthresh):
    if cs1.value(0) > backleftthresh and cs2.value(0) < backrightthresh:
        print('CASE 1')
        return 1
    if cs2.value(0) > backrightthresh and cs1.value(0) < backleftthresh:
        print('CASE 2')
        return 2
    if cs1.value(0) > backleftthresh and cs2.value(0) > backrightthresh:
        print('CASE 3')
        return 3
    if ls.value(0) > frontthresh and ls.value(7) < frontthresh:
        print('CASE 4')
        return 4
    if ls.value(7) > frontthresh and ls.value(0) < frontthresh:
        print('CASE 5')
        return 5
    if ls.value(0) > frontthresh and ls.value(7) > frontthresh:
        print('CASE 6')
        return 6
    if ls.value(0) > frontthresh and cs1.value(0) > backleftthresh:
        print('CASE 7')
        return 7
    if ls.value(7) > frontthresh and cs2.value(0) > backrightthresh:
        print('CASE 8')
        return 8
    if cs1.value(0) < backleftthresh and cs2.value(0) < backrightthresh and ls.value(0) < frontthresh and ls.value(7) < frontthresh:
        #print('CASE 0')
        return 0







# Program

#while btn.any() ==False: # beginning of the loop for the whole program

# Program for 'Find and Charge'
print('step0')

threshold = 600
backleftthresh = 20
backrightthresh = 20
frontthresh = 20

while btn.right == False:
    time.sleep(0.2) # do nothing
    print('step1')

while 0==0:
    print('step2')
    findrobot(threshold, backleftthresh, backrightthresh, frontthresh)
    if detectline(backleftthresh, backrightthresh, frontthresh) != 0:
        avoidline(backleftthresh, backrightthresh, frontthresh)
    charge(threshold, backleftthresh, backrightthresh, frontthresh)
    if detectline(backleftthresh, backrightthresh, frontthresh) != 0:
        avoidline(backleftthresh, backrightthresh, frontthresh)

    if btn.check_buttons(buttons=['left', 'right']):
        break
    #Sound.beep()

    print('step3')

Sound.beep()
LeftMotor.stop(stop_action='brake')
RightMotor.stop(stop_action='brake')

#if detectline(backleftthresh, backrightthresh, frontthresh) != 0:
#    avoidline(backleftthresh, backrightthresh, frontthresh)
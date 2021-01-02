# python3 test_1


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

lsLEFT = (ls.value(0)+ls.value(1)+ls.value(2)+ls.value(3))/4
lsRIGHT = (ls.value(4)+ls.value(5)+ls.value(6)+ls.value(7))/4

value = 30                                                                     # change this to whatever you want


# Define Functions
def findRobot(value):
    while us.value(0) > value and btn.left and detectline == False:
        LeftMotor.run_forever(speed_sp= 1000)
        RightMotor.run_forever(speed_sp=-1000)


def charge(value):
    while us.value(0) < value and btn.left == False:
        LeftMotor.run_forever(1000)
        RightMotor.run_forever(1000)


# Function  for Light Sensor
def lightbar():
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

    if lsLEFT > white and lsRIGHT > white:
        RightMotor.run_forever(speed_sp=highpower)
    LeftMotor.run_forever(speed_sp=highpower)


# Function for Color Sensors
def colorsensor(thresholdvalue):
    while cs1.value(0) >= thresholdvalue:                                      # cs1 is on the left side

        RightMotor.run_forever(speed_sp=-800)
        LeftMotor.run_forever(speed_sp=800)

        if cs1.value(0) and cs2.value(0) >= thresholdvalue:
            RightMotor.run_forever(speed_sp=1000)
            LeftMotor.run_forever(speed_sp=1000)

    while cs2.value(0) >= thresholdvalue:                                      # cs2 is on the right side

        RightMotor.run_forever(speed_sp=800)
        LeftMotor.run_forever(speed_sp=-800)

        if cs2.value(0) and cs1.value(0) >= thresholdvalue:
            RightMotor.run_forever(speed_sp=1000)
            LeftMotor.run_forever(speed_sp=1000)

def avoidline(backleftthresh, backrightthresh, frontthresh):

def detectline(backleftthresh, backrightthresh, frontthresh):


# Declare Object
btn = Button()


# Declare Variables
basespeed = 1000
turnSpeed = 1000
#ultrasonicthreshold = 1                                                       # INPUT VALUE ** ASK COLIN


# Defining Values
white = 50
highpower = 1000
lowpower = 500
backtime = 0.5


# Program

#while btn.any() ==False:                                                     # beginning of the loop for the whole program

# Program for 'Find and Charge'
print('step0')

while btn.right == False:
    time.sleep(0.2) # do nothing
    print('step1')
    print('cs1:', cs1.value(0))
    print('cs2:', cs2.value(0))

while 0==0:

    #findRobot(value)
    #charge(value)
    #Sound.beep()

    print('UltraSonic', us.value(0))

    lightbar()

    colorsensor(20)

    if btn.check_buttons(buttons=['left', 'right']):
        break
    #Sound.beep()



Sound.beep()
LeftMotor.stop(stop_action='brake')
RightMotor.stop(stop_action='brake')


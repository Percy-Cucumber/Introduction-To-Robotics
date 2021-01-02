# Import Libraries
from ev3dev.auto import *
import time

#Define Motors & Sensors
lm = LargeMotor(OUTPUT_A)
rm = LargeMotor(OUTPUT_D)
btn = Button()
ls = Sensor(INPUT_4)

ls.mode = 'CAL'


#Program
while btn.any() == False:
    print(ls.value(0),(ls.value(1),(ls.value(2),(ls.value(3))
    time.sleep(0.5)


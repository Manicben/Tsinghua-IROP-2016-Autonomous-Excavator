#!/usr/bin/python

from Raspi_PWM_Servo_Driver import PWM
import time

# ===========================================================================
# Input Test Code
# Author: Benjamin Withers
# EIE Imperial College London
# ===========================================================================

# Initialise the PWM device using the default address
# bmp = PWM(0x40, debug=True)
pwm = PWM(0x6F)

# Set Servo Min, Mid and Max positions
# Play around with the pulse length to get desired position
# Each servo is slightly different, so be careful
# Try not to overload servos or drive too many at once
# Channel 0 - Servo 1
servoMin0 = 150  # Min pulse length out of 4096
servoMid0 = 410
servoMax0 = 600  # Max pulse length out of 4096

# Channel 1 - Servo 2
servoMin1 = 150  # Min pulse length out of 4096
servoMid1 = 345
servoMax1 = 600  # Max pulse length out of 4096

# Channel 14 - Servo 3
servoMin14 = 440  # Min pulse length out of 4096
servoMid14 = 265
servoMax14 = 120  # Max pulse length out of 4096

# Channel 15 - Servo 4
servoMin15 = 150  # Min pulse length out of 4096
servoMid15 = 365
servoMax15 = 600  # Max pulse length out of 4096

pwm.setPWMFreq(60)          # Set frequency to 60 Hz

#Set all to Min
#pwm.setPWM(0, 0, servoMin)
#time.sleep(1)
#pwm.setPWM(1, 0, servoMin)
#time.sleep(1)
#pwm.setPWM(14, 0, servoMin)
#time.sleep(1)
#pwm.setPWM(15, 0, servoMin)
#time.sleep(1)

while (True):

    # Input keyboard command
    command = str(raw_input("Input: "))

    #Channel 0
    if command == "q":
        pwm.setPWM(0, 0, servoMin0)
        time.sleep(1)

    if command == "a":
        pwm.setPWM(0, 0, servoMid0)
        time.sleep(1)

    if command == "z":
        pwm.setPWM(0, 0, servoMax0)
        time.sleep(1)

    #Channel 1
    if command == "w":
        pwm.setPWM(1, 0, servoMin1)
        pwm.setPWM(14, 0, (servoMid14 + 195))
        time.sleep(1)

    if command == "s":
        pwm.setPWM(1, 0, servoMid1)
        pwm.setPWM(14, 0, servoMid14)
        time.sleep(1)

    if command == "x":
        pwm.setPWM(1, 0, servoMax1)
        time.sleep(1)

    #Channel 14
    if command == "e":
        pwm.setPWM(14, 0, servoMin14)
        time.sleep(1)

    if command == "d":
        pwm.setPWM(14, 0, servoMid14)
        time.sleep(1)

    if command == "c":
        pwm.setPWM(14, 0, servoMax14)
        time.sleep(1)

    #Channel 15
    if command == "r":
        pwm.setPWM(15, 0, servoMin15)
        time.sleep(1)

    if command == "f":
        pwm.setPWM(15, 0, servoMid15)
        time.sleep(1)

    if command == "v":
        pwm.setPWM(15, 0, servoMax15)
        time.sleep(1)

    

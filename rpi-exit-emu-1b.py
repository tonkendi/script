#!/usr/bin/python
#Import libs
import RPi.GPIO as GPIO
import os
import time
#Set Environment
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(02, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#Code
try:
 while True:
  GPIO.wait_for_edge(02, GPIO.FALLING)
  pressedat = time.clock()
  while GPIO.input(02) == GPIO.LOW:
    releasedat = time.clock()
    if (releasedat - pressedat) >= 0.500:
      os.system("killall -9 retroarch mupen64plus fba2x scummvm &> /dev/null")
  #Reset Control Vars
  releasedat = pressedat = 0
#Cleaning Gpio ports on Error or Exit
finally:
   GPIO.cleanup()

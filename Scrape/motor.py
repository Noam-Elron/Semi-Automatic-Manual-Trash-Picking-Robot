# Importing Libraries

import RPi.GPIO as GPIO
import time
from tkinter import *
import tkinter.font


PWMPin = 26 # PWM Pin connected to ENA.
Motor1 = 20 # Connected to Input 1.
Motor2 = 21 # Connected to Input 2.
Motor3 = 6
Motor4 = 13
PWMPin2 = 12
MotorTop1 = 17
MotorTop2 = 27
PWMMotortop = 22

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) # BCM-GPIO Locations, Board- Physical Locations GPIO
GPIO.setup(PWMPin, GPIO.OUT) 
GPIO.setup(Motor1, GPIO.OUT)
GPIO.setup(Motor2, GPIO.OUT)
GPIO.setup(PWMPin2, GPIO.OUT) 
GPIO.setup(Motor3, GPIO.OUT)
GPIO.setup(Motor4, GPIO.OUT)
GPIO.setup(MotorTop1, GPIO.OUT) 
GPIO.setup(MotorTop2, GPIO.OUT)
GPIO.setup(PWMMotortop, GPIO.OUT)

GPIO.output(PWMPin, GPIO.LOW) 
GPIO.output(Motor1, GPIO.LOW)
GPIO.output(Motor2, GPIO.LOW)
GPIO.output(PWMPin2, GPIO.OUT) 
GPIO.output(Motor3, GPIO.OUT)
GPIO.output(Motor4, GPIO.OUT)
GPIO.output(MotorTop1, GPIO.OUT) 
GPIO.output(MotorTop2, GPIO.OUT)
GPIO.output(PWMMotortop, GPIO.OUT)

PwmValue = GPIO.PWM(PWMPin, 2000) # PWM frequency to 2000.
PwmValue2 = GPIO.PWM(PWMPin2, 2000) # PWM frequency to 2000.
PwmValueTop =  GPIO.PWM(PWMMotortop, 2000) 
PwmValue.start(75) 
PwmValue2.start(75) 
PwmValueTop.start(90)



def BeltStart():
    GPIO.output(MotorTop1, GPIO.HIGH)
    GPIO.output(MotorTop2, GPIO.LOW)

def BeltStop():
    GPIO.output(MotorTop1, GPIO.LOW)
    GPIO.output(MotorTop2, GPIO.LOW)
      
def MotorClockwise():
    GPIO.output(Motor1, GPIO.HIGH) # Motor will move in clockwise direction.
    GPIO.output(Motor2, GPIO.LOW)
    GPIO.output(Motor3, GPIO.HIGH) # Motor will move in clockwise direction.
    GPIO.output(Motor4, GPIO.LOW)

def MotorLeft():
    PwmValue.ChangeDutyCycle(80)
    GPIO.output(Motor1, GPIO.LOW)
    GPIO.output(Motor2, GPIO.HIGH)
    GPIO.output(Motor3, GPIO.HIGH)
    GPIO.output(Motor4, GPIO.LOW)

def MotorRight():
    PwmValue2.ChangeDutyCycle(80)
    GPIO.output(Motor1, GPIO.HIGH)
    GPIO.output(Motor2, GPIO.LOW)
    GPIO.output(Motor3, GPIO.LOW)
    GPIO.output(Motor4, GPIO.HIGH)
    
def MotorAntiClockwise():
    GPIO.output(Motor1, GPIO.LOW) # Motor will move in anti-clockwise direction.
    GPIO.output(Motor2, GPIO.HIGH)
    GPIO.output(Motor3, GPIO.LOW) # Motor will move in anti-clockwise direction.
    GPIO.output(Motor4, GPIO.HIGH)

def MotorStop():
    GPIO.output(Motor1, GPIO.LOW) # Motor will stop.
    GPIO.output(Motor2, GPIO.LOW)
    GPIO.output(Motor3, GPIO.LOW) # Motor will stop.
    GPIO.output(Motor4, GPIO.LOW)
    



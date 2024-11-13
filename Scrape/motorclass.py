# Importing Libraries
import RPi.GPIO as GPIO


'''
PWMPin = 26 # PWM Pin connected to ENA.
Motor1 = 20 # Connected to Input 1.
Motor2 = 21 # Connected to Input 2.
Motor3 = 6
Motor4 = 13
PWMPin2 = 12
MotorTop1 = 17
MotorTop2 = 27
PWMMotortop = 22
'''

class MotorActivation:
    PWMPin = 26 # PWM Pin connected to ENA.
    Motor1 = 20 # Connected to Input 1.
    Motor2 = 21 # Connected to Input 2.
    Motor3 = 6
    Motor4 = 13
    PWMPin2 = 12
    MotorTop1 = 17
    MotorTop2 = 27
    PWMMotortop = 22
    def __init__(self):
        self.gpio_setup()
        self.pwm_setup()
        
    def gpio_setup(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM) # BCM-GPIO Locations, Board- Physical Locations GPIO
        GPIO.setup(self.PWMPin, GPIO.OUT) 
        GPIO.setup(self.Motor1, GPIO.OUT)
        GPIO.setup(self.Motor2, GPIO.OUT)
        GPIO.setup(self.PWMPin2, GPIO.OUT) 
        GPIO.setup(self.Motor3, GPIO.OUT)
        GPIO.setup(self.Motor4, GPIO.OUT)
        GPIO.setup(self.MotorTop1, GPIO.OUT) 
        GPIO.setup(self.MotorTop2, GPIO.OUT)
        GPIO.setup(self.PWMMotortop, GPIO.OUT)

    def pwm_setup(self):
        PwmValue = GPIO.PWM(self.PWMPin, 2000) # PWM frequency to 2000.
        PwmValue2 = GPIO.PWM(self.PWMPin2, 2000) # PWM frequency to 2000.
        PwmValueTop =  GPIO.PWM(self.PWMMotortop, 2000) 
        PwmValue.start(75) 
        PwmValue2.start(75) 
        PwmValueTop.start(80)

    def belt_start(self):
        GPIO.output(self.MotorTop1, GPIO.HIGH)
        GPIO.output(self.MotorTop2, GPIO.LOW)

    def belt_stop(self):
        GPIO.output(self.MotorTop1, GPIO.LOW)
        GPIO.output(self.MotorTop2, GPIO.LOW)
        
    def motor_clockwise(self):
        GPIO.output(self.Motor1, GPIO.HIGH) 
        GPIO.output(self.Motor2, GPIO.LOW)
        GPIO.output(self.Motor3, GPIO.HIGH) 
        GPIO.output(self.Motor4, GPIO.LOW)

    def motor_left(self):
        self.PwmValue.ChangeDutyCycle(80)
        self.PwmValue2.ChangeDutyCycle(100)
        GPIO.output(self.Motor1, GPIO.LOW)
        GPIO.output(self.Motor2, GPIO.HIGH)
        GPIO.output(self.Motor3, GPIO.HIGH)
        GPIO.output(self.Motor4, GPIO.LOW)

    def motor_right(self):
        self.PwmValue.ChangeDutyCycle(100)
        self.PwmValue2.ChangeDutyCycle(80)
        GPIO.output(self.Motor1, GPIO.HIGH)
        GPIO.output(self.Motor2, GPIO.LOW)
        GPIO.output(self.Motor3, GPIO.LOW)
        GPIO.output(self.Motor4, GPIO.HIGH)
        
    def motor_anti_clockwise(self):
        GPIO.output(self.Motor1, GPIO.LOW) 
        GPIO.output(self.Motor2, GPIO.HIGH)
        GPIO.output(self.Motor3, GPIO.LOW) 
        GPIO.output(self.Motor4, GPIO.HIGH)

    def motor_stop(self):
        GPIO.output(self.Motor1, GPIO.LOW) 
        GPIO.output(self.Motor2, GPIO.LOW)
        GPIO.output(self.Motor3, GPIO.LOW) 
        GPIO.output(self.Motor4, GPIO.LOW)
    
    @staticmethod
    def release_gpios():
        GPIO.cleanup()


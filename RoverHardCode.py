#Libraries
#----------------------------------------------------------------------
import RPi.GPIO as GPIO
import time


#----------------------------------------------------------------------



#Set global variables
#----------------------------------------------------------------------
L298N_IN1 = 7  #assign pin 7/GPIO04
L298N_IN2 = 11 #assign pin 11/GPIO17
L298N_IN3 = 12 #assign pin12/GPIO18
L298N_IN4 = 13 #assign pin13/GPIO27

WHEEL_RIGHT_FRONT = 15   #assign pin 15/GPIO22
WHEEL_RIGHT_MIDDLE = 16  #assign pin 16/GPIO23
WHEEL_RIGHT_REAR = 18    #assign pin 18/GPIO24
WHEEL_LEFT_REAR = 22     #assign pin 22/GPIO25
WHEEL_LEFT_MIDDLE = 29   #assign pin 19/GPIO05
WHEEL_LEFT_FRONT = 31    #assign pin 31/GPIO06


#----------------------------------------------------------------------



#Initialize GPIO Settings
#----------------------------------------------------------------------
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
pygame.init()
pygame.mixer.init()
#----------------------------------------------------------------------



#Setup GPIO pins
#----------------------------------------------------------------------
GPIO.setup(L298N_IN1, GPIO.OUT)
GPIO.output(L298N_IN1, GPIO.LOW)
GPIO.setup(L298N_IN2, GPIO.OUT)
GPIO.output(L298N_IN2, GPIO.LOW)
GPIO.setup(L298N_IN3, GPIO.OUT)
GPIO.output(L298N_IN3, GPIO.LOW)
GPIO.setup(L298N_IN4, GPIO.OUT)
GPIO.output(L298N_IN4, GPIO.LOW)

GPIO.setup(WHEEL_RIGHT_FRONT, GPIO.OUT)
GPIO.output(WHEEL_RIGHT_FRONT, GPIO.LOW)
GPIO.setup(WHEEL_RIGHT_MIDDLE, GPIO.OUT)
GPIO.output(WHEEL_RIGHT_MIDDLE, GPIO.LOW)
GPIO.setup(WHEEL_RIGHT_REAR, GPIO.OUT)
GPIO.output(WHEEL_RIGHT_REAR, GPIO.LOW)
GPIO.setup(WHEEL_LEFT_REAR, GPIO.OUT)
GPIO.output(WHEEL_LEFT_REAR, GPIO.LOW)
GPIO.setup(WHEEL_LEFT_MIDDLE, GPIO.OUT)
GPIO.output(WHEEL_LEFT_MIDDLE, GPIO.LOW)
GPIO.setup(WHEEL_LEFT_FRONT, GPIO.OUT)
GPIO.output(WHEEL_LEFT_FRONT, GPIO.LOW)

#----------------------------------------------------------------------



#Set up PWM (Pulse Width Modulation) objects
#----------------------------------------------------------------------
PWM_L298N_IN1 = GPIO.PWM(L298N_IN1, 207)
PWM_L298N_IN2 = GPIO.PWM(L298N_IN2, 207)
PWM_L298N_IN3 = GPIO.PWM(L298N_IN3, 207)
PWM_L298N_IN4 = GPIO.PWM(L298N_IN4, 207)
PWM_L298N_IN1.start(0)
PWM_L298N_IN2.start(0)
PWM_L298N_IN3.start(0)
PWM_L298N_IN4.start(0)

PWM_WHEEL_RIGHT_FRONT = GPIO.PWM(WHEEL_RIGHT_FRONT, 50)
PWM_WHEEL_RIGHT_MIDDLE = GPIO.PWM(WHEEL_RIGHT_MIDDLE, 50)
PWM_WHEEL_RIGHT_REAR = GPIO.PWM(WHEEL_RIGHT_REAR, 50)
PWM_WHEEL_LEFT_REAR = GPIO.PWM(WHEEL_LEFT_REAR, 50)
PWM_WHEEL_LEFT_MIDDLE = GPIO.PWM(WHEEL_LEFT_MIDDLE, 50)
PWM_WHEEL_LEFT_FRONT = GPIO.PWM(WHEEL_LEFT_FRONT, 50)

PWM_WHEEL_RIGHT_FRONT.start(7.5)
PWM_WHEEL_RIGHT_MIDDLE.start(7.5)
PWM_WHEEL_RIGHT_REAR.start(7.5)
PWM_WHEEL_LEFT_REAR.start(7.5)
PWM_WHEEL_LEFT_MIDDLE.start(7.5)
PWM_WHEEL_LEFT_FRONT.start(7.5)

time.sleep(1)

#----------------------------------------------------------------------



#Funtions
#----------------------------------------------------------------------
#Set all wheel servos to 90 degree
def straightenWheels():
    print("Straighten wheels")
    PWM_WHEEL_RIGHT_FRONT.ChangeDutyCycle(7.5)
    PWM_WHEEL_RIGHT_MIDDLE.ChangeDutyCycle(7.5)
    PWM_WHEEL_RIGHT_REAR.ChangeDutyCycle(7.5)
    PWM_WHEEL_LEFT_REAR.ChangeDutyCycle(7.5)
    PWM_WHEEL_LEFT_MIDDLE.ChangeDutyCycle(7.5)
    PWM_WHEEL_LEFT_FRONT.ChangeDutyCycle(7.5)
    time.sleep(1)

#Toe-in front wheels by 45 degrees and toe-out rear wheels by 45 degrees 
def turnWheels():
    print("Turn wheels")
    PWM_WHEEL_RIGHT_FRONT.ChangeDutyCycle(5)
    PWM_WHEEL_RIGHT_MIDDLE.ChangeDutyCycle(7.5)
    PWM_WHEEL_RIGHT_REAR.ChangeDutyCycle(10)
    PWM_WHEEL_LEFT_REAR.ChangeDutyCycle(5)
    PWM_WHEEL_LEFT_MIDDLE.ChangeDutyCycle(7.5)
    PWM_WHEEL_LEFT_FRONT.ChangeDutyCycle(10)
    time.sleep(1)

#Stop rover movement
def stop():
    print("Stop")
    PWM_L298N_IN1.ChangeDutyCycle(0)
    PWM_L298N_IN2.ChangeDutyCycle(0)
    PWM_L298N_IN3.ChangeDutyCycle(0)
    PWM_L298N_IN4.ChangeDutyCycle(0)
    time.sleep(.5)
    straightenWheels()

    
#Make all drive wheels spin forward
def forward():
    print("Forward")
    straightenWheels()
    PWM_L298N_IN1.ChangeDutyCycle(0)
    PWM_L298N_IN2.ChangeDutyCycle(25)
    PWM_L298N_IN3.ChangeDutyCycle(20)
    PWM_L298N_IN4.ChangeDutyCycle(0)
    

#Make all drive wheels spin backwards
def reverse():
    print("Reverse")
    straightenWheels()
    PWM_L298N_IN1.ChangeDutyCycle(20)
    PWM_L298N_IN2.ChangeDutyCycle(0)
    PWM_L298N_IN3.ChangeDutyCycle(0)
    PWM_L298N_IN4.ChangeDutyCycle(25)

#Make right drive wheels spin backwards and left drive wheels spin forward
def spinRight():
    print("Spin right")
    turnWheels()
    PWM_L298N_IN1.ChangeDutyCycle(0)
    PWM_L298N_IN2.ChangeDutyCycle(20)
    PWM_L298N_IN3.ChangeDutyCycle(0)
    PWM_L298N_IN4.ChangeDutyCycle(20)
    time.sleep(1.3)
    stop()
    straightenWheels()

#Make right drive wheels spin forward and left drive wheels spin backwards
def spinLeft():
    print("Spin left")
    turnWheels()
    PWM_L298N_IN1.ChangeDutyCycle(20)
    PWM_L298N_IN2.ChangeDutyCycle(0)
    PWM_L298N_IN3.ChangeDutyCycle(20)
    PWM_L298N_IN4.ChangeDutyCycle(0)
    time.sleep(1.3)
    stop()
    straightenWheels()

    
#----------------------------------------------------------------------

print("Start rover")
straightenWheels()
try:
    while True:
        forward()
        time.sleep(1)
        stop()
        time.sleep(.5)
        spinLeft()
        forward()
        time.sleep(4)
        stop()
        spinRight()
        forward()
        time.sleep(9)
        stop()
        spinRight()
        forward()
        time.sleep(4)
        stop()
        spinLeft()
        forward()
        time.sleep(1)
        stop()
        celebrate()

except KeyboardInterrupt:
    print("Stoping")

print("End rover")


GPIO.cleanup

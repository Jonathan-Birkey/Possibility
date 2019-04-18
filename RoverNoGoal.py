#Libraries
#----------------------------------------------------------------------
import RPi.GPIO as GPIO
import time
import Adafruit_ADXL345
import dht11
import pygame
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

DISTANCE_SENSOR_FRONT_TRIGGER = 24 #assign pin 24/GPIO08
DISTANCE_SENSOR_FRONT_ECHO = 26    #assign pin 26/GPIO07
DISTANCE_SENSOR_RIGHT_TRIGGER = 32 #assign pin 32/GPIO12
DISTANCE_SENSOR_RIGHT_ECHO = 33    #assign pin 33/GPIO13
DISTANCE_SENSOR_LEFT_TRIGGER = 36  #assign pin 36/GPIO16
DISTANCE_SENSOR_LEFT_ECHO = 35     #assign pin 35/GPIO19

PHOTO_CELL = 40 #assign pin 40/GPIO21

ACCEL = Adafruit_ADXL345.ADXL345() #create an ADXL345 instance
TEMP = dht11.DHT11(pin=38) #create a DHT11 instance

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

GPIO.setup(DISTANCE_SENSOR_FRONT_TRIGGER, GPIO.OUT)
GPIO.output(DISTANCE_SENSOR_FRONT_TRIGGER, GPIO.LOW)
GPIO.setup(DISTANCE_SENSOR_FRONT_ECHO, GPIO.IN)
GPIO.setup(DISTANCE_SENSOR_RIGHT_TRIGGER, GPIO.OUT)
GPIO.output(DISTANCE_SENSOR_RIGHT_TRIGGER, GPIO.LOW)
GPIO.setup(DISTANCE_SENSOR_RIGHT_ECHO, GPIO.IN)
GPIO.setup(DISTANCE_SENSOR_LEFT_TRIGGER, GPIO.OUT)
GPIO.output(DISTANCE_SENSOR_LEFT_TRIGGER, GPIO.LOW)
GPIO.setup(DISTANCE_SENSOR_LEFT_ECHO, GPIO.IN)


GPIO.setup(PHOTO_CELL, GPIO.OUT)
GPIO.output(PHOTO_CELL, GPIO.LOW)
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

#Pulse right side wheels a little faster
def veerRight():
    print("Veer right")
    straightenWheels()
    PWM_L298N_IN1.ChangeDutyCycle(0)
    PWM_L298N_IN2.ChangeDutyCycle(30)
    PWM_L298N_IN3.ChangeDutyCycle(20)
    PWM_L298N_IN4.ChangeDutyCycle(0)


#Pulse left side wheels a little faster
def veerLeft():
    print("Veer left")
    straightenWheels()
    PWM_L298N_IN1.ChangeDutyCycle(0)
    PWM_L298N_IN2.ChangeDutyCycle(20)
    PWM_L298N_IN3.ChangeDutyCycle(30)
    PWM_L298N_IN4.ChangeDutyCycle(0)

#Check the temapture in Fahrenheit
def checkTemp():
    print("Check tempature")
    result = TEMP.read()
    result.temperature = (result.temperature * 9/5) + 32
    print("Temperature: %d F" % result.temperature )
    print("Humidity: %d %%" % result.humidity)
    return result

#Check rovers relative X, Y, and Z position
def checkPosition():
    print("Check position")
    position = ACCEL.read()
    print('X={0}, Y={1}, Z={2}'.format(position[0], position[1], position[2]))
    return position

#Ping front ultrasonic distance sensor
def checkFrontDistance():
    print("Check front distance")
    GPIO.output(DISTANCE_SENSOR_FRONT_TRIGGER, GPIO.HIGH)
    time.sleep(0.0001)
    GPIO.output(DISTANCE_SENSOR_FRONT_TRIGGER, GPIO.LOW)
    while GPIO.input(DISTANCE_SENSOR_FRONT_ECHO) == 0:
        start = time.time()

    while GPIO.input(DISTANCE_SENSOR_FRONT_ECHO) == 1:
        stop = time.time()
        if(stop-start > .5):
            break

    duration = stop - start
    distance = duration * 17150
    distance = round(distance, 2)
    print("Front distance: %d cm" % distance)
    return distance

#Ping right ultrasonic distance sensor
def checkRightDistance():
    print("Check right distance")
    GPIO.output(DISTANCE_SENSOR_RIGHT_TRIGGER, GPIO.HIGH)
    time.sleep(0.0001)
    GPIO.output(DISTANCE_SENSOR_RIGHT_TRIGGER, GPIO.LOW)
    while GPIO.input(DISTANCE_SENSOR_RIGHT_ECHO) == 0:
        start = time.time()

    while GPIO.input(DISTANCE_SENSOR_RIGHT_ECHO) == 1:
        stop = time.time()
        if(stop-start > .5):
            break

    duration = stop - start
    distance = duration * 17150
    distance = round(distance, 2)
    print("Right distance: %d cm" % distance)
    return distance

#Ping rear ultrasonic distance sensor
def checkLeftDistance():
    print("Check right side distance")
    GPIO.output(DISTANCE_SENSOR_LEFT_TRIGGER, GPIO.HIGH)
    time.sleep(0.0001)
    GPIO.output(DISTANCE_SENSOR_LEFT_TRIGGER, GPIO.LOW)
    while GPIO.input(DISTANCE_SENSOR_LEFT_ECHO) == 0:
        start = time.time()
        

    while GPIO.input(DISTANCE_SENSOR_LEFT_ECHO) == 1:
        stop = time.time()
        if(stop-start > .5):
            break
    

    duration = stop - start
    distance = duration * 17150
    distance = round(distance, 2)
    print("Left distance: %d cm" % distance)
    return distance

    
#Check the current brightness of the rovers position
def checkIllumination():
    print("Check Illumination")
    count = 0
    GPIO.setup(PHOTO_CELL, GPIO.OUT)
    GPIO.output(PHOTO_CELL, GPIO.LOW)
    time.sleep(0.1)
    GPIO.setup(PHOTO_CELL, GPIO.IN)
    while(GPIO.input(PHOTO_CELL) == GPIO.LOW):
        count += 1

    if(count <= 9999):
        print("Really bright")
    elif(count >= 10000 and count <= 70000):
        print("Bright room")
    elif(count > 70000 and count <= 300000):
        print("Well lit room")
    elif(count >= 300001 and count <= 1500000):
        print("Getting pretty dark")
    else:
        print("Too dark")
    return count

#----------------------------------------------------------------------

print("Start rover")
straightenWheels()
previousLeftDistance = checkLeftDistance()
try:
    while True:

        temp = checkTemp()
        illumination = checkIllumination()
        frontDistance = checkFrontDistance()
        previousLeftDistance = leftDistance()
        leftDistance = checkLeftDistance()
        rightDistance = checkRightDistance()
        
        if(temp > 80):
            stop()
            spinRight()
            spinRight()
        elif(illumination > 300001):
            stop()
            spinRight()
            spinRight()
        elif((leftDistance - previousLeftDistance) > 10):
            stop()
            spinLeft()
        elif(frontDistance < 25):
            stop()
            if(leftDistance < 15):
                if(rightDistance > 15):
                    spintRight()
                else:
                    spinRight()
                    spinRight()
        else:
            forward()
            if(leftDistance < 13):
                veerRight()
            elif(leftDistance > 15):
                veerLeft()



except KeyboardInterrupt:
    print("Stoping")

print("End rover")


GPIO.cleanup

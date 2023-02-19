import RPi.GPIO as GPIO
from time import sleep
import time
from pyrebase import pyrebase
import sys

config = {
    "apiKey": "AIzaSyAHpO0pBeqj9xhJ_wj92QSvWE5Xtbk9O44",
    "authDomain":"smarthomedeneme3.firebaseapp.com",
    "databaseURL": "https://smarthomedeneme3-default-rtdb.firebaseio.com",
    "storageBucket": "smarthomedeneme3.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

GPIO.setmode(GPIO.BCM)  
GPIO.setup(18,GPIO.OUT)  
pwm=GPIO.PWM(18,181)  
pwm.start(0)
temp = 0
doorCheck = "0"
while(1):
    database = firebase.database()
    ProjectBucket = database.child("Door")                        
    door = ProjectBucket.child("State").get().val()
    print(door)
    
    if str(door) == "Open":
        if str(door) != str(doorCheck):
            print("aww")
            print("run")
            doorCheck = door
            pwm.ChangeDutyCycle(30)
        
         
    elif str(door) == "Close" :
        if str(door) != str(doorCheck):
            print("stop")
            doorCheck = door
            pwm.ChangeDutyCycle(10)
            
    time.sleep(3)
        
        
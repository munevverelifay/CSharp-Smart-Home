import RPi.GPIO as GPIO          
from time import sleep
import time
from pyrebase import pyrebase
import sys

config = {
    "apiKey": "***",
    "authDomain":"***",
    "databaseURL": "***",
    "storageBucket": "***"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

in1 = 12
in2 = 13
en = 19
temp1=1
Ampul_Control = "0"

GPIO.setmode(GPIO.BCM)
GPIO.setup(en,GPIO.OUT)
p=GPIO.PWM(en,1000)
p.start(25)
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")    

while(1):
    database = firebase.database()
    ProjectBucket = database.child("Ampul_Control")                            
    ampul = ProjectBucket.child("Ampul_Level").get().val()
    print(ampul)
    
    
    if str(ampul) == "run":
        print("aww")
        if(temp1==1):
            print("run")
            p.ChangeDutyCycle(50)
         
        else:
            print("stop")
            p.ChangeDutyCycle(0)
         


    elif str(ampul) == "stop":
        print("stop")
        p.ChangeDutyCycle(0)


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      

    elif str(ampul) == "low":
        print("low")
        p.ChangeDutyCycle(10)


    elif str(ampul) == "medium":
        print("medium")
        p.ChangeDutyCycle(35)


    elif str(ampul) == "high":
        print("high")
        p.ChangeDutyCycle(80)


    
    elif str(ampul) == "out":
        GPIO.cleanup()
        break
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
    time.sleep(1) 

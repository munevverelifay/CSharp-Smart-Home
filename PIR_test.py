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

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


GPIO_PIR = 4

GPIO.setup(GPIO_PIR,GPIO.IN)
Current_State = 0

try:
    while True:
        Current_State = GPIO.input(GPIO_PIR)
        if Current_State == 1:
            print("Hareket ALGILANDI")
        elif Current_State == 0:
            print("Hareket ALGILANMADI")    
        dato = {"Current_State":str(Current_State)}
        db.child().set(dato)
        time.sleep(5)   

except KeyboardInterrupt:
    pass
   

GPIO.cleanup()

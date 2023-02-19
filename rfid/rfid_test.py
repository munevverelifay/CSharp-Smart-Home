import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep
from pyrebase import pyrebase
import sys

config = {
    "apiKey": "***",
    "authDomain":"***",
    "databaseURL": "**",
    "storageBucket": "***"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

Tag_ID_Elif = "***"
Tag_ID_Zuzu = "***"
Tag_ID_Ali = "***"

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

read = SimpleMFRC522()



while True:
    print("Place your Tag")
    id,Tag = read.read()
    
    control = "0"
    
    id = str(id)
    
    if id == Tag_ID_Elif:
        print("Elif AY Hoşgelgin")        
        control = "elif"
        print("Eif AY kayitli %s" %control)        
        sleep(1)
    elif id == Tag_ID_Zuzu:
        print("Zeynep Uzunsoy Hoşgelgin")        
        control = "zuzu"
        print("Zeynep Uzunsoy kayitli %s" %control)        
        sleep(1)
    elif id == Tag_ID_Ali:
        print("Ali Deniz Hoşgelgin")        
        control = "ali"
        print("Ali Deniz kayitli %s" %control)        
        sleep(1)
    else:
        print("Wrong Tag")
        control = "0"
        print("Kayitli degil %s" %control) 
        sleep(1)
        
    dato = {"control":str(control)}
    db.child("RFID_Control").set(dato)
GPIO.cleanup()

#!/usr/local/bin/python

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

GPIO.setmode(GPIO.BOARD)

#define the pin that goes to the circuit
pin_to_circuit = 11

def rc_time (pin_to_circuit):
    count = 0
  
    #Output on the pin for 
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(1                                                           )

    #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1

    return count

#Catch when script is interrupted, cleanup correctly
try:
    # Main loop
    while True:
        #print(rc_time(pin_to_circuit))
        candela = rc_time(pin_to_circuit)
        print(candela)
        lumen = (candela/12.57)
        print ("Ortamın ışık şiddetinin yaklaşık lümen cinsinden değeri:",lumen,"lm")
        dato = {"Lumen":str(lumen)}
        db.child().set(dato)
        time.sleep(5) 
        
        
        
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()

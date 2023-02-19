import RPi.GPIO as GPIO
from datetime import datetime
from time import sleep
from picamera2 import Picamera2, Preview
import os

import pyrebase
import sys

config = {
    "apiKey": "***",
    "authDomain":"***",
    "databaseURL": "***",
    'projectId': "***",
    "storageBucket": "***.appspot.com",
    'messagingSenderId': "***",
    'appId': "***",
    'measurementId': "***"
}

firebase = pyrebase.initialize_app(config)

storage = firebase.storage()


picam2 = Picamera2()

while True:
    try:
        print("pushed")
        now = datetime.now()
        dt = now.strftime("%d%m%Y%H:%M:%S")
        name = dt+".jpg"
        
        camera_config = picam2.create_still_configuration(main={"size": (1920, 1080)}, lores={"size": (640, 480)}, display="lores")
        picam2.configure(camera_config)
        picam2.start_preview(Preview.QTGL)
        picam2.start()
        picam2.capture_file(name)

        print(name+" saved")
        storage.child(name).put(name)
        print("Image sent")
        os.remove(name)
        print("File Removed")
        sleep(2)
    except:
        picam2.close()
        



        
 

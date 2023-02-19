import RPi.GPIO as GPIO
from datetime import datetime
from time import sleep
from picamera2 import Picamera2, Preview
import os

import pyrebase
import sys

config = {
    "apiKey": "AIzaSyAHpO0pBeqj9xhJ_wj92QSvWE5Xtbk9O44",
    "authDomain":"smarthomedeneme3.firebaseapp.com",
    "databaseURL": "https://smarthomedeneme3-default-rtdb.firebaseio.com",
    'projectId': "smarthomedeneme3",
    "storageBucket": "smarthomedeneme3.appspot.com",
    'messagingSenderId': "551070005895",
    'appId': "1:551070005895:web:d0b518d9a6a4da7a8bd622",
    'measurementId': "G-NP50F66T5X"
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
        



        
 
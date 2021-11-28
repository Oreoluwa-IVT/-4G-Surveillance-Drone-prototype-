#This Program will run on your Raspberry Pi
#For this to work , you have to enable Camera via the Raspberry pi System Configuration
#Access System Configuration on the CLI using "sudo raspi-config"

from picamera import PiCamera
import time

camera=PiCamera()
camera.resolution=(1920,1080)
camera.vflip=True
camera.capture("FistTake.jpg")

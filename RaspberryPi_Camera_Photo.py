#This Program will run on your Raspberry Pi
#For this to work , you have to enable Camera via the Raspberry pi System Configuration
#Access "System Configuration" on the CLI using the command  "sudo raspi-config"

from picamera import PiCamera
import time

camera=PiCamera()
camera.resolution=(1920,1080) # Raspberry pI configureation is set here 
camera.vflip=True # this flip the camera view vertically 
camera.capture("FistTake.jpg") # This line take a snapshot once. (At the instant the camera is started)
camera.stat_preview()
camera.capture("Ayeoluwa.jpg")
camera.start_recording("newvideo.h264")
time.sleep(10) #it takes the video for 10secs then stops 
camera.stop_recording()

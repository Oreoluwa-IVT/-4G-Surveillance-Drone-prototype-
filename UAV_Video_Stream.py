#This Program will run on your Raspberry Pi
#For this to work , you have to enable Camera via the Raspberry pi System Configuration
#Access "System Configuration" on the CLI using the command  "sudo raspi-config"

#Python Script for UAV Video Streaming
import io
import threading , os, signal
import picamera
from picamera import PiCamera
import socketserver
#from evdev import input InputDevice
from select import select
from threading import Condition
from http import server
import threading , os , signal
import subprocess
from subprocess import check_call , call
import sys
import glob
import time

uavcam= PiCamera()
uavcam.resolution=(1920,1080)
uavcam.vflip=True
uavcam.start_preview()
uavcam.capture("/home/pi/Downloads/TestCamShoot.jpg") #this photo saved in the default

#script location
uavcam.start_recording("/home/pi/Downloads/TestCamVid.h264")
time.sleep(70) #Video will record for 20 seconds
uavcam.stop_recording()
#cd Documents
#omxplayer "videofilename"
#use omxplayer to play the h264 video 

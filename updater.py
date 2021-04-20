#!/usr/bin/python
# -*- coding:utf-8 -*-import sys
#import sys
#sys.path.insert(1, "~pi/lib") # Adds lib folder in this directory to sys

import logging
import epd2in7
from PIL import Image,ImageDraw,ImageFont
from gpiozero import Button
from signal import pause
import socket
import time

import requests
import json
import time
import os


def printToDisplayHeadline(string1):
    global draw, font1, font2


#     draw = ImageDraw.Draw(HBlackImage) # Create draw object and pass in the image layer we want to work with (HBlackImage)
#     font1 = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSans.ttf', 20) # Create our font, passing in the font file and font size
#     font2 = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSans.ttf', 15) # Create our font, passing in the font file and font size

    draw.text((7, 46), string1, font = font1, fill = 0)
    epd.display(epd.getbuffer(HBlackImage))

def printToDisplayNextLine(linenr, string1): 
            
    draw.text((25, 80+((linenr - 1)*15)), string1, font = font2, fill = 0)
    epd.display(epd.getbuffer(HBlackImage))

    
def getIPv4():
    global ipv4_address

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    ipv4_address = IP


#initialize
logging.basicConfig(level=logging.DEBUG)

epd = epd2in7.EPD() # get the  display
epd.init()           # initialize the display
print("Clear...")    # prints to console, not the display, for debugging
epd.Clear()      # clear the display
#create object for displaying text and images
HBlackImage = Image.new('1', (epd2in7.EPD_HEIGHT, epd2in7.EPD_WIDTH), 255)  # 264*179
draw = ImageDraw.Draw(HBlackImage) # Create draw object and pass in the image layer we want to work with (HBlackImage)
font1 = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSans.ttf', 18) # Create our font, passing in the font file and font size
font2 = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSans.ttf', 13) # Create our font, passing in the font file and font size


#display update message
printToDisplayHeadline('Welcome to project Copernicus')

#Init global vars
ipv4_address = ""

#sleep 30 secs before starting to wait for network connectivity
printToDisplayNextLine(1,'Searching for network')
getIPv4()
while (ipv4_address == '127.0.0.1'):
    print("Network not found, retry")
    printToDisplayNextLine(2,'Network not found, retrying.')
    getIPv4()    
else:
    print("Ready, network found")
    printToDisplayNextLine(2,'Network found at '+ ipv4_address)
    printToDisplayNextLine(3,'Performing updates')



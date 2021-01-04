#!/usr/bin/python
# -*- coding:utf-8 -*-import sys
#import sys
#sys.path.insert(1, "~pi/lib") # Adds lib folder in this directory to sys

import logging
import epd2in7b_V2
from PIL import Image,ImageDraw,ImageFont
from gpiozero import Button
from signal import pause
import socket
import time

import requests
import json
import time


#font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)

def printToDisplay3lines(string1, string2, string3):
    HBlackImage = Image.new('1', (epd2in7b_V2.EPD_HEIGHT, epd2in7b_V2.EPD_WIDTH), 0)  # 264*179
    HRedImage = Image.new('1', (epd2in7b_V2.EPD_HEIGHT, epd2in7b_V2.EPD_WIDTH), 0)  # 264*179

    draw = ImageDraw.Draw(HRedImage) # Create draw object and pass in the image layer we want to work with (HBlackImage)
    font1 = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSans.ttf', 20) # Create our font, passing in the font file and font size
    font2 = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSans.ttf', 11) # Create our font, passing in the font file and font size

#    draw.text((10, 0), string, font = font24, fill = 0)
    draw.text((25, 29), string1, font = font1, fill = 255)
    draw.text((25, 78), string2, font = font1, fill = 255)
    draw.text((25, 127), string3, font = font1, fill = 255)
    draw.text((timeXpos, timeYpos), lastRefreshTime, font = font2, fill = 255)
    draw.text((ipXpos, ipYpos), ipv4_address, font = font2, fill = 255)

    epd.display(epd.getbuffer(HRedImage), epd.getbuffer(HRedImage))

def printToDisplay2lines(string1, string2):
    HBlackImage = Image.new('1', (epd2in7b_V2.EPD_HEIGHT, epd2in7b_V2.EPD_WIDTH), 0)  # 298*126
    HRedImage = Image.new('1', (epd2in7b_V2.EPD_HEIGHT, epd2in7b_V2.EPD_WIDTH), 0)  # 298*126

    draw = ImageDraw.Draw(HRedImage) # Create draw object and pass in the image layer we want to work with (HBlackImage)
    font1 = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSans.ttf', 20) # Create our font, passing in the font file and font size
    font2 = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSans.ttf', 10) # Create our font, passing in the font file and font size

    draw.text((25, 46), string1, font = font1, fill = 255)
    draw.text((25, 112), string2, font = font1, fill = 255)
    draw.text((timeXpos, timeYpos), lastRefreshTime, font = font2, fill = 255)
    draw.text((ipXpos, ipYpos), ipv4_address, font = font2, fill = 255)

    epd.display(epd.getbuffer(HRedImage), epd.getbuffer(HRedImage))


def handleKey1Press():
    global buttonPressed
    print('Key1 pressed')
    printToDisplay2lines('ETH value: '+eth_amount,'USD value: $'+usd_amount)
    buttonPressed = 1

def handleKey2Press():
    global buttonPressed
    print('Key2 pressed')
    printToDisplay2lines('ETH value: '+eth_amount,'EUR value: €'+eur_amount)
    buttonPressed = 2

def handleKey3Press():
    global buttonPressed
    print('Key3 pressed')
    printToDisplay3lines('ETH value: '+eth_amount,'USD value: $'+usd_amount, 'EUR value: €'+eur_amount)
    buttonPressed = 3

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

def refreshValues():
    global eth_amount
    global usd_amount
    global eur_amount
    global buttonPressed
    global lastRefreshTime

    #call the api for the Copernicus Value
    response = requests.get('http://isitcopernicus.art:3000/api/v1.0/price')
    print(response.text)

    #Process api result
    data = json.loads(response.text)
    txt = "{:,}"
    eth_amount = txt.format(float(data[0]["amount"]))
    usd_amount = txt.format(float(data[1]["amount"]))
    eur_amount = txt.format(float(data[2]["amount"]))
    #Set last refresh variable
    lastRefreshTime = time.strftime("%b %d %Y %H:%M")

    #get the ip address to show on the display for ssh or vnc connections
    getIPv4()

    if (buttonPressed == 1):
        print('refresh key 1')
        handleKey1Press()
    elif (buttonPressed == 2):
        print('refresh key 2')
        handleKey2Press()
    elif (buttonPressed == 3):
        print('refresh key 3')
        handleKey3Press()

#initialize
logging.basicConfig(level=logging.DEBUG)

epd = epd2in7b_V2.EPD() # get the  display
epd.init()           # initialize the display
print("Clear...")    # prints to console, not the display, for debugging
epd.Clear()      # clear the display

#Init global vars
eth_amount = 0
usd_amount = 0
eur_amount = 0
buttonPressed = 3
lastRefreshTime = 0
timeXpos = 170
timeYpos = 159
ipXpos = 10
ipYpos = 159
ipv4_address = ""

#Assign buttos to gpio pins
key1 = Button(5) #set key1
key2 = Button(6) #set key2
key3 = Button(13) #set key3
key4 = Button(19) #set key4


#main program
key1.when_pressed = handleKey1Press
key2.when_pressed = handleKey2Press
key3.when_pressed = handleKey3Press
key4.when_pressed = refreshValues

#sleep 30 secs before starting
time.sleep(30)

refreshValues()

pause()

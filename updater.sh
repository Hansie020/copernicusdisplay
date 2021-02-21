#!/bin/bash
/usr/bin/python3 /home/pi/copernicusdisplay/updater.py
cd /home/pi/copernicusdisplay
git pull
/usr/bin/python3 /home/pi/copernicusdisplay/copernicusdisplay.py

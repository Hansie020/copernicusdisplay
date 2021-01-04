#!/bin/sh
# installer.sh will install the necessary packages to get the e-Paper HAT
# waveshare 2.7inch e-Paper HAT V2
# up and running for displaying the Copernicus wallet value

#cd ~
#mkdir isitcopernicus
#cd isitcopernicus

#install BCM2835 libraries
wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.60.tar.gz
tar zxvf bcm2835-1.60.tar.gz
cd bcm2835-1.60/
sudo ./configure
sudo make
sudo make check
sudo make install

#install wiringPi libraries
sudo apt-get install wiringpi

# Install python libraries
PACKAGES="python3-pip python3-pil python3-numpy"
apt-get update
apt-get upgrade -y
apt-get install $PACKAGES -y
sudo pip3 install RPi.GPIO
sudo pip3 install spidev

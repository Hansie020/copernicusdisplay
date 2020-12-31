#!/bin/sh
# installer.sh will install the necessary packages to get the e-Paper HAT
# waveshare 2.7inch e-Paper HAT V2
# up and running for displaying the Copernicus wallet value

# Install packages
PACKAGES="python3-pip python3-pil python3-numpy"
apt-get update
apt-get upgrade -y
apt-get install $PACKAGES -y
sudo pip3 install RPi.GPIO


# copernicusdisplay

**Installation instructions:**
1. Attach the [2.7inch e-Paper HAT from waveshare](https://www.waveshare.com/product/displays/e-paper/epaper-2/2.7inch-e-paper-hat.htm) to a raspberry pi
2. Create a fresh Pi OS sd-card (with desktop for novice users), boot the Pi with it whilst connected to a display, keyboard and mouse and setup the raspberry pi to your needs. Make sure it is connected to the internet.
1. Open the raspberry pi configuration tool and enable the SPI interface and optional the SSH and or VNC interface
1. Open a terminal on your raspberry pi (using ssh or a desktop interface) and run the commands below
```
    git clone https://github.com/Hansie020/copernicusdisplay.git
    cd copernicusdisplay
    chmod u+x install.sh
    sudo ./install.sh
```
Check if the display is working:
```
    sudo python3 copernicusdisplay.py
```
The display should blink and shows three lines of text depicting the value of the copernicus vault in ETH, USD and EUR. If not, log an issue in this github after checking if all the above is done correctly.

When the display shows the correct data, you can install copernicusdisplay as a systemd service using the following commands:
```
    sudo cp copernicusdisplay.service /etc/systemd/system
    sudo systemctl enable copernicusdisplay.service
    sudo systemctl start copernicusdisplay
```
The raspberry pi will update itself with the latest version of the master branch at boottime.

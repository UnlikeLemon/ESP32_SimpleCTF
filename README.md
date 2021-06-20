This simple CTF is a little project im working on.
Its nothing special and it started because i wan't to
sharpen my networking skills and so i decided to turn it
into a fun and quick challenge.


All the tools will be listed in this README.md
along with a tutorial on how to make it work:


#Installization

esptool.py
ampy
screen

~>sudo apt-get install screen

~>sudo pip install adafruit-ampy

~>sudo pip3 install esptool


Screen will be used to get an interface from the ESP
Ampy is going to be used to upload the main.py file in the ESP
esptool will be used to upload the firmware to the ESP and allow it to run micropython


#Uploading firmware

~>sudo esptool.py --port [PORT] --baud [BAUD] erase_flash

e.g
~>sudo esptool.py --port /dev/ttyUSB0 --baud 115200 erase_flash

and after that:

~>sudo esptool.py --port /dev/ttyUSB0 --baud 115200 write_flash --flash_size=detect 0 firmware.bin

#Uploading the main.py

~>sudo ampy --port [PORT] --baud [BAUD] put main.py

~>sudo ampy --port /dev/ttyUSB0 --baud 115200 put main.py

And that's it!

[[All thats left is to get an interface with:]]

~>sudo screen [PORT] [BAUD]

~>sudo screen /dev/ttyUSB0 115200

Note: In case that you see gibberish in your screen or nothing, restart the ESP from its reset button and 
it should be working



# What this is.

This repository is a simple project i've been working on. I personally use it to sharpen my network skills along with challenging myself with coding. Thought to share this cause it might seem helpfull to some.

# How do i setup it?
---

## Manual Setup

So, for starters we need to download the list of tools that will be needed so we can work.

Tool list:
- [ ] adafruit-ampy
- [ ] esptool.py
- [ ] screen

## How do we install them?

**adafruit-ampy**

>pip3 install adafruit-ampy

**esptool.py**
>pip3 install esptool

**screen**
>sudo apt-get install screen


After all our tools are ready, we need to flash our ESP.

---

## Flashing and uploading firmware.

>esptool.py --port [PORT] --baud [BAUD] erase_flash

I set the port to `/dev/ttyUSB0` and baud at `115200` but it's mostly depending on your machine.

Next, we need to upload the firmware to the ESP.

>esptool.py --port [PORT] --baud [BAUD] write_flash --flash_size=detect 0 firmware.bin

After we've finished with that, we use screen to see if we did things correctly.

>sudo screen [PORT] [BAUD]

Note: If all you see is a black screen, try pressing the RST button on your ESP.

---

## Ampy

Now we need a way to upload/remove files to the ESP, and we do that with ampy.

>sudo ampy --port [PORT] --baud [BAUD] put main.py


What this will do is put `main.py` from our machine to the ESP

We can also do

>sudo ampy --port [PORT] --baud [BAUD] ls

to list all the files in the ESP and

>sudo ampy --port [PORT] --baud [BAUD] rm file.py

to remove something.

---

## How the challenge works and how to solve it.
When you plug-in the ESP and it's powered, it will start by generating a password and an AP (Access Point) with that random password. The password is only digits to make it easier with cracking. I also made it print the first four digits of the password along with its length and its IP to make it a bit easier. The password is also printed and i'll explain why later. Once you crack the password and manage to enter the network you need to find the web page that is running in a random port. I haven't finished it yet so the challenge stops there.

### Cracking the password.

How i do it is simply open `airodump-ng` and connect to the AP with my phone so i can grab the handshake. Once i get it i go to `aircrack-ng`, make a custom wordlist with the 4 digits that have been given to me and wait for the password to crack.

### The web part of the challenge is not finished yet.


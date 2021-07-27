import subprocess, sys, os


try:
    device = sys.argv[1]
    firmware_file = sys.argv[2]
except:
    print("Device not provided!\nExample: python3 autobuild.py /dev/ttyUSB0 firmware.bin")
    quit()

def install_dependecies():
    try:
        print("Donwloading and installing screen")
        subprocess.call("sudo apt-get install screen", shell=True)
        print("Downloading and installing ampy")
        subprocess.call("pip3 install adafruit-ampy", shell=True)
        print("Downloading and installing esptool")
        subprocess.call("pip3 install esptool", shell=True)
    except:
        print("Ooops, something went wrong")


def flash_firm(port, baud):
    try:
        print("Erasing firmware")
        subprocess.call(f"sudo esptool.py --port {port} --baud {baud} erase_flash")
    except:
        print("Ooops, something went wrong")


def upload_firmware(port, baud, firmware):
    try:
        print(f"Flashing device at port {port}")
        subprocess.call(f"sudo esptool.py --port {port} -- baud {baud} write_flash --flash_size=detect 0 {firmware}")
    except:
        print("Ooops, something went wrong")

def print_menu():
    print("Flash firmware | 1")
    print("Install dependecies | 2")
    print("Upload firmware | 3")
    print("Upload main.py | 4")

def upload_main_file(port, baud):
    try:
        print("Uploading file to device")
        subprocess.call(f"sudo ampy --port {port} --baud {baud} rm main.py")
        subprocess.call(f"sudo ampy --port {port} --baud {baud} put main.py")
    except:
        print("Ooops, something went wrong")

def main():
    print_menu()
    choice = int(input("Enter your choice: "))
    baud = 115200
    if choice == 1:
        flash_firm(device, baud)
    elif choice == 2:
        install_dependecies()
    elif choice == 3:
        upload_firmware(device, baud, firmware_file)
    elif choice == 4:
        upload_main_file(device, baud)
    else:
        print("Option unrecognized")

main()
import network
from machine import *
import random, time
import usocket as socket

s = socket.socket()
ap = network.WLAN(network.AP_IF)
bars = "-" * 31
congratulations_msg = bars + "\nCongratulations but my website is the most secure thing that you probably across,\n so highly unlikely that you will get past my ultimate secure login page :)\n"

def html():
    website = """<html>
    <title>Testing 123</title>
    <p>This is a test</p>
    <p>Parameter test</p>
    <b>"""+bars+"""</b>
    </html>"""
    return website

def forbiden_site():
    html = """<html>
    <title> A different website ;)</title>
    <p>It seems that you are using a forbidden User-Agent</p>
    <p>It is not allowed!</p>
    </html>"""
    return html

def create_pass():
    password = ""
    nums = 9
    for i in range(3):
        x = random.getrandbits(nums)
        password = password + str(x)
    print("\n{ + } Password Generated! { + }")
    print(bars)
    return password

def create_AP(name, passwd):
    ap.active(1)
    ap.config(essid=name, password=passwd)
    print("\n{ + } Network Created! { + }")
    print(bars)

def sockets():
    ip = ap.ifconfig()[0]
    s.bind((ip, 80))
    s.listen(5)
    while True:
        c, addr = s.accept()
        print("Got a connection from: " + str(addr))
        req = c.recv(1024)
        resp = html()
        c.send(resp)
        c.close()

def start():
    password = create_pass()
    passwd = str(password)
    create_AP("Try to crack me ;)", str(123456789)) #<-- Change the password after debugging
    print("\n{ + } Let the Cracking Begin! { + }")
    print(bars)
    hint = hints(password)
    pass_len = hint[1]
    digits = hint[0]
    ip = hint[2]
    print("Hints: \nFirst 4 Digits: " + str(digits) + "\nLength: " + str(pass_len))
    print("Password: " + passwd)
    print("IP: " + ip)
    sockets()

def hints(passwd):
    x = passwd
    length = len(x)
    length_y = 4
    asterisks = (length - length_y) * "*"
    y = ""
    for i in range(0, 4):
        y = y + x[i]
    ip = ap.ifconfig()[0]

    return y + asterisks, length, ip


start()



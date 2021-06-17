import network
import random
import usocket as socket

#Importing all the libraries that are needed

s = socket.socket()
ap = network.WLAN(network.AP_IF)
#Initializing the AP(Access Point) and the socket

bars = "-" * 31 #Bars, mostly for better appearance
congratulations_msg = bars + "\nCongratulations but my website is the most secure thing that you probably across,\n so highly unlikely that you will get past my ultimate secure login page :)\n"
#Congratulations message, a part of the web challenge
#----Not developed yet----

def html():
    website = """<html>
    <title>Testing 123</title>
    <p>This is a test</p>
    <p>Parameter test</p>
    <b>"""+bars+"""</b>
    </html>"""
    return website

#Function that returns a really simple website

def forbiden_site():
    html = """<html>
    <title> A different website ;)</title>
    <p>It seems that you are using a forbidden User-Agent</p>
    <p>It is not allowed!</p>
    </html>"""
    return html
#Same function as above, different cause its part of the challenge

def create_pass():
    password = ""
    nums = 9
    for i in range(3):
        x = random.getrandbits(nums)
        password = password + str(x)
    print("\n{ + } Password Generated! { + }")
    print(bars)
    return password
#Function that creates and returns the password

#Function that thakes a name/password parameter and uses them to create an AP with these credentials
def create_AP(name, passwd):
    ap.active(1)
    ap.config(essid=name, password=passwd, authmode=2)
    print("\n{ + } Network Created! { + }")
    print(bars)

#Socket function, acts as a listener when a request is made at port 80 and returns the website, along with printing the response for troubleshooting
def sockets():
    ip = ap.ifconfig()[0]#ap.ifconfig returns a list of stats from the current network so that we don't have to guess and change the IP everytime
    s.bind((ip, 80))#Bind to the IP and listen to port 80
    s.listen(5)
    while True:
        c, addr = s.accept()
        print("Got a connection from: " + str(addr))
        req = c.recv(1024)
        resp = html()
        c.send(resp)
        c.close()

#Main function that starts everything
def main():
    password = str(create_pass())
    create_AP("Try to crack me ;)", str(123456789)) #<-- Change the password after debugging
    print("\n{ + } Let the Cracking Begin! { + }")
    print(bars)
    hint = hints(password)
    pass_len = hint[1]
    digits = hint[0]
    ip = hint[2]
    print("Hints: \nFirst 4 Digits: " + str(digits) + "\nLength: " + str(pass_len))
    print("Password: " + password)
    print("IP: " + ip)
    sockets()

#Hints function, takes the password and returns the first 4 digits, the rest are turned into asterisks
def hints(passwd):
    x = passwd
    length = len(x)
    length_y = 4
    asterisks = (length - length_y) * "*"
    y = ""
    for i in range(0, 4):
        y += x[i]
    ip = ap.ifconfig()[0]
    return y + asterisks, length, ip


main()



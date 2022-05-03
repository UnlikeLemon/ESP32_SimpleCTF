import network
import urandom as random
import usocket as socket
#Libraries needed for the challenge


#------Variables-------
s=socket.socket()
ap=network.WLAN(network.AP_IF)#Initializing the ESP as an Access Point (AP)

bars="-"*30
congrats_msg="\nCongratulations,brotha but my website is the most secure thing! Good luck"
forbidden_user_agents=["Firefox","Curl","firefox","curl","redmi","Redmi"]
ap_name="Try to crack me ;)"

#Website that will be shown if the user-agent filter gets bypassed
def default_website():
    website="""<html>
    <title>Hello User</title>
    <p><b1>Hello mate</b1></p>
    <p>Parameter_test: {bars}</p>
    </html>""".format(bars=bars)
    return website

#Website that will be shown if the user agent filter isn't bypassed
def forbidden_site():
    website="""<html>
    <title> A different website ;)</title>
    <p>It seems that you are using a forbidden User-Agent</p>
    <p>It is not allowed!</p>
    <p>{bars}
    Testing parameters and sh..
    </html>""".format(bars=bars)
    return website

#Function generating and returing a password of numbers with a length of 8
def password_generator():
    password=""
    for i in range(0,8):
        password+=str(random.getrandbits(9))[0]
    print("\n{ + } Password Generated! { + }\n"+bars)
    return password

#Function initializing the AP, essid is the name of the AP,
#password is password and authmode is the security protocol
#that will be used
def ap_generator(name,password):
    ap.active(1)
    ap.config(essid=name,password=password, authmode=3)
    print("{ + } Network Created! { + }\n"+bars)

#Function checking each request, acting as a user-agent filter
def user_agent_filter(req):
    for i in forbidden_user_agents:
        if str(i) in str(req):return 1
        else: return 0

#Sockets Function
#Binds to the IP of the ESP and port 80
#Acts as a web server, accordingly with the user-agent filter
def sockets():
    ip=ap.ifconfig()[0]
    s.bind((ip,80))
    s.listen(5)
    while True:
        c,addr=s.accept()
        print(f"Connection recieved: {addr}")
        r=str(c.recv(1024))
        check=user_agent_filter(r)
        if check:
            resp=forbidden_site()
            c.send(resp)
            c.close()
        else:
            resp=default_website()
            c.send(resp)
            c.close()

#Hint function, providing the IP/Length of the password
#And the first 4 digits of it, just for the sake of smaller wordlists
#when cracking
def hint_func(password):
    password=str(password)
    x=len(password)
    l=4
    a=(x-l)*"*"
    y=""
    for i in range(0,4): y+=password[i]
    ip=ap.ifconfig()[0]
    return y+a,l,ip
#main function
# Self-explanatory :/
def main():
    password=password_generator()
    ap_generator(ap_name,password)
    print("{ + } Challenge Started, Good Luck! { + }\n"+bars)
    hints=hint_func(password)
    first_digits,pass_len,ip=hints[0],hints[1],hints[2]
    print(f"Hints:\nFirst 4 Digits: {first_digits}\nLength:{pass_len}\nPassword: {password}\nIP: {ip}")
    sockets()

main()
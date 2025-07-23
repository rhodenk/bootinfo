from os.path import exists
import os
import json
import urllib, http.client
import netifaces
import time
import publicIP

def pushover(pushoverSettings, msg, sound="gamelan"):
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
                urllib.parse.urlencode({
                    "token": pushoverSettings["token"],
                    "user": pushoverSettings["user"],
                    "message": msg,
                    "sound": sound,
                }), {"Content-type": "application/x-www-form-urlencoded"})
    r = conn.getresponse()
    print("PUSHOVER", f"'{msg}' sent. Response = {r.read()}")


def privateIPs():
    ips = ""
    interfaces = [i for i in netifaces.interfaces() if i.startswith("eth") or i.startswith("wlan")]
    for interface in interfaces:
        ips += (f"Interface: {interface}") + "\n"

        addresses = netifaces.ifaddresses(interface)
        if 2 in addresses:
            ips += str(addresses[2]) + "\n"

    return ips



############

print("Started bootinfo")

print("waiting 30 seconds for network to come up")
time.sleep(30)

if exists("./pushover.json"):
    with open("./pushover.json") as myFile:
        pushoverSettings = json.load(myFile)
        print("pushover credentials loaded")

        msg = "DEVICE BOOT" + "\n\n"
        msg += f"Hostname: {os.uname()[1]}\n\n"
        msg += f"Public IP: {publicIP.get()}\n\n"
        msg += f"Private IP(s):\n{ privateIPs() }\n"

        if exists("./custommessage.txt"):
            f = open("./custommessage.txt", "r")
            msg += f.read() + "\n"
            f.close()

        print(f"Sending pushover message : {msg}")
        pushover(pushoverSettings, msg)
        print("Pushover message sent")

else:
    print("bootinfo could not load pushover credentials from 'pushover.json'")
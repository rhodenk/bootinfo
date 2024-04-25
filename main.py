from os.path import exists
import os
import json
import urllib, http.client
import netifaces


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

print("Starting bootinfo")

if exists("./pushover.json"):
    with open("./pushover.json") as myFile:
        pushoverSettings = json.load(myFile)

        msg = "DEVICE BOOT" + "\n\n"
        msg += f"Hostname: {os.uname()[1]}\n\n"
        msg += f"Private IP(s):\n{ privateIPs() }\n"

        if exists("./custommessage.txt"):
            f = open("./custommessage.txt", "r")
            msg += f.read() + "\n"
            f.close()

        print(f"Message : {msg}")
        pushover(pushoverSettings, msg)


else:
    print("bootinfo could not load pushover credentials from 'pushover.json'")
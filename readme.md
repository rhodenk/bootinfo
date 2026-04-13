# bootinfo sent to pushover client (pushover account needed)

## Clone repo
clone the repo into `/home/pi` path


## install dependencies
UBUNTU:
```
sudo apt install netifaces
```
DEBIAN
```
sudo apt install python3-netifaces
```

## Systemd
install service by copying systemd unit file:
```
cp bootinfo.service /lib/systemd/system/bootinfo.service
```

enable the service
```
sudo systemctl daemon-reload
sudo systemctl enable bootinfo.service
sudo systemctl daemon-reexec
```

## bootinfo.service
If you're not using the "pi" user, update the paths to reflect your chosen path


## Pushover creds
create pushover creds file `pushover.json`:
```
{
    "token": "your_token",
    "user": "your_user"
}
```

## custom message
add/update custom message `custommessage.txt`.  This should be in plaintext format.  Newlines are recognised without needing `\n`


## other stuff
consider updating `/etc/motd` for terminal welcome message to explain purpose of device
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
sudo systemctl enable Garage2.service
sudo systemctl daemon-reexec
```

## Pushover creds

create pushover creds file `pushover.json`:
```
{
    "token": "your_token",
    "user": "your_user"
}
```

## custom message

update custom message `custommessage.txt`
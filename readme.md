#bootinfo sent to pushover client (pushover account needed)

clone the repo into `/home/pi` path

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

create pushover creds file:
```pushover.json
{
    "token": "your_token",
    "user": "your_user"
}
```

update custom message `custommessage.txt`
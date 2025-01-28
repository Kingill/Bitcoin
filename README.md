# Bitcoin

https://bitcoin.org/en/full-node#other-linux-gui
```
bitcoind -daemon
bitcoin-cli stop
```

Service bitcoind
```
Edit /usr/lib/systemd/system/bitcoind.service
systemctl start bitcoind.service
systemctl stop bitcoind.service
systemctl status bitcoind.service

systemctl enable bitcoind.service
Created symlink /etc/systemd/system/multi-user.target.wants/bitcoind.service → /usr/lib/systemd/system/bitcoind.service.
```

Journal de log
```
journalctl -xeu bitcoind.service
```

# Bitcoin

https://bitcoin.org/en/full-node#other-linux-gui

Install
```
tar xzf bitcoin-27.0-x86_64-linux-gnu.tar.gz
sudo install -m 0755 -o root -g root -t /usr/local/bin bitcoin-27.0/bin/*
```

Daemon
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

Log
```
journalctl -xeu bitcoind.service
```

Check
```
bitcoin-cli -rpcuser=username -rpcpassword=password -getinfo
```

After it starts, you may find the following commands useful for basic interaction with your node: getblockchaininfo, getnetworkinfo, getnettotals, getwalletinfo, stop, and help.

For example, to safely stop your node, run the following command:
```
bitcoin-cli stop
```

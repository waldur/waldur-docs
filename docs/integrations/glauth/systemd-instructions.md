# Systemd setup for glauth and config refresher

Prerequisites:

1. Ensure wget is installed to a target machine as refreshing script uses it;
2. Install glauth binary to `/usr/bin/glauth` upon staring glauth service, e.g.
[glauth v2.3.0](https://github.com/glauth/glauth/releases/download/v2.3.0/glauth-linux-amd64).

## Refresher service

Copy the files from this repository to a corresponding paths on the target host:

```bash
mkdir /etc/glauth
cp systemd-conf/refresher/preconfig.cfg.template /etc/glauth/preconfig.cfg.template
cp systemd-conf/refresher/refresher.env /etc/glauth/refresher.env
cp systemd-conf/refresher/refresh-glauth-config.sh /usr/sbin/refresh-glauth-config.sh
cp systemd-conf/refresher/refresh-glauth-config.service /etc/systemd/system/refresh-glauth-config.service
```

Update systemd daemon configs and start and enabled the service:

```bash
systemctl daemon-reload
systemctl start refresh-glauth-config
systemctl enable refresh-glauth-config
```

After some time, you should be able to check the prepared config file in `/etc/glauth/config.cfg`

## Glauth service

Ensure glauth binary is installed in `/usr/bin/glauth` and perform the same steps for the glauth service:

```bash
cp systemd-conf/glauth/glauth.service /etc/systemd/system/glauth.service
systemctl daemon-reload
systemctl start refresh-glauth-config
systemctl enable refresh-glauth-config
```

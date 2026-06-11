# Systemd setup for glauth and config refresher

Prerequisites:

1. Ensure Python 3.9+ and `pip` are installed on the target machine, then install the refresher dependencies:

   ```bash
   pip3 install -r refresher/requirements.txt
   ```

2. Install the glauth binary to `/usr/bin/glauth`. Use the same version as pinned by `GLAUTH_VERSION` in the [Dockerfile](../Dockerfile), e.g.:

   ```bash
   wget -O /usr/bin/glauth https://github.com/glauth/glauth/releases/download/GLAuth-v2.5.0/glauth-linux-amd64
   chmod +x /usr/bin/glauth
   ```

## Refresher service

Copy the files from [this repository](https://github.com/waldur/glauth) to the corresponding paths on the target host:

```bash
mkdir /etc/glauth
cp refresher/preconfig.cfg.template /etc/glauth/preconfig.cfg.template
cp systemd/refresher.env.example /etc/glauth/refresher.env
cp refresher/refresh-glauth-config.py /usr/sbin/refresh-glauth-config.py
cp systemd/refresh-glauth-config.service /etc/systemd/system/refresh-glauth-config.service
```

Update the `.env` file for the refresher service, i.e. `/etc/glauth/refresher.env`:

```env
WALDUR_URL=https://waldur.example.com/api/
WALDUR_TOKEN=891a3dee2b905d08ed672d407308020d241c4f31
WALDUR_OFFERING_UUID=94dd1cec1f3940ef017e
WALDUR_API_VERIFY_TLS=false
LDAP_ADMIN_UIDNUMBER=4000
LDAP_ADMIN_PGROUP=4000
LDAP_ADMIN_USERNAME=admin
LDAP_ADMIN_PASSWORD=Adm1n!
LDAP_ADMIN_EMAIL=admin@example.com
```

Update systemd daemon configs and start and enable the service:

```bash
systemctl daemon-reload
systemctl start refresh-glauth-config
systemctl enable refresh-glauth-config
```

After some time, you should be able to check the prepared config file in `/etc/glauth/config.cfg`

## Glauth service

Ensure the glauth binary is installed in `/usr/bin/glauth` and perform the same steps for the glauth service:

```bash
cp systemd/glauth.service /etc/systemd/system/glauth.service
systemctl daemon-reload
systemctl start glauth
systemctl enable glauth
```

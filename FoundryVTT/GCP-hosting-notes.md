### SSL Cert from Let's Encrypt
```
sudo apt install snapd
sudo snap install core; sudo snap refresh core
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot
```

#### In the Google Cloud Console edit the virtual machine config and allow HTTP

```
sudo certbot certonly --standalone

sudo cp /etc/letsencrypt/live/<your fully qualified domainname>/fullchain.pem ~/foundrydata/
sudo cp /etc/letsencrypt/live/<your fully qualified domainname>/privkey.pem ~/foundrydata/
sudo chown <the username running your Foundry VTT server> privkey.pem 
```

#### Add the full path for each cert to the setup entries for SSL

#### Restart your server

(node </path/to/>/foundryvtt/resources/app/main.js --datapath=</path/to/>/foundrydata &)

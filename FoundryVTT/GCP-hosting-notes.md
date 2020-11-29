### SSL Cert from Let's Encrypt
Let's Encrypt recommends running a command from the shell on the server that you want to
generate a cert for.  Follow the instructions at 
https://certbot.eff.org/lets-encrypt/debianbuster-other and use `None of the above` and 
the operating system you are using on GCP to get custom instructions.

These are the commands I ran on my Debian Buster server:
```
sudo apt install snapd
sudo snap install core; sudo snap refresh core
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot
```

#### In the Google Cloud Console edit the virtual machine config and allow HTTP

```
sudo certbot certonly --standalone
```
At this point you should see that a cert and private key have been created, and the 
paths for the files.  If you are running Foundry VTT as a non-root user you will have
to copy the files from where they are placed by certbot into a directory that the user
running Foundry VTT can read:

```
sudo cp /etc/letsencrypt/live/<your fully qualified domainname>/fullchain.pem ~/foundrydata/
sudo cp /etc/letsencrypt/live/<your fully qualified domainname>/privkey.pem ~/foundrydata/
sudo chown <the username running your Foundry VTT server> ~/foundrydata/privkey.pem 
```

#### Add the full path for each cert to the setup entries for SSL

#### Restart your server

(node </path/to/>/foundryvtt/resources/app/main.js --datapath=</path/to/>/foundrydata &)

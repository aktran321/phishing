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

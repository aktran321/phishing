import subprocess
import os

def run_command(cmd):
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"Command failed: {cmd}")
    else:
        print(f"Success: {cmd}")
run_command("sudo apt update")
run_command("sudo apt upgrade -y")
run_command("sudo apt install -y unzip")

domain = input("Enter your domain (e.g., login.example.com): ").strip()

env = os.environ.copy()
env["DOMAIN"] = domain
# Create Gophish and Evilginx directories and retrieve files
run_command("mkdir evilginx")
run_command("mkdir gophish")
run_command("wget https://github.com/gophish/gophish/releases/download/v0.12.1/gophish-v0.12.1-linux-64bit.zip")
run_command("wget https://github.com/kgretzky/evilginx2/releases/download/v3.3.0/evilginx-v3.3.0-linux-64bit.zip")
run_command("unzip gophish-v0.12.1-linux-64bit.zip -d gophish")
run_command("unzip evilginx-v3.3.0-linux-64bit.zip -d evilginx")
run_command("mv gophish-v0.12.1-linux-64bit.zip gophish")
run_command("mv evilginx-v3.3.0-linux-64bit.zip evilginx")


# Use Certbot and create Certificate and Keys
run_command("sudo apt install -y certbot")
certbot_cmd=f"sudo certbot certonly -d {domain} --manual --preferred-challenges dns --register-unsafely-without-email"
run_command(certbot_cmd)


subprocess.run(["python3", "gophish_config.py"], env=env)

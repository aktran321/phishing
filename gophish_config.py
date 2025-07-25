import json
import os

domain = os.getenv("DOMAIN")
if not domain:
    raise Exception("DOMAIN environment variable not set")

with open("gophish/config.json", "r") as f:
    config = json.load(f)
    
config["admin_server"]["listen_url"] = "0.0.0.0:3333"
config["phish_server"]["listen_url"] = "0.0.0.0:443"
config["phish_server"]["use_tls"] = True
config["phish_server"]["cert_path"] = f"/etc/letsencrypt/live/{domain}/fullchain.pem"
config["phish_server"]["key_path"] = f"/etc/letsencrypt/live/{domain}/privkey.pem"

with open("gophish/config.json", "w") as f:
    json.dump(config, f, indent=4)

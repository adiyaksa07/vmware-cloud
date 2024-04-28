import os
import requests
from env_control import * 

def server_check_power(pc):
    headers = { 
        'Accept': 'application/vnd.vmware.vmw.rest-v1+json',
        'Authorization': os.getenv("AUTH")
    } 
    status_server = requests.get(f"http://127.0.0.1:8697/api/vms/{pc}/power", headers=headers)
    if status_server.json()['power_state'] == 'poweredOff': 
        return False
    return True
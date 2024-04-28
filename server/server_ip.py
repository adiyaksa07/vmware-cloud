import os
import json
import requests
from env_control import * 
def get_ip(pc):
    headers = { 
        'Accept': 'application/vnd.vmware.vmw.rest-v1+json',
        'Authorization': os.getenv("AUTH")
    } 
    restrictions_information_server = requests.get(f"http://127.0.0.1:8697/api/vms/{pc}/ip", headers=headers)
    return restrictions_information_server.json()

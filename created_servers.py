import requests
import json

from datetime import timedelta
from flask import Blueprint, render_template, session, redirect, url_for, request
from database.db import mysql
from index import os
from server.server_check_power import server_check_power

server_for_copy = os.getenv("SERVER_1")

created_server = Blueprint("created_servers",  __name__)

@created_server.route("/create/servers", methods=["GET", "POST"])
def page_created_server(): 

    """
        Renders the create server page if user is logged in and has permission to create servers.
        Allows users to create servers and updates the database accordingly.
    """

    url = "http://127.0.0.1:8697/api/vms"

    if session.get('login') == True:      
        if session.get('createdServers') == False:
            return redirect(url_for('dashboard'))

        if request.method == "POST":
            value_system = request.form.get("server")
            data_server = { 
                "name": "Server_" + session.get("username"),
                "parentId": server_for_copy
            }

            if value_system == "windows_1":
                print(server_check_power(server_for_copy))
                if server_check_power(server_for_copy): 
                    x = requests.put(f"http://127.0.0.1:8697/api/vms/{server_for_copy}/power", data="off", headers={
                        'Content-Type': 'application/vnd.vmware.vmw.rest-v1+json',
                        'Accept': 'application/vnd.vmware.vmw.rest-v1+json',
                        'Authorization': os.getenv("AUTH")
                    })
                    print(x)
                    
                x = requests.post(url, data=json.dumps(data_server), headers= {
                    'Content-Type': 'application/vnd.vmware.vmw.rest-v1+json',
                    'Accept': 'application/vnd.vmware.vmw.rest-v1+json',
                    'Authorization': os.getenv("AUTH")
                })
                
                data = x.json()
                print(data)
                try:
                    session["createdServers"] = False
                    session["server_id"] = data["id"]
                    session["baru_buat"] = True
                    session.permanent = True
                    conn = mysql.connection
                    cursor = conn.cursor()
                    cursor.execute("UPDATE user SET createdServers = %s, servers = %s WHERE username = %s", (False, data["id"], session["username"]))
                    conn.commit()
                    return redirect(url_for('dashboard'))
                except Exception as e: 
                    print(e)
                    return "The server is having problems building, please report it"      
            else: 
                return render_template("create_server.html", alert=True)

        return render_template("create_server.html")

    else: 
         return redirect(url_for('auth.login'))
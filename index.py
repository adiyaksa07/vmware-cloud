import os
import requests
from datetime import timedelta
from flask import Flask, render_template, request, session, redirect, url_for
from server.server_check_power import server_check_power
from server.server_restrictions_information import get_restrictions_information_server
from server.server_ip import get_ip
from database.db import mysql
from auth import auth_page
from created_servers import created_server

app = Flask(__name__)
app.secret_key = os.urandom(32)
app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(days=1)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'rhani_cloud'

mysql.init_app(app)

headers = { 
    'Accept': 'application/vnd.vmware.vmw.rest-v1+json',
    'Authorization': os.getenv("AUTH")
}

pc = os.getenv("PC")

@app.route("/", methods=['GET', 'POST'])
def dashboard():
    if session.get("login") == True:
       conn = mysql.connection
       cursor = conn.cursor()
       cursor.execute("SELECT createdServers FROM user WHERE username = %s", (session.get("username"), )) 
       created_server = cursor.fetchone()
       cursor.close()
       if created_server[0]: 
           session["createdServers"] = True
       else: 
           session["createdServers"] = False
       if session.get("createdServers") == True: 
            return redirect(url_for("created_servers.page_created_server"))
       else: 
            try:
                if session.get("baru_buat"): 
                    session["baru_buat"] = False
                    on = requests.put(f"http://127.0.0.1:8697/api/vms/{session.get("server_id")}/power", data="on", headers={
                        'Content-Type': 'application/vnd.vmware.vmw.rest-v1+json',
                        'Accept': 'application/vnd.vmware.vmw.rest-v1+json',
                        'Authorization': os.getenv("AUTH")
                    })
                    print(on)
                if request.method == "POST": 
                    status = request.form.get('btnserver') 
                    x = requests.put(f"http://127.0.0.1:8697/api/vms/{session.get("server_id")}/power", data=status, headers={
                        'Content-Type': 'application/vnd.vmware.vmw.rest-v1+json',
                        'Accept': 'application/vnd.vmware.vmw.rest-v1+json',
                        'Authorization': os.getenv("AUTH")
                    })
                    print(f"status = {status}")
                    print(x.json())
                return render_template('index.html', ip=get_ip(session.get("server_id")), status_power=server_check_power(session.get("server_id")), data=get_restrictions_information_server(session.get("server_id")).json())
            except Exception as e:
                print(e)  
                return "Sorry, the server is having problems, please call 089523636957."
    else: 
        return redirect(url_for("auth.login"))


app.register_blueprint(auth_page)
app.register_blueprint(created_server)


if __name__ == "__main__":
    app.run()

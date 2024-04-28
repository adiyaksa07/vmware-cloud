from datetime import timedelta
from flask import Blueprint, render_template, request, redirect, url_for, session, app
from database.db import mysql

auth_page = Blueprint('auth', __name__)

@auth_page.route('/login', methods=["GET", "POST"])
def login(): 
    if session.get("login") != True:
        if request.method == "POST":
            username = request.form.get("username")
            password = request.form.get("password")
            if not username or not password: 
                return "Please enter a username and password for login." 
            else: 
                conn = mysql.connection
                cursor  = conn.cursor()
                cursor.execute("SELECT * FROM user WHERE username = %s AND password = %s", (username, password))
                user = cursor.fetchone()
                cursor.close()
                if user:
                    session["id"] = user[0]
                    session["username"] = username
                    session["email"] = user[2]
                    session["login"] = True
                    session["createdServers"] = user[4]
                    session["server_id"] = user[5]
                    return redirect(url_for("dashboard"))
                else:
                    return render_template("login.html", alert=True)
        else:
            return render_template("login.html", alert=False)
    else:
        return redirect(url_for("dashboard"))
    
@auth_page.route("/register", methods=["GET", "POST"])
def register_page(): 
    if session.get("login") != True: 
        if request.method == "POST":
            username = request.form.get("username")
            email = request.form.get("email")
            password = request.form.get("password")
            conf_password = request.form.get("confirm_password")
            if not username or not password:
                return "Please enter a username or password for register."
            elif not email:
                return "Please enter a emaily for register."
            elif len(username) > 70 or len(email) > 70:
                return render_template("register.html", alert_length=True)
            elif password != conf_password:
                return render_template("register.html", alert_conf=True)
            else:
                conn = mysql.connection
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM user WHERE username = %s", (username,))
                existing_user = cursor.fetchone()
                cursor1 = conn.cursor()
                cursor1.execute("SELECT * FROM user WHERE email = %s", (email,))
                existing_email = cursor1.fetchone()
                cursor1.close()
                if existing_user:
                    return render_template("register.html", alert=True)
                elif existing_email: 
                    return render_template("register.html", alert_email=True)
                else:
                    cursor.execute("INSERT INTO user (username, email, password, createdServers) VALUES (%s, %s, %s, %s)", (username, email, password, True))
                    conn.commit()
                    cursor.close()
                    return redirect(url_for("auth.login"))
        else: 
            return render_template("register.html")
    else: 
        return redirect(url_for("dashboard"))

@auth_page.route("/logout")
def logout_page(): 
    session.pop('username', None)
    session.pop('login', None)
    return redirect(url_for('auth.login'))

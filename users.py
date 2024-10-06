from app import db
import errors
from flask import render_template, request, session
import re
from secrets import token_hex
from sqlalchemy.sql import text
from werkzeug.security import check_password_hash, generate_password_hash

def csrf_check():
    return session["csrf_token"] == request.form["csrf_token"]

def csrf_delete():
    del session["csrf_token"]

def csrf_new():
    session["csrf_token"] = token_hex(16)

def is_logged_in():
    return "username" in session

def login(username, first_time=False):
    if is_logged_in():
        message = "logged out and "
    else:
        message = ""
    session["username"] = username
    csrf_new()
    if first_time:
        variation = "created a new account. You are now "
    else:
        variation = ""
    message = f"Successfully {message}{variation}logged in as {username}."
    return render_template("success.html", message=message)

def login_ok(username, password):
    sql = "SELECT password_hash FROM users WHERE username=:username"
    result = db.session.execute(text(sql), {"username":username})
    user = result.fetchone()
    if not user:
        return (False, "Username does not exist")
    if check_password_hash(user.password_hash, password):
        return (True, "")
    return (False, "Wrong password")

def logout():
    del session["username"]
    csrf_delete()
    message = "Successfully logged out."
    return render_template("success.html", message=message)

def signup(username, password, password_again):
    if not re.search("^[\w._\-]{2,32}$", username):
        return errors.render_error("Invalid username", "signup")
    if password != password_again:
        return errors.render_error("Password inputs do not match", "signup")
    if len(password) < 8 or len(password) > 5000:
        return errors.render_error("Invalid password length", "signup")
    password_hash = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username, password_hash) VALUES (:username, :password_hash)"
        db.session.execute(text(sql), {"username":username, "password_hash":password_hash})
        db.session.commit()
    except:
        return errors.render_error("Username already taken", "signup")
    return login(username, True)
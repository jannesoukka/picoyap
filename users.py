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

def get_user_id(username):
    if username == "":
        id = 0
    else:
        sql = "SELECT id FROM users WHERE username=:username"
        result = db.session.execute(text(sql), {"username":username})
        id = result.fetchone()[0]
    return id    

def is_admin(user_id):
    if user_id == 0:
        return False
    sql = "SELECT is_admin FROM users WHERE id=:user_id"
    result = db.session.execute(text(sql), {"user_id":user_id})
    is_admin = result.fetchone()[0]
    if is_admin == "t":
        is_admin = True
    else:
        is_admin = False
    return is_admin

def is_logged_in(ask_who=False):
    # ask_who: bool. request to return username.
    logged_in = "username" in session
    if not ask_who:
        return logged_in
    if not logged_in:
        return ""
    return session["username"]

def login(username, first_time=False):
    if is_logged_in():
        if first_time:
            errors.flash_succ("signup_again", [username])
        else:
            errors.flash_succ("login_again", [username])
    else:
        if first_time:
            errors.flash_succ("signup")
        errors.flash_succ("login", [username])
    session["username"] = username
    csrf_new()
    return

def login_check(username, password):
    sql = "SELECT password_hash FROM users WHERE username=:username"
    result = db.session.execute(text(sql), {"username":username})
    user = result.fetchone()
    if not user:
        errors.flash_error("username", "exist")
        return False
    if not check_password_hash(user.password_hash, password):
        errors.flash_error("password_login", "wrong")
        return False
    return True

def logout():
    errors.flash_succ("logout")
    del session["username"]
    csrf_delete()
    return

def signup_try(username, password):
    password_hash = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username, password_hash) VALUES (:username, :password_hash)"
        db.session.execute(text(sql), {"username":username, "password_hash":password_hash})
        db.session.commit()
    except:
        errors.flash_error("username", "unique")
        return False
    return True
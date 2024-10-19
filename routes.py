from app import app, db
import content
import errors
from flask import abort, flash, redirect, render_template, request, session
import re
from sqlalchemy.sql import text
import users

@app.route("/")
def index():
    sql = "SELECT f.id, f.topic, COALESCE(COUNT(DISTINCT a.id),0) AS attoyap_count, COALESCE(COUNT(z.id),0) AS zeptoyap_count, " \
          "MAX(a.created_at) AS latest_attoyap, MAX(z.created_at) AS latest_zeptoyap " \
          "FROM femtoyaps f LEFT JOIN attoyaps a ON f.id = a.femtoyap_id LEFT JOIN zeptoyaps z ON a.id = z.attoyap_id GROUP BY f.id " \
          "ORDER BY f.topic"
    result = db.session.execute(text(sql))
    femtoyaps = result.fetchall()
    return render_template("index.html", femtoyaps=femtoyaps)

@app.route("/femtoyaps/<int:femtoyap_id>")
def femtoyap(femtoyap_id):
    sql = "SELECT topic FROM femtoyaps WHERE id=:femtoyap_id"
    result = db.session.execute(text(sql), {"femtoyap_id":femtoyap_id})
    femtoyap = result.fetchone()
    if not femtoyap:
        return errors.render_error("Either the femtoyap does not exist or access to it is restricted.")
    femtoyap_topic = femtoyap[0]
    sql = "SELECT a.id, a.title, a.created_at, u.username, COALESCE(COUNT(z.id),0) AS zeptoyap_count, MAX(z.created_at) AS latest_zeptoyap " \
          "FROM attoyaps a LEFT JOIN users u ON a.creator_id = u.id LEFT JOIN zeptoyaps z ON a.id = z.attoyap_id " \
          "WHERE a.femtoyap_id=:femtoyap_id GROUP BY a.id, a.title, a.created_at, u.username ORDER BY a.created_at DESC"
    result = db.session.execute(text(sql), {"femtoyap_id":femtoyap_id})
    attoyaps = result.fetchall()
    return render_template("femtoyap.html", femtoyap_topic=femtoyap_topic, attoyaps=attoyaps, femtoyap_id=femtoyap_id)

@app.route("/femtoyaps/<int:femtoyap_id>/attoyaps/<int:attoyap_id>")
def attoyap(femtoyap_id, attoyap_id):
    sql = "SELECT a.femtoyap_id, a.title, a.id, u.username FROM attoyaps a LEFT JOIN users u ON a.creator_id = u.id WHERE a.id=:attoyap_id"
    result = db.session.execute(text(sql), {"attoyap_id":attoyap_id})
    attoyap = result.fetchone()
    if not attoyap:
        return errors.render_error("Either the attoyap does not exist or access to it is restricted.")
    if femtoyap_id != attoyap[0]:
        femtoyap_id = attoyap[0]
        return redirect(f"/femtoyaps/{femtoyap_id}/attoyaps/{attoyap_id}")
    sql = "SELECT z.content, z.created_at, u.username FROM zeptoyaps z LEFT JOIN users u ON z.creator_id = u.id " \
          "WHERE attoyap_id=:attoyap_id ORDER BY created_at"
    result = db.session.execute(text(sql), {"attoyap_id":attoyap_id})
    zeptoyaps = result.fetchall()
    return render_template("attoyap.html", attoyap=attoyap, zeptoyaps=zeptoyaps, femtoyap_id=femtoyap_id)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    restrictions = errors.get_restrictions("username")
    restrictions.extend(errors.get_restrictions("password"))
    if request.method == "GET":
        users.csrf_new()
        return render_template("signup.html", restrictions=restrictions)
    else:
        if not users.csrf_check():
            abort(403)
        else:
            username = request.form["username"]
            password = request.form["password"]
            password_again = request.form["password_again"]
            return users.signup(username, password, password_again)
    
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        users.csrf_new()
        return render_template("login.html")
    else:
        if not users.csrf_check():
            abort(403)
        else:
            username = request.form["username"]
            password = request.form["password"]
            login_ok = users.login_ok(username, password)
            if not login_ok[0]:
                return errors.render_error(login_ok[1], "login")
            return users.login(username)
        
@app.route("/logout", methods=["GET", "POST"])
def logout():
    if request.method == "GET":
        if not users.is_logged_in():
            return errors.render_error("Cannot log out if not logged in the first place!", "login")
        return render_template("logout.html")
    else:
        if not users.csrf_check():
            abort(403)
        else:
            return users.logout()
    
@app.route("/femtoyaps/<int:femtoyap_id>/attoyaps/create", methods=["GET", "POST"])
def create_attoyap(femtoyap_id):
    restrictions = errors.get_restrictions("attoyap_title")
    restrictions.extend(errors.get_restrictions("zeptoyap_content"))
    if request.method == "GET":
        if not users.is_logged_in():
            return errors.render_error("You must be logged in to create attoyaps!", "login")
        return render_template("create_attoyap.html", femtoyap_id=femtoyap_id, restrictions=restrictions)
    else:
        if not users.csrf_check():
            abort(403)
        else:
            attoyap_title = request.form["attoyap_title"]
            zeptoyap_content = request.form["zeptoyap_content"]
            attoyap_errors = errors.check_errors("attoyap_title", attoyap_title)
            zeptoyap_errors = errors.check_errors("zeptoyap_content", zeptoyap_content)
            if attoyap_errors or zeptoyap_errors:
                return render_template("create_attoyap.html", femtoyap_id=femtoyap_id, restrictions=restrictions)
            username = session["username"]
            user_id = users.get_user_id(username)
            attoyap_id = content.create_attoyap(femtoyap_id, attoyap_title, user_id)
            content.create_zeptoyap(attoyap_id, zeptoyap_content, user_id)
            return redirect(f"/femtoyaps/{femtoyap_id}/attoyaps/{attoyap_id}")

@app.route("/femtoyaps/<int:femtoyap_id>/attoyaps/<int:attoyap_id>/zeptoyaps/create", methods=["GET", "POST"])
def create_zeptoyap(femtoyap_id, attoyap_id):
    restrictions = errors.get_restrictions("zeptoyap_content")
    if request.method == "GET":
        if not users.is_logged_in():
            return errors.render_error("You must be logged in to create zeptoyaps!", "login")
        else:
            return render_template("create_zeptoyap.html", femtoyap_id=femtoyap_id, attoyap_id=attoyap_id, restrictions=restrictions)
    else:
        if not users.csrf_check():
            abort(403)
        else:
            zeptoyap_content = request.form["zeptoyap_content"]
            zeptoyap_errors = errors.check_errors("zeptoyap_content", zeptoyap_content)
            if zeptoyap_errors:
                return render_template("create_zeptoyap.html", femtoyap_id=femtoyap_id, attoyap_id=attoyap_id, restrictions=restrictions)
            username = session["username"]
            user_id = users.get_user_id(username)
            content.create_zeptoyap(attoyap_id, zeptoyap_content, user_id)
            return redirect(f"/femtoyaps/{femtoyap_id}/attoyaps/{attoyap_id}")
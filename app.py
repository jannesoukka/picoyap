from sqlalchemy.sql import text
from flask import Flask
from flask import redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import re
from werkzeug.security import check_password_hash, generate_password_hash
from secrets import token_hex

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
app.secret_key = getenv("SECRET_KEY")
db = SQLAlchemy(app)

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
    sql = "SELECT a.id, a.title, a.created_at, u.username, COALESCE(COUNT(z.id),0) AS zeptoyap_count, MAX(z.created_at) AS latest_zeptoyap " \
          "FROM attoyaps a LEFT JOIN users u ON a.creator_id = u.id LEFT JOIN zeptoyaps z ON a.id = z.attoyap_id " \
          "WHERE a.femtoyap_id=:femtoyap_id GROUP BY a.id, a.title, a.created_at, u.username ORDER BY a.created_at DESC"
    result = db.session.execute(text(sql), {"femtoyap_id":femtoyap_id})
    attoyaps = result.fetchall()
    sql = "SELECT topic FROM femtoyaps WHERE id=:femtoyap_id"
    result = db.session.execute(text(sql), {"femtoyap_id":femtoyap_id})
    femtoyap_topic = result.fetchone()[0]
    return render_template("femtoyap.html", femtoyap_topic=femtoyap_topic, attoyaps=attoyaps, femtoyap_id=femtoyap_id)

@app.route("/femtoyaps/<int:femtoyap_id>/attoyaps/<int:attoyap_id>")
def attoyap(femtoyap_id, attoyap_id):
    sql = "SELECT z.content, z.created_at, u.username FROM zeptoyaps z LEFT JOIN users u ON z.creator_id = u.id " \
          "WHERE attoyap_id=:attoyap_id ORDER BY created_at"
    result = db.session.execute(text(sql), {"attoyap_id":attoyap_id})
    zeptoyaps = result.fetchall()
    sql = "SELECT a.title, a.id, u.username FROM attoyaps a LEFT JOIN users u ON a.creator_id = u.id WHERE a.id=:attoyap_id"
    result = db.session.execute(text(sql), {"attoyap_id":attoyap_id})
    attoyap = result.fetchone()
    return render_template("attoyap.html", attoyap=attoyap, zeptoyaps=zeptoyaps, femtoyap_id=femtoyap_id)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        session["csrf_token"] = token_hex(16) # temp token to prevent creating accounts unintentionally. not final product as it assumes only that you're not logged in. 
        return render_template("signup.html")
    else:
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        else:
            username = request.form["username"]
            password = request.form["password"]
            password_again = request.form["password_again"]
            if not re.search("^[\w._\-]{2,32}$", username):
                message = "Invalid username"
                suggested_path = "/signup"
                suggestion_name = "signup"
                return render_template("error.html", message=message, suggested_path=suggested_path, suggestion_name=suggestion_name)
            if password != password_again:
                message = "Password inputs do not match"
                suggested_path = "/signup"
                suggestion_name = "signup"
                return render_template("error.html", message=message, suggested_path=suggested_path, suggestion_name=suggestion_name)
            if len(password) < 8 or len(password) > 5000:
                message = "Invalid password length"
                suggested_path = "/signup"
                suggestion_name = "signup"
                return render_template("error.html", message=message, suggested_path=suggested_path, suggestion_name=suggestion_name)
            password_hash = generate_password_hash(password)
            try:
                sql = "INSERT INTO users (username, password_hash) VALUES (:username, :password_hash)"
                db.session.execute(text(sql), {"username":username, "password_hash":password_hash})
                db.session.commit()
            except:
                message = "Username already taken"
                suggested_path = "/signup"
                suggestion_name = "signup"
                return render_template("error.html", message=message, suggested_path=suggested_path, suggestion_name=suggestion_name)
            if "username" in session:
                message = "logged out and "
            else:
                message = ""
            session["username"] = username
            session["csrf_token"] = token_hex(16)
            message = f"Successfully {message}created a new account. You are now logged in as {username}."
            return render_template("success.html", message=message)
    
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        session["csrf_token"] = token_hex(16)
        return render_template("login.html")
    else:
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        else:
            username = request.form["username"]
            password = request.form["password"]
            sql = "SELECT password_hash FROM users WHERE username=:username"
            result = db.session.execute(text(sql), {"username":username})
            user = result.fetchone()
            if not user:
                message = "Username does not exist"
                suggested_path = "/login"
                suggestion_name = "login"
                return render_template("error.html", message=message, suggested_path=suggested_path, suggestion_name=suggestion_name)
            if check_password_hash(user.password_hash, password):
                if "username" in session:
                    message = "logged out and "
                else:
                    message = ""
                session["username"] = username
                session["csrf_token"] = token_hex(16)
                message = f"Successfully {message}logged in as {username}."
                return render_template("success.html", message=message)
            else:
                message = "Wrong password"
                suggested_path = "/login"
                suggestion_name = "login"
                return render_template("error.html", message=message, suggested_path=suggested_path, suggestion_name=suggestion_name)
        
@app.route("/logout", methods=["GET", "POST"])
def logout():
    if request.method == "GET":
        if not "username" in session:
            message = "Cannot log out if not logged in the first place!"
            suggested_path = "/login"
            suggestion_name = "login"
            return render_template("error.html", message=message, suggested_path=suggested_path, suggestion_name=suggestion_name)
        else:
            return render_template("logout.html")
    else:
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        else:
            del session["username"]
            del session["csrf_token"]
            message = "Successfully logged out."
            return render_template("success.html", message=message)
    
@app.route("/femtoyaps/<int:femtoyap_id>/attoyaps/create", methods=["GET", "POST"])
def create_attoyap(femtoyap_id):
    if request.method == "GET":
        if not "username" in session:
            message = "You must be logged in to create attoyaps!"
            suggested_path = "/login"
            suggestion_name = "login"
            return render_template("error.html", message=message, suggested_path=suggested_path, suggestion_name=suggestion_name)
        else:
            return render_template("create_attoyap.html", femtoyap_id=femtoyap_id)
    else:
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        else:
            attoyap_title = request.form["attoyap_title"]
            zeptoyap_content = request.form["zeptoyap_content"]
            if len(attoyap_title) < 1:
                message = "The title is too short, less than 1 character!"
                suggested_path = f"/femtoyaps/{femtoyap_id}/attoyaps/create"
                suggestion_name = "attoyap creation"
                return render_template("error.html", message=message, suggested_path=suggested_path, suggestion_name=suggestion_name)
            if len(attoyap_title) > 100:
                message = "The title is too long, over 100 characters!"
                suggested_path = f"/femtoyaps/{femtoyap_id}/attoyaps/create"
                suggestion_name = "attoyap creation"
                return render_template("error.html", message=message, suggested_path=suggested_path, suggestion_name=suggestion_name)
            if len(zeptoyap_content) > 5000:
                message = "The starting zeptoyap is too long, over 5000 characters!"
                suggested_path = f"/femtoyaps/{femtoyap_id}/attoyaps/create"
                suggestion_name = "attoyap creation"
                return render_template("error.html", message=message, suggested_path=suggested_path, suggestion_name=suggestion_name)
            username = session["username"]
            sql = "SELECT id FROM users WHERE username=:username"
            result = db.session.execute(text(sql), {"username":username})
            user_id = result.fetchone()[0]
            sql = "INSERT INTO attoyaps (femtoyap_id, creator_id, title) VALUES (:femtoyap_id, :user_id, :attoyap_title) RETURNING id"
            result = db.session.execute(text(sql), {"femtoyap_id":femtoyap_id, "user_id":user_id, "attoyap_title":attoyap_title})
            attoyap_id = result.fetchone()[0]
            sql = "INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (:attoyap_id, :user_id, :zeptoyap_content)"
            db.session.execute(text(sql), {"attoyap_id":attoyap_id, "user_id":user_id, "zeptoyap_content":zeptoyap_content})
            db.session.commit()
            return redirect(f"/femtoyaps/{femtoyap_id}/attoyaps/{attoyap_id}")

@app.route("/femtoyaps/<int:femtoyap_id>/attoyaps/<int:attoyap_id>/zeptoyaps/create", methods=["GET", "POST"])
def create_zeptoyap(femtoyap_id, attoyap_id):
    if request.method == "GET":
        if not "username" in session:
            message = "You must be logged in to create zeptoyaps!"
            suggested_path = "/login"
            suggestion_name = "login"
            return render_template("error.html", message=message, suggested_path=suggested_path, suggestion_name=suggestion_name)
        else:
            return render_template("create_zeptoyap.html", femtoyap_id=femtoyap_id, attoyap_id=attoyap_id)
    else:
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        else:
            zeptoyap_content = request.form["zeptoyap_content"]
            if len(zeptoyap_content) > 5000:
                message = "The zeptoyap is too long, over 5000 characters!"
                suggested_path = f"/femtoyaps/{femtoyap_id}/attoyaps/{attoyap_id}/zeptoyaps/create"
                suggestion_name = "zeptoyap creation"
                return render_template("error.html", message=message, suggested_path=suggested_path, suggestion_name=suggestion_name)
            username = session["username"]
            sql = "SELECT id FROM users WHERE username=:username"
            result = db.session.execute(text(sql), {"username":username})
            user_id = result.fetchone()[0]
            sql = "INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (:attoyap_id, :user_id, :zeptoyap_content)"
            db.session.execute(text(sql), {"attoyap_id":attoyap_id, "user_id":user_id, "zeptoyap_content":zeptoyap_content})
            db.session.commit()
            return redirect(f"/femtoyaps/{femtoyap_id}/attoyaps/{attoyap_id}")
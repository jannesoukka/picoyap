from sqlalchemy.sql import text
from flask import Flask
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import re
from werkzeug.security import check_password_hash, generate_password_hash

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
    sql = "SELECT a.id, a.title, COALESCE(COUNT(z.id),0) AS zeptoyap_count, MAX(z.created_at) AS latest_zeptoyap " \
          "FROM attoyaps a LEFT JOIN zeptoyaps z ON a.id = z.attoyap_id WHERE a.femtoyap_id=:femtoyap_id GROUP BY a.id ORDER BY a.created_at DESC"
    result = db.session.execute(text(sql), {"femtoyap_id":femtoyap_id})
    attoyaps = result.fetchall()
    sql = "SELECT topic FROM femtoyaps WHERE id=:femtoyap_id"
    result = db.session.execute(text(sql), {"femtoyap_id":femtoyap_id})
    femtoyap_topic = result.fetchone()[0]
    return render_template("femtoyap.html", femtoyap_topic=femtoyap_topic, attoyaps=attoyaps, femtoyap_id=femtoyap_id)

@app.route("/femtoyaps/<int:femtoyap_id>/attoyaps/<int:attoyap_id>")
def attoyap(femtoyap_id, attoyap_id):
    sql = "SELECT content, created_at FROM zeptoyaps WHERE attoyap_id=:attoyap_id ORDER BY created_at DESC"
    result = db.session.execute(text(sql), {"attoyap_id":attoyap_id})
    zeptoyaps = result.fetchall()
    sql = "SELECT title FROM attoyaps WHERE id=:attoyap_id"
    result = db.session.execute(text(sql), {"attoyap_id":attoyap_id})
    title = result.fetchone()[0]
    return render_template("attoyap.html", title=title, zeptoyaps=zeptoyaps, femtoyap_id=femtoyap_id)

@app.route("/signup", methods=["GET", "POST"])
def signup_attempt():
    if request.method == "GET":
        return render_template("signup.html")
    else:
        username = request.form["username"]
        password = request.form["password"]
        password_again = request.form["password_again"]
        if not re.search("^[\w._\-]{2,32}$", username):
            message = "Invalid username"
            new_attempt_path = "/signup"
            new_attempt_name = "signup"
            return render_template("error.html", message=message, new_attempt_path=new_attempt_path, new_attempt_name=new_attempt_name)
        if password != password_again:
            message = "Password inputs do not match"
            new_attempt_path = "/signup"
            new_attempt_name = "signup"
            return render_template("error.html", message=message, new_attempt_path=new_attempt_path, new_attempt_name=new_attempt_name)
        if len(password) < 8 or len(password) > 5000:
            message = "Invalid password length"
            new_attempt_path = "/signup"
            new_attempt_name = "signup"
            return render_template("error.html", message=message, new_attempt_path=new_attempt_path, new_attempt_name=new_attempt_name)
        password_hash = generate_password_hash(password)
        try:
            sql = "INSERT INTO users (username, password_hash) VALUES (:username, :password_hash)"
            db.session.execute(text(sql), {"username":username, "password_hash":password_hash})
            db.session.commit()
        except:
            message = "Username already taken"
            new_attempt_path = "/signup"
            new_attempt_name = "signup"
            return render_template("error.html", message=message, new_attempt_path=new_attempt_path, new_attempt_name=new_attempt_name)
        message = "Successfully created a new account."
        return render_template("success.html", message=message)
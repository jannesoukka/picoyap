from sqlalchemy.sql import text
from flask import Flask
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
app.secret_key = getenv("SECRET_KEY")
db = SQLAlchemy(app)

@app.route("/")
def index():
    sql = "SELECT id, topic FROM femtoyaps"
    result = db.session.execute(text(sql))
    femtoyaps = result.fetchall()
    return render_template("index.html", femtoyaps=femtoyaps)

@app.route("/femtoyaps/<int:id>")
def femtoyap(id):
    sql = "SELECT id, title FROM attoyaps WHERE femtoyap_id=:id"
    result = db.session.execute(text(sql), {"id":id})
    attoyaps = result.fetchall()
    sql = "SELECT topic FROM femtoyaps WHERE id=:id"
    result = db.session.execute(text(sql), {"id":id})
    topic = result.fetchone()[0]
    return render_template("femtoyap.html", topic=topic, attoyaps=attoyaps, id=id)

@app.route("/femtoyaps/<int:femtoyap_id>/attoyaps/<int:attoyap_id>")
def attoyap(femtoyap_id, attoyap_id):
    sql = "SELECT content FROM zeptoyaps WHERE attoyap_id=:attoyap_id"
    result = db.session.execute(text(sql), {"attoyap_id":attoyap_id})
    zeptoyaps = result.fetchall()
    sql = "SELECT title FROM attoyaps WHERE id=:attoyap_id"
    result = db.session.execute(text(sql), {"attoyap_id":attoyap_id})
    title = result.fetchone()[0]
    return render_template("attoyap.html", title=title, zeptoyaps=zeptoyaps, femtoyap_id=femtoyap_id)
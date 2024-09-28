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
    sql = "SELECT f.id, f.topic, COALESCE(COUNT(DISTINCT a.id),0) AS attoyap_count, COALESCE(COUNT(z.id),0) AS zeptoyap_count, " \
          "MAX(a.created_at) AS latest_attoyap, MAX(z.created_at) AS latest_zeptoyap " \
          "FROM femtoyaps f LEFT JOIN attoyaps a ON f.id = a.femtoyap_id LEFT JOIN zeptoyaps z ON a.id = z.attoyap_id GROUP BY f.id"
    result = db.session.execute(text(sql))
    femtoyaps = result.fetchall()
    return render_template("index.html", femtoyaps=femtoyaps)

@app.route("/femtoyaps/<int:femtoyap_id>")
def femtoyap(femtoyap_id):
    sql = "SELECT a.id, a.title, COALESCE(COUNT(z.id),0) AS zeptoyap_count, MAX(z.created_at) AS latest_zeptoyap " \
          "FROM attoyaps a LEFT JOIN zeptoyaps z ON a.id = z.attoyap_id WHERE a.femtoyap_id=:femtoyap_id GROUP BY a.id"
    result = db.session.execute(text(sql), {"femtoyap_id":femtoyap_id})
    attoyaps = result.fetchall()
    sql = "SELECT topic FROM femtoyaps WHERE id=:femtoyap_id"
    result = db.session.execute(text(sql), {"femtoyap_id":femtoyap_id})
    femtoyap_topic = result.fetchone()[0]
    return render_template("femtoyap.html", femtoyap_topic=femtoyap_topic, attoyaps=attoyaps, femtoyap_id=femtoyap_id)

@app.route("/femtoyaps/<int:femtoyap_id>/attoyaps/<int:attoyap_id>")
def attoyap(femtoyap_id, attoyap_id):
    sql = "SELECT content FROM zeptoyaps WHERE attoyap_id=:attoyap_id"
    result = db.session.execute(text(sql), {"attoyap_id":attoyap_id})
    zeptoyaps = result.fetchall()
    sql = "SELECT title FROM attoyaps WHERE id=:attoyap_id"
    result = db.session.execute(text(sql), {"attoyap_id":attoyap_id})
    title = result.fetchone()[0]
    return render_template("attoyap.html", title=title, zeptoyaps=zeptoyaps, femtoyap_id=femtoyap_id)
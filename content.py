from app import db
from sqlalchemy.sql import text

def create_attoyap(femtoyap_id, title, user_id):
    sql = "INSERT INTO attoyaps (femtoyap_id, creator_id, title) VALUES (:femtoyap_id, :user_id, :title) RETURNING id"
    result = db.session.execute(text(sql), {"femtoyap_id":femtoyap_id, "user_id":user_id, "title":title})
    id = result.fetchone()[0]
    db.session.commit()
    return id

def create_zeptoyap(attoyap_id, content, user_id):
    sql = "INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (:attoyap_id, :user_id, :content)"
    db.session.execute(text(sql), {"attoyap_id":attoyap_id, "user_id":user_id, "content":content})
    db.session.commit()

def view_picoyap_public():
    sql = "SELECT f.id, f.topic, COALESCE(COUNT(DISTINCT a.id),0) AS attoyap_count, COALESCE(COUNT(z.id),0) AS zeptoyap_count, " \
        "MAX(a.created_at) AS latest_attoyap, MAX(z.created_at) AS latest_zeptoyap " \
        "FROM femtoyaps f LEFT JOIN attoyaps a ON f.id = a.femtoyap_id LEFT JOIN zeptoyaps z ON a.id = z.attoyap_id " \
        "WHERE f.is_secret = 'f' GROUP BY f.id " \
        "ORDER BY f.topic"
    result = db.session.execute(text(sql))
    femtoyaps = result.fetchall()
    return femtoyaps

def view_picoyap_secret(user_id):
    if user_id == -1:
        sql = "SELECT f.id, f.topic, COALESCE(COUNT(DISTINCT a.id),0) AS attoyap_count, COALESCE(COUNT(z.id),0) AS zeptoyap_count, " \
            "MAX(a.created_at) AS latest_attoyap, MAX(z.created_at) AS latest_zeptoyap " \
            "FROM femtoyaps f LEFT JOIN attoyaps a ON f.id = a.femtoyap_id LEFT JOIN zeptoyaps z ON a.id = z.attoyap_id " \
            "WHERE f.is_secret = 't' GROUP BY f.id " \
            "ORDER BY f.topic"
        result = db.session.execute(text(sql))
    else:
        sql = "SELECT f.id, f.topic, COALESCE(COUNT(DISTINCT a.id),0) AS attoyap_count, COALESCE(COUNT(z.id),0) AS zeptoyap_count, " \
            "MAX(a.created_at) AS latest_attoyap, MAX(z.created_at) AS latest_zeptoyap " \
            "FROM femtoyaps f LEFT JOIN attoyaps a ON f.id = a.femtoyap_id LEFT JOIN zeptoyaps z ON a.id = z.attoyap_id " \
            "LEFT JOIN secret_permissions s ON f.id = s.femtoyap_id WHERE s.user_id=:user_id AND f.is_secret = 't' GROUP BY f.id " \
            "ORDER BY f.topic"
        result = db.session.execute(text(sql), {"user_id":user_id})
    secret_femtoyaps = result.fetchall()
    return secret_femtoyaps
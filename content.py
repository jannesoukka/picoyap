from app import db
from sqlalchemy.sql import text

def zeptoyap_ok(content):
    return (len(content) <= 5000, "The starting zeptoyap is too long, over 5000 characters!")

def create_zeptoyap(attoyap_id, content, username):
    sql = "SELECT id FROM users WHERE username=:username"
    result = db.session.execute(text(sql), {"username":username})
    user_id = result.fetchone()[0]
    sql = "INSERT INTO zeptoyaps (attoyap_id, creator_id, content) VALUES (:attoyap_id, :user_id, :content)"
    db.session.execute(text(sql), {"attoyap_id":attoyap_id, "user_id":user_id, "content":content})
    db.session.commit()
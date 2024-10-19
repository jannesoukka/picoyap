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
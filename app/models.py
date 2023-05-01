from app import db

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
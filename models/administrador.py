from app import db

class Administrador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
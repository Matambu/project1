from application import db

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    planet = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    databank = db.Column(db.String(100), nullable=False)

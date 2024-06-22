from app import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

class Maquina(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(15), unique=True, nullable=False)
    status = db.Column(db.String(20), nullable=False, default='available')

class Deploy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='pending')
    data = db.Column(db.DateTime, default=db.func.current_timestamp())
    maquina1_id = db.Column(db.Integer, db.ForeignKey('maquina.id'), nullable=False)
    maquina2_id = db.Column(db.Integer, db.ForeignKey('maquina.id'), nullable=False)
    maquina3_id = db.Column(db.Integer, db.ForeignKey('maquina.id'), nullable=False)

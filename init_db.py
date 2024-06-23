from app import app, db
from models import Usuario, Maquina, Deploy

with app.app_context():
    db.create_all()

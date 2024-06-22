from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from models import Usuario, Maquina, Deploy

@app.route('/usuarios', methods=['POST'])
def create_usuario():
    data = request.get_json()
    nome = data.get('nome')
    email = data.get('email')
    
    if not nome or not email:
        return jsonify({"error": "Nome e email são obrigatórios"}), 400

    usuario = Usuario(nome=nome, email=email)
    db.session.add(usuario)
    db.session.commit()
    return jsonify({"id": usuario.id, "nome": usuario.nome, "email": usuario.email}), 201

@app.route('/maquinas', methods=['POST'])
def create_maquina():
    data = request.get_json()
    ip = data.get('ip')
    status = data.get('status', 'available')
    
    if not ip:
        return jsonify({"error": "IP é obrigatório"}), 400

    maquina = Maquina(ip=ip, status=status)
    db.session.add(maquina)
    db.session.commit()
    return jsonify({"id": maquina.id, "ip": maquina.ip, "status": maquina.status}), 201

@app.route('/deploys', methods=['POST'])
def create_deploy():
    data = request.get_json()
    usuario_id = data.get('usuario_id')
    maquina1_id = data.get('maquina1_id')
    maquina2_id = data.get('maquina2_id')
    maquina3_id = data.get('maquina3_id')
    status = data.get('status', 'pending')
    
    if not usuario_id or not maquina1_id or not maquina2_id or not maquina3_id:
        return jsonify({"error": "Todos os IDs são obrigatórios"}), 400

    deploy = Deploy(usuario_id=usuario_id, status=status,
                    maquina1_id=maquina1_id, maquina2_id=maquina2_id, maquina3_id=maquina3_id)
    db.session.add(deploy)
    db.session.commit()
    return jsonify({"id": deploy.id, "usuario_id": deploy.usuario_id, "status": deploy.status}), 201

@app.route('/deploys/<int:deploy_id>', methods=['GET'])
def get_deploy(deploy_id):
    deploy = Deploy.query.get_or_404(deploy_id)
    return jsonify({"id": deploy.id, "usuario_id": deploy.usuario_id, "status": deploy.status,
                    "maquina1_id": deploy.maquina1_id, "maquina2_id": deploy.maquina2_id, "maquina3_id": deploy.maquina3_id})

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Enquete(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    opcoes = db.relationship('OpcaoEnquete', backref='enquete', lazy=True, cascade='all,delete')

class OpcaoEnquete(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.Text, nullable=False)
    votos = db.Column(db.Integer, default=0)
    enquete_id = db.Column(db.Integer, db.ForeignKey('enquete.id'), nullable=False)

@app.route('/api/enquetes', methods=['POST'])
def criar_enquete():
    data = request.get_json()
    if 'titulo' in data and 'descricao' in data:
        new_enquete = Enquete(titulo=data['titulo'], descricao=data['descricao'])
        db.session.add(new_enquete)
        db.session.commit()
        return jsonify({"message": "Enquete criada com sucesso"}), 201
    else:
        return jsonify({"error": "Título e descrição são obrigatórios"}), 400

@app.route('/api/enquetes', methods=['GET'])
def listar_enquetes():
    enquetes = Enquete.query.all()
    enquetes_list = []
    for enquete in enquetes:
        enquete_data = {
            "id": enquete.id,
            "titulo": enquete.titulo,
            "descricao": enquete.descricao
        }
        enquetes_list.append(enquete_data)
    return jsonify(enquetes_list), 200

@app.route('/api/enquetes/<int:id>', methods=['GET'])
def obter_detalhes_enquete(id):
    enquete = Enquete.query.get(id)
    if enquete:
        enquete_data = {
            "id": enquete.id,
            "titulo": enquete.titulo,
            "descricao": enquete.descricao,
            "opcoes": [{"id": opcao.id, "descricao": opcao.descricao, "votos": opcao.votos} for opcao in enquete.opcoes]
        }
        return jsonify(enquete_data), 200
    else:
        return jsonify({"error": "Enquete não encontrada"}), 404

@app.route('/api/enquetes/<int:id>/votar', methods=['POST'])
def votar_enquete(id):
    data = request.get_json()
    if 'opcao_id' in data:
        try:
            db.session.begin()

            opcao = OpcaoEnquete.query.get(data['opcao_id'])
            if opcao:
                opcao.votos += 1
                db.session.commit()  
                return jsonify({"message": "Voto registrado com sucesso"}), 200
            else:
                return jsonify({"error": "Opção não encontrada"}), 404

        except SQLAlchemyError as e:
            db.session.rollback()  
            return jsonify({"error": "Erro ao votar na enquete"}), 500

    else:
        return jsonify({"error": "opcao_id é obrigatório"}), 400

@app.route('/api/enquetes/<int:id>/resultados', methods=['GET'])
def obter_resultados_enquete(id):
    enquete = Enquete.query.get(id)
    if enquete:
        resultados = [{"id": opcao.id, "descricao": opcao.descricao, "votos": opcao.votos} for opcao in enquete.opcoes]
        return jsonify(resultados), 200
    else:
        return jsonify({"error": "Enquete não encontrada"}), 404

@app.route('/api/enquetes/<int:id>/opcoes', methods=['GET'])
def visualizar_opcoes_enquete(id):
    enquete = Enquete.query.get(id)
    if enquete:
        opcoes = [{"id": opcao.id, "descricao": opcao.descricao} for opcao in enquete.opcoes]
        return jsonify(opcoes), 200
    else:
        return jsonify({"error": "Enquete não encontrada"}), 404

@app.route('/api/enquetes/<int:id>/opcoes', methods=['POST'])
def adicionar_opcao_enquete(id):
    data = request.get_json()
    if 'descricao' in data:
        enquete = Enquete.query.get(id)
        if enquete:
            new_opcao = OpcaoEnquete(descricao=data['descricao'], enquete=enquete)
            db.session.add(new_opcao)
            db.session.commit()
            return jsonify({"message": "Opção adicionada com sucesso"}), 201
        else:
            return jsonify({"error": "Enquete não encontrada"}), 404
    else:
        return jsonify({"error": "Descrição da opção é obrigatória"}), 400

@app.route('/api/enquetes/<int:id>', methods=['DELETE'])
def deletar_enquete(id):
    enquete = Enquete.query.get(id)
    if enquete:
        for opcao in enquete.opcoes:
            db.session.delete(opcao)
        db.session.delete(enquete)
        db.session.commit()
        return jsonify({"message": "Enquete deletada com sucesso"}), 200
    else:
        return jsonify({"error": "Enquete não encontrada"}), 404

@app.route('/api/enquetes/<int:id_enquete>/opcoes/<int:id_opcao>', methods=['DELETE'])
def deletar_opcao_enquete(id_enquete, id_opcao):
    opcao = OpcaoEnquete.query.filter_by(enquete_id=id_enquete, id=id_opcao).first()
    if opcao:
        db.session.delete(opcao)
        db.session.commit()
        return jsonify({"message": "Opção deletada com sucesso"}), 200
    else:
        return jsonify({"error": "Opção não encontrada"}), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

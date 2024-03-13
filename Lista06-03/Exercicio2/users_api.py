from flask import Flask, request, jsonify
import json

app = Flask(__name__)

def load_users():
    with open('users_data.json', 'r') as file:
        return json.load(file)

def save_users(users):
    with open('users_data.json', 'w') as file:
        json.dump(users, file)

@app.route('/users', methods=['GET'])
def get_users():
    users = load_users()
    return jsonify(users)

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    users = load_users()
    users.append(data)
    save_users(users)
    return jsonify({'message': 'Usuário adicionado com sucesso'})

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    users = load_users()
    users[user_id] = data
    save_users(users)
    return jsonify({'message': 'Usuário atualizado com sucesso'})

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    users = load_users()
    del users[user_id]
    save_users(users)
    return jsonify({'message': 'Usuário excluído com sucesso'})

if __name__ == '__main__':
    app.run(debug=True)

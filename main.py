from flask import Flask, jsonify, request
from endpoints_logic import get_users, get_user, create_user, update_user, delete_user

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def read_users():
    return jsonify(get_users())

@app.route('/users/<int:user_id>', methods=['GET'])
def read_user(user_id):
    user = get_user(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/users', methods=['POST'])
def create_user():
    user_data = request.get_json()
    response = create_user(user_data)
    return jsonify(response), 201

@app.route('/users/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
    updated_data = request.get_json()
    try:
        response = update_user(user_id, updated_data)
        return jsonify(response), 204
    except ValueError as error:
        return jsonify({"error": str(error)}), 400

@app.route('/users/<int:user_id>', methods=['PUT'])
def create_or_update_user(user_id):
    user_data = request.get_json()
    response = update_user(user_id, user_data)
    return jsonify(response), 204

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        response = delete_user(user_id)
        return jsonify(response), 204
    except ValueError as error:
        return jsonify({"error": str(error)}), 400

if __name__ == '__main__':
    app.run()

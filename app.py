from flask import Flask, jsonify, request

app = Flask(__name__)

USERS = {
    101:{"name":"Alice","email":"alice@example.com","role":"admin"},
    102:{"name":"Bob","email":"bob@example.com","role":"user"},
    103:{"name":"Charlie","email":"charlie@example.com","role":"user"}
}

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(USERS)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = USERS.get(user_id)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
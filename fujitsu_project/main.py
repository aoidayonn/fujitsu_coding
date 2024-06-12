import base64
from flask import Flask, request, jsonify,render_template

app = Flask(__name__)

# テスト用のユーザーデータ
test_user = {
    "user_id": "TaroYamada",
    "password": "PaSSwd4TY",
    "nickname": "たろー",
    "comment": "僕は元気です"
}

# ユーザーデータベース（テスト用）
users = {
    "TaroYamada": test_user
}


# Basic認証をチェックする関数
def check_auth(auth_header):
    try:
        decoded_credentials = base64.b64decode(auth_header.split(' ')[1]).decode('utf-8').split(':')
        user_id = decoded_credentials[0]
        password = decoded_credentials[1]
        if user_id in users and users[user_id]['password'] == password:
            return True, user_id
    except:
        pass
    return False, None


# POST /signup
@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    user_id = data.get('user_id')
    password = data.get('password')

    if not user_id or not password:
        return jsonify({"message": "Account creation failed", "cause": "required user_id and password"}), 400

    if len(user_id) < 6 or len(user_id) > 20 or not user_id.isalnum():
        return jsonify({"message": "Account creation failed", "cause": "invalid user_id length or format"}), 400

    if len(password) < 8 or len(password) > 20:
        return jsonify({"message": "Account creat/1ion failed", "cause": "invalid password length"}), 400

    if any(
            char not in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
            for char in password):
        return jsonify({"message": "Account creation failed", "cause": "invalid password characters"}), 400

    if user_id in users:
        return jsonify({"message": "Account creation failed", "cause": "already same user_id is used"}), 400

    users[user_id] = {"user_id": user_id, "password": password, "nickname": user_id}

    return jsonify({"message": "Account successfully created", "user": {"user_id": user_id, "nickname": user_id}}), 200


# GET /users/{user_id}
@app.route('/users/<string:user_id>', methods=['GET'])
def get_user(user_id):
    auth_result, auth_user_id = check_auth(request.headers.get('Authorization'))
    if not auth_result:
        return jsonify({"message": "Authentication Failed"}), 401

    if user_id not in users:
        return jsonify({"message": "No User found"}), 404

    user_data = users[user_id]
    response_data = {
        "message": "User details by user_id",
        "user": {
            "user_id": user_data["user_id"],
            "nickname": user_data.get("nickname", user_id),
            "comment": user_data.get("comment", "")
        }
    }

    return jsonify(response_data), 200


# PATCH /users/{user_id}
@app.route('/users/<string:user_id>', methods=['PATCH'])
def update_user(user_id):
    auth_result, auth_user_id = check_auth(request.headers.get('Authorization'))
    if not auth_result:
        return jsonify({"message": "Authentication Failed"}), 401

    if user_id not in users:
        return jsonify({"message": "No User found"}), 404

    data = request.json
    nickname = data.get('nickname')
    comment = data.get('comment')

    if not nickname and not comment:
        return jsonify({"message": "User updation failed", "cause": "required nickname or comment"}), 400

    if user_id != auth_user_id:
        return jsonify({"message": "No Permission for Update"}), 403

    user_data = users[user_id]

    if nickname:
        user_data['nickname'] = nickname[:30]
    if comment is not None:
        user_data['comment'] = comment[:100]

    return jsonify({"message": "User successfully updated",
                    "recipe": [{"nickname": user_data['nickname'], "comment": user_data['comment']}]}), 200


# POST /close
@app.route('/close', methods=['POST'])
def close_account():
    auth_result, auth_user_id = check_auth(request.headers.get('Authorization'))
    if not auth_result:
        return jsonify({"message": "Authentication Failed"}), 401

    if auth_user_id not in users:
        return jsonify({"message": "No User found"}), 404

    # アカウントを削除
    del users[auth_user_id]

    return jsonify({"message": "Account and user successfully removed"}), 200

# ルート
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

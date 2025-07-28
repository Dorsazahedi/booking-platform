from flask import Flask, request, jsonify

app = Flask(__name__)
users = {}

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400
    if username in users:
        return jsonify({"error": "User already exists"}), 409
    users[username] = password
    return jsonify({"message": f"User {username} registered successfully! Congratulations!"}), 201

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if users.get(username) == password:
        return jsonify({"message": f"Welcome back, {username}!"}), 200
    return jsonify({"error": "Invalid credentials! Try again!"}), 401

@app.route("/profile/<username>", methods=["GET"])
def profile(username):
    if username in users:
        return jsonify({"username": username}), 200
    return jsonify({"error": "User not found! Try again!"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

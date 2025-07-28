from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/notify/email", methods=["POST"])
def send_email():
    data = request.get_json()
    user = data.get("user")
    message = data.get("message")
    print("📬 Notification Service Log:")
    print(f"   ✅ Email successfully sent to: {user}")
    print(f"   📩 Message content: {message}\n")
    return jsonify({"status": "email sent", "user": user}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)

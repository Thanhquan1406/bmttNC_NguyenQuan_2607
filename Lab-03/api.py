from flask import Flask, request, jsonify
from cipher.rsa import RSACipher

app = Flask(__name__)

rsa_cipher = RSACipher()

@app.route("/api/rsa/generate_keys", methods=["GET"])
def generate_key():
    rsa_cipher.generate_keys()
    return jsonify({"message" : "Tao khoa thanh cong"})

@app.route("/api/rsa/encrypt", methods=["POST"])
def encrypted_rsa ():
    data = request.json
    plain_text = data["plain_text"]
    key = data["key"]
    public_key, private_key = rsa_cipher.load_keys()
    if key =="public":
        key = public_key
    elif key =="private":
         key = private_key
    else :
        return jsonify({"message" : "Tao khoa sai"})
    encrypted_text = rsa_cipher.encrypt(plain_text, key)
    encrypted_hex = encrypted_text.hex()
    return jsonify({"encrypted_message" : encrypted_hex})
# @app.route("/api/rsa/decrypt", methods=["POST"])

# @app.route("/api/rsa/sign", methods=["POST"])

# @app.route("/api/rsa/verify", methods=["POST"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port= 5000, debug= True)
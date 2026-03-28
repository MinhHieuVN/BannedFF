from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"status": "API Running"})


@app.route("/inspect", methods=["POST"])
def inspect():
    token = request.json.get("token")

    url = f"https://100067.connect.garena.com/oauth/token/inspect?token={token}"

    r = requests.get(url)

    return jsonify(r.json())


@app.route("/ban", methods=["POST"])
def ban():
    token = request.json.get("token")

    headers = {
        "Authorization": f"Bearer {token}",
        "User-Agent": "Mozilla/5.0"
    }

    url = "https://100067.connect.garena.com/game/account_security/ban"

    r = requests.post(url, headers=headers)

    return jsonify({
        "status": r.status_code,
        "result": r.text
    })


if __name__ == "__main__":
    app.run()

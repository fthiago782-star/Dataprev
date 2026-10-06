from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def health():
    return "Guardrail running"

@app.route("/detect", methods=["POST"])
def detect():

    body = request.get_json()

    text = str(body).lower()

    if "cpf" in text:
        return jsonify({
            "decision": "block",
            "reason": "CPF detected"
        })

    return jsonify({
        "decision": "allow"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
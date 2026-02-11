from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from openai import OpenAI

app = Flask(__name__)
CORS(app)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def home():
    return "Chatbot online 🚀"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    mensagem = data.get("mensagem", "")

    try:
        resposta = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um atendente virtual educado e profissional."},
                {"role": "user", "content": mensagem}
            ]
        )

        return jsonify({
            "resposta": resposta.choices[0].message.content
        })

    except Exception as e:
        return jsonify({
            "erro": str(e)
        }), 500

if __name__ == "__main__":
    app.run()

from flask import Flask, request, jsonify
import os
import openai

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return "Chatbot online 🚀"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    mensagem = data.get("mensagem", "")

    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Você é um atendente virtual educado, direto e profissional."
            },
            {
                "role": "user",
                "content": mensagem
            }
        ]
    )

    return jsonify({
        "resposta": resposta.choices[0].message.content
    })

if __name__ == "__main__":
    app.run()

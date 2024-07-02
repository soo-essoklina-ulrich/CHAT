import os
from dotenv import load_dotenv

from openai import OpenAI
from flask import Flask, request, jsonify
from flask_cors import CORS

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

app = Flask(__name__)
cors = CORS()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL")

)

cors.init_app(
    app,
    resources={r"*": {"origins": "*"}}
)


def generate_response(prompt):
    response = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL"),
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
        max_tokens=128,
    )
    return response.choices[0].message.content


@app.route('/chat', methods=['POST'])
def chat_api():
    prompt = request.json.get('prompt', None)
    if not prompt:
        return {"msg": "Missing required fields"}, 400
    response = generate_response(prompt)
    return jsonify({"response": response})


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# if __name__ == "__main__":
#     app.run(
#         host='0.0.0.0',
#         port=8080,
#         debug=True
#     )

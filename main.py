from openai import OpenAI
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS()
client = OpenAI(
    api_key="372bc681bc094005af573f9cf35fb076",
    base_url="https://api.aimlapi.com"
)
cors.init_app(
    app,
    resources={r"*": {"origins": "*"}}
)


def generate_response(prompt):
    response = client.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.1",
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


if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=8080,
        debug=True
    )

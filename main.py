from openai import OpenAI

client = OpenAI(
    api_key="372bc681bc094005af573f9cf35fb076",
    base_url="https://api.aimlapi.com"
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


def chat():
    response = generate_response("comment tu marche ?\n")
    print(f"Chatbot : {response}")


if __name__ == "__main__":
    chat()

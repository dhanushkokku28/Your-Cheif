import requests

GEMINI_API_KEY = "AIzaSyAGd5qIMc-JGrRAjx3Q8iswDi2TxNeqbqQ"
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

def generate_content(prompt):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {GEMINI_API_KEY}"
    }
    data = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }
    response = requests.post(API_URL, headers=headers, json=data)
    return response.json()

if __name__ == "__main__":
    prompt = "Explain zero-shot prompting in simple terms."
    result = generate_content(prompt)
    print(result)
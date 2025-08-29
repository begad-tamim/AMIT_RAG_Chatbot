import requests

API_KEY = "AIzaSyCmyBnUkNvm70VpbJLLvIaFdv6YB7t2JwA"
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

question = input("Enter your Question: ")

payload = {
  "contents": [
    {
      "parts": [
        {"text": question}
      ]
    }
  ]
}

response = requests.post(url, json=payload)

if response.status_code == 200:
    data = response.json()
    print(data["candidates"][0]["content"]["parts"][0]["text"])
else:
    print(f"Error: {response.status_code} - {response.text}")
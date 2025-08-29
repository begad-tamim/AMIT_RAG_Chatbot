import PyPDF2
import requests
import os
from prompting import prompt_config

API_KEY = "AIzaSyCmyBnUkNvm70VpbJLLvIaFdv6YB7t2JwA"
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

DOCS_DIR = r"D:\Chatbot\AMIT_RAG_Chatbot\AMIT_RAG_Chatbot\docs"

def read_all_pdfs(folder_path):
    all_text = ""
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(folder_path, filename)
            try:
                with open(pdf_path, "rb") as f:
                    reader = PyPDF2.PdfReader(f)
                    for page in reader.pages:
                        text = page.extract_text()
                        if text:
                            all_text += text + "\n"
                print(f"📄 Loaded: {filename}")
            except Exception as e:
                print(f"⚠️ Error reading {filename}: {e}")
    return all_text


# Step 1: Collect context from all PDFs once
relevant_context = read_all_pdfs(DOCS_DIR)

if not relevant_context.strip():
    print("❌ Sorry, no information was found in PDFs. The chatbot cannot run.")
else:
    print("✅ Knowledge base loaded. You can now start asking questions!")
    print("💡 Type 'exit' to quit.\n")

    while True:
        # The user's question
        question = input("Enter your Question: ")

        if question.lower() in ["exit", "quit", "bye"]:
            print("👋 Exiting chatbot. Goodbye!")
            break

        # Step 3: Make the API request
        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": prompt_config["instructions"]},
                    ]
                }
            ]
        }

        response = requests.post(url, json=payload)

        if response.status_code == 200:
            data = response.json()
            try:
                answer = data["candidates"][0]["content"]["parts"][0]["text"]
                print("\n🤖 Amit Helper:\n", answer, "\n")
            except Exception as e:
                print("⚠️ Unexpected response format:", e)
                print(data)
        else:
            print(f"❌ Error: {response.status_code} - {response.text}")
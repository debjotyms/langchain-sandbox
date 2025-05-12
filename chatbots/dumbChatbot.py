from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

gemini_chat_model = ChatGoogleGenerativeAI(model='gemini-2.0-flash', temperature=0)

while True:
    prompt = input("User: ")

    if prompt == "exit":
        break

    ai = gemini_chat_model.invoke(prompt)
    print(f"AI: {ai.content}")
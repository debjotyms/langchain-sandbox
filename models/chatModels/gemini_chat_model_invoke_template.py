from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

gemini_chat_model = ChatGoogleGenerativeAI(model='gemini-2.0-flash', temperature=1)
result = gemini_chat_model.invoke("What is the capital of Bangladesh?")

print(result)
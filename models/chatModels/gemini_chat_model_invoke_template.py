from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

gemini_chat_model = ChatGoogleGenerativeAI(model='gemini-2.0-flash', temperature=0)
result = gemini_chat_model.invoke("write a poem of 4 lines about love.")

print(result.content)
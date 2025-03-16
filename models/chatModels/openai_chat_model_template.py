from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

openai_chat_model = OpenAI(model='gpt-4')
result = openai_chat_model.invoke("Who is Elon Musk?")
from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

openai_llm_model = OpenAI(model='gpt-3.5-turbo-instruct')
result = openai_llm_model.invoke("What is the meaning of AGI?")

print(result)

# load_dotenv() → Used to load API key from the .env file.
# .invoke() → Takes a string as prompt and returns the result as a string.
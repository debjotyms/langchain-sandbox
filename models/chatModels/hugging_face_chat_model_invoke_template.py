from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

tiny_llama = HuggingFaceEndpoint(
    repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text-generation"
)

hf_chat_model = ChatHuggingFace(llm = tiny_llama)

result = hf_chat_model.invoke("Do you believe in Parallel?")

print(result)

# `load_dotenv()` → Used to ==load API== key from the `.env` file.
# `.invoke()` → Takes a ==string== as ==prompt== and returns the result as a ==string==.
# `result` → This would be a `langchain_core.messages.AIMessage` object. This object contains the content generated by the ==ChatGoogleGenerativeAI== model.
# `HuggingFaceEndpoint` → We need this when we work with HF [[API]].
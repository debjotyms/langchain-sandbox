from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

gemini_chat_model = ChatGoogleGenerativeAI(model='gemini-2.0-flash', temperature=0)

chat_history = [SystemMessage(content="You are a good student! Always ans in a simple single sentence.")]

while True:
    human = HumanMessage(content = input("Human : "))

    if(human.content == "exit"):
        break

    chat_history.append(human)
    result = gemini_chat_model.invoke(chat_history)
    chat_history.append(result)
    
    print(f"AI    : {result.content}")

print(chat_history)
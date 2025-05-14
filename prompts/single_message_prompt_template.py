from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash', temperature=0)

prompt = PromptTemplate.from_template("Summarize {topic} in {line} sentences. Every sentence should be in a separate line mentioning the line number at the beginning.")

topic = input("Topic: ")
line = input("Lines: ")

formatted_prompt = prompt.format(topic=topic, line=line)
result = model.invoke(formatted_prompt)

print(result.content)
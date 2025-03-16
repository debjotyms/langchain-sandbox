from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

openai_embedding_model = OpenAIEmbeddings(
    model='text-embedding-3-small',
    dimensions=32
)

documents = [
    "My name is Debjoty.",
    "I am a good Boy."
    "I like to play football"
]

result = openai_embedding_model.embed_query("My name is Debjoty Mitra")
result = openai_embedding_model.embed_documents(documents)

print(str(result))

# OpenAIEmbeddings → Used for working with Embedding models.
# dimensions → The dimension of the output vector.
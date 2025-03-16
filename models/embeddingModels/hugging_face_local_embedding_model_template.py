from langchain_huggingface import HuggingFaceEmbeddings

miniLM_embedding_model = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")

documents = [
    "My name is Debjoty.",
    "I am a good Boy."
    "I like to play football"
]

vector = miniLM_embedding_model.embed_documents(documents)

print(str(vector))
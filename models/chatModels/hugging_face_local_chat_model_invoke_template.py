from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

tiny_llama = HuggingFacePipeline.from_model_id(
    model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text-generation",
    pipeline_kwargs = dict(
        temperature = 0.5,
        max_new_tokens = 10
    )
)

hf_chat_model = ChatHuggingFace(llm = tiny_llama)
result = hf_chat_model.invoke("Do you believe in God?")

print(result)

# - `HuggingFacePipeline` → This is used during local model run.
# - `model_id` → You will get this value from https://huggingface.co/models
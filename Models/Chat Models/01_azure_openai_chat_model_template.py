from langchain_openai import AzureOpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize the AzureOpenAI model
openai_llm_model = AzureOpenAI(
    deployment_name=os.getenv("DEPLOYMENT_NAME"),  # Deployment name from .env
    azure_endpoint=os.getenv("AZURE_ENDPOINT"),    # Azure endpoint from .env
    api_key=os.getenv("OPENAI_API_KEY"),           # API key from .env
    api_version=os.getenv("API_VERSION")           # API version from .env
)

# Invoke the model with a prompt
result = openai_llm_model.invoke("What is the meaning of AGI?")

# Print the result
print(result)
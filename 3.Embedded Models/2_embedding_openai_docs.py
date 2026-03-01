from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv


load_dotenv()

documents = [
    "Delhi is the capital of India",
    "Doha is the capital of Qatar",
    "Riyadh is the capital of Saudi Arabia"
]

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)

result = embedding.embed_documents(documents)

print(str(result))
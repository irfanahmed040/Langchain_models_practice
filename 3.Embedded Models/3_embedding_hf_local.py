from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = HuggingFaceEmbeddings(model = "sentence-transformers/all-MiniLM-L6-v2") #provides a 384 dimensional vector 

documents = [
    "Delhi is the capital of India",
    "Doha is the capital of Qatar",
    "Riyadh is the capital of Saudi Arabia"
]
# result = embedding.embed_query("delhi is the capital of india")

result = embedding.embed_documents(documents)

print(str(result))
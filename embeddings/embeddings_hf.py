from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2", encode_kwargs={'normalize_embeddings': True})
result = embeddings.embed_query("Ankush bhardwaj is my name add I live in India")
print(str(result))
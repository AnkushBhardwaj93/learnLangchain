from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()


embeddings = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=32)
result = embeddings.embed_query("Ankush bhardwaj is my name add I live in India")
print(str(result))


from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


load_dotenv()
embeddings = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=32)


documents={
      "virat kohli is a famous indian cricketer. virat kohli is a right handed batsman.",
      "jasprit bumrah is known for his fast bowling.",
      "sachin tendulkar is regarded as one of the greatest batsmen.",
      "sourav ganguly was a successful captain for india."
}

query="who is the best batsman in india?"

doc_embeddings_list= embeddings.embed_documents(documents)
query_embedding= embeddings.embed_query(query)

similarity_scores= cosine_similarity([query_embedding],doc_embeddings_list)[0]

print(similarity_scores)


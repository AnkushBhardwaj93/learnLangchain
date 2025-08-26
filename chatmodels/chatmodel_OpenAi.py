from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

chat = OpenAI(model_name="gpt-4o-mini", temperature=0.7)

result = chat.invoke("What is the capital of India?")
print(result)
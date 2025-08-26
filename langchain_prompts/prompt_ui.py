from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st


load_dotenv()
chat = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)

st.title("Chat with GPT-4o-mini")
st.header("Ask anything you want!")
user_input = st.text_input("Your Question:",)
if st.button("Submit"):
      st.text("random text")

#Q&A Chatbot
##from langchain.llms import OpenAI
from langchain_community.llms import OpenAI
from dotenv import load_dotenv
#from openai import OpenAI
import streamlit as st
import os


from urllib import response

load_dotenv() # take environment variables from .env file.

api_key = os.getenv("OPEN_API_KEY")

def get_openai_response(question):
    llm = OpenAI(temperature = 0.6,openai_api_key = api_key)
    response =llm(question)
    return response

#intialize the streamlit app
st.set_page_config(page_title = "Q&A Chatbot Demo")

st.header("Small Q&A chatbot using Langchain and openAI")

input = st.text_input("Input:", key = "input")
answer = get_openai_response(input) 

submit = st.button("Ask the question")

#if button is clicked

if submit:
    st.subheader("Here is your answer")
    st.write(answer)

    








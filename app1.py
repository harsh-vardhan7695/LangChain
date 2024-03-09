# Cobersational ChatBot
import streamlit as st
import os
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
load_dotenv()

chat= ChatOpenAI(temperature = 0.6,openai_api_key = os.getenv("OPEN_API_KEY"),model = 'gpt-3.5-turbo')

if 'messages' not in st.session_state:
    st.session_state['messages'] =[
        SystemMessage(content = "You are a comedian AI assistant")
    ]


def get_openai_response(question):
    st.session_state['messages'].append(HumanMessage(content=question))
    answer = chat(st.session_state['messages'])
    st.session_state['messages'].append(AIMessage(content=answer.content))
    return answer.content  

#intialize the streamlit app
st.set_page_config(page_title = "Conversational Q&A Chatbot Demo")

st.header("Conversational Q&A chatbot using Langchain")

input = st.text_input("Input:", key = "input")
answer = get_openai_response(input) 

submit = st.button("Ask the question")

#if button is clicked

if submit:
    st.subheader("Here is your answer")
    st.write(answer)

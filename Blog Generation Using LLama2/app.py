import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from langchain_community.llms import CTransformers

## Function to get the response from LLAma 2 model

def getLLamaResponse(input_text,no_words,blog_style):
    llm = CTransformers(model = 'E:\Gen-AI\Langchain\Blog Generation Using LLAMA 2\model\llama-2-7b-chat.ggmlv3.q8_0.bin',model_type = 'llama',config={'max_new_tokens':256,'temperature': 0.01})

    ##Prompt Template
    template = """Write a blog for {blog_style} jon profile for a topic {input_text} within {no_words} words."""

    prompt = PromptTemplate(input_variables=["blog_style",'input_text','no_words'],template=template)

    #generate the response from the llama 2 model
    repsonse =  llm(prompt.format(blog_style = blog_style,input_text = input_text, no_words = no_words))

st.set_page_config(page_title="Generation Blogs", page_icon=" ", layout="centered", initial_sidebar_state="collapsed", menu_items=None)

st.header("Gererate Blogs")

input_text = st.text_input("Enter the Blog Topic")

#

col1,col2 = st.columns([5,5])

with col1:
    no_words = st.text_input('No of words')

with col2:
    blog_style = st.selectbox('Writing the blog for',('Reseacchers','Data Scientist','Common People'),index = 0)

submit =st.button("Generate")

#Final Response
if submit:
    st.write(getLLamaResponse(input_text,no_words,blog_style))




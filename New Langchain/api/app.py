from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
import os
from langserve import add_routes
import uvicorn
from langchain_community.llms import Ollama

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

app = FastAPI(
    title = 'Langchain Server',
    version = "1.0",
    description = "A simple API server"
)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)


model = ChatOpenAI()

llm = Ollama(model = "llama2")

prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")

prompt2 = ChatPromptTemplate.from_template("Write me an poem about {topic} with 100 words")


add_routes(
    app,
    prompt1|model,
    path= "/essay"
)


add_routes(
    app,
    prompt2|llm,
    path= "/poem"
)

if __name__ =="__main__":
    uvicorn.run(app,host="localhost",port = 8000)
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv


# loading the environment variables
load_dotenv()

## Langsmith tracking
#os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")
#os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")


# Creating the FastAPI app
app = FastAPI(
    title="Langchain Server",
    version="1.0",
    decsription="A simple API Server which can be used to interact with the API server"
)


# adding route for ChatOpenAI model
add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)


# creating different models
model = ChatOpenAI()
llm = Ollama(model="llama2")


# Creating different prompts for different models
prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2 = ChatPromptTemplate.from_template("Write me an poem about {topic} for a 5 years child with 100 words")


# adding route for model which uses ChatOpenAI
add_routes(
    app,
    prompt1|model,
    path="/essay"
)

# adding route for model which uses Llama2 via ollama
add_routes(
    app,
    prompt2|llm,
    path="/poem"
)



if __name__=="__main__":
    uvicorn.run(app, host="localhost", port=8000)

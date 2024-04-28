import requests
import streamlit as st


# Function for invoking openai model  
def get_openai_response(input_text):
    response = requests.post("http://localhost:8000/essay/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']['content']


# Function for invoking llama2 model using ollama
def get_ollama_response(input_text):
    response = requests.post(
    "http://localhost:8000/poem/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']



# Streamlit framework
st.title('Langchain Demo With OpenAI and LLAMA2 API')
input_text = st.text_input("Write an essay on below topics")
input_text1 = st.text_input("Write a poem on below topic")


if input_text:
    st.write(get_openai_response(input_text))

if input_text1:
    st.write(get_ollama_response(input_text1))
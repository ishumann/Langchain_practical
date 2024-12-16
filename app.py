# Q&A Chatbot
import os
# from dotenv import load_dotenv
# load_dotenv()
# from lanchain.llms import OpenAI
from langchain_openai import OpenAI # for gpt 3.5 turbo
from langchain_community.chat_models import ChatOpenAI  # gpt-4o-mini
import streamlit as st

## Funtion to load OpenAI model and get response


def get_openai_response(question):
    llm = ChatOpenAI(
        # openai_api_key=os.getenv("OPENAI_API_KEY"),
        model_name="gpt-4o-mini",
        temperature=0.5,
    )
    response = llm.invoke(question).content
    return response

# Initializing our streamlit app


st.set_page_config(page_title="Q&A Demo")

st.header("Langchain Application")

input = st.text_input("Input: ", key="input")

submit = st.button("Ask the Question")


if submit:
    response = get_openai_response(input)
    st.subheader("The Response is")
    st.write(response)

# gpt_4o_mini =  ChatOpenAI(
#     openai_api_key=os.environ["OPEN_API_KEY"], temperature=0.6, model="gpt-4o-mini"
# )

# gpt_4o_mini
# future implementations - output parsers , conversational buffer memory, implement schemas like human message system, ai system, system messages

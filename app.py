# Importing the necessary libraries

import os
from api_key import apikey
import streamlit as st
import pandas as pd

from langchain_openai import OpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent

from dotenv import load_dotenv, find_dotenv
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI

#OpenAIKey
os.environ['OPENAI_API_KEY'] = apikey
load_dotenv(find_dotenv())


# App 

# Title
st.title("Financial ChatBot for GFC 🤖")

# Welcome Message
st.write('Hello, 👋 I am your financial assistant and I am here to help you get upto date with the financial performance of big companies.')

# Explanation Sidebar

with st.sidebar:
    st.write("🎉 Welcome to the Financial Chatbot! 📈💰")
    st.caption('''Are you ready to dive into the world of finance and explore the balance sheets and cash flows of companies like Microsoft, Tesla, and Apple? 🚀

To get started on this fun and informative exploration, simply upload your CSV file containing the financial data. Our chatbot will assist you in analyzing the data and answering any questions you may have. Whether you're a financial enthusiast or just curious about the performance of these companies, we're here to help!

Let's embark on this exciting journey together. Upload your CSV file and let's begin! 📊💡''')
    
    
    st.divider()
    st.caption("<p style='text-align:center'> made with ❤️ by Anshuman</p>",unsafe_allow_html=True)
    
# Initialise the key in the session state 
if 'clicked' not in st.session_state:
    st.session_state.clicked={1:False}

# Function to update the value in the session state
def clicked(button):
    st.session_state.clicked[button]= True
st.button("Let's get started", on_click = clicked, args=[1])
if st.session_state.clicked[1]:
    user_csv = st.file_uploader("Upload your file here", type="csv")
    
    if user_csv is not None:
        user_csv.seek(0)
        df = pd.read_csv(user_csv, low_memory=False)
    
    
        # Prompt Template
        template = """Question: {question}

        Answer: Let's think step by step."""

        prompt = PromptTemplate.from_template(template)
        # LLM 

        llm = OpenAI()

        llm_chain = LLMChain(prompt=prompt, llm=llm)
        
        #Pandas agent
        pandas_agent = create_pandas_dataframe_agent(llm, df, verbose = True)
        
        @st.cache_data
        def function_question_dataframe():
            dataframe_info = pandas_agent.run(user_question_dataframe)
            st.write(dataframe_info)
            return

        st.subheader('Ask Me!!')

        user_question_dataframe = st.text_input( "What would you like to know about your dataframe?")
        if user_question_dataframe is not None and user_question_dataframe not in ("","no","No"):
            function_question_dataframe()
        if user_question_dataframe in ("no", "No"):
            st.write("")

    

import streamlit as st
import re
from langchain_community.chat_models import ChatOllama
from langchain.chains import create_sql_query_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from sql_execution import db, get_schema


# Function to provide sql query as response from a user's question

def get_llama2_response(question, db):
    chain = create_sql_query_chain(llm, db)
    response = chain.invoke({"question": question})
    return response 

# Function to extract the SQL query from a text

def extract_query(text):
    query = re.search(r"```\n(.*?)```", text, re.DOTALL)  
    sql_query = query.group(1)
    return sql_query

# Define a prompt template for sql to text chain 

template = """Based on the table schema below, question, sql query, and sql response, write a natural language response:
{schema}

Question: {question}
SQL Query: {query}
SQL Response: {response}"""

prompt_response = ChatPromptTemplate.from_template(template)
llm = ChatOllama(model="llama2")

# def get_schema(db):
#    return db.get_table_info()

# Function to retrieve query from the Sql database and give the natural language response 

def read_sql_query(question, db):
    
    final_chain=(
        RunnablePassthrough.assign(query=extract_query(get_llama2_response(question,db))).assign(
            schema=get_schema(db),
            response = lambda x: db.run(x["query"]),
        )
        |prompt_response
        |llm
        |StrOutputParser()
    )
    nl_result = final_chain.invoke({"question": "How many customers are there"})
    return nl_result   


# create Streamlit App 

st.title("AI SQL Assistant ")
user_input = st.text_input("Enter your question here")
tab_titles = ["Result", "Query"]
tabs = st.tabs(tab_titles)

# 

if user_input:
    sql_query = extract_query(get_llama2_response(user_input, db))
    result = read_sql_query(user_input, db)

    with tabs[0]:
        st.write(result)
    with tabs[1]:
        st.write(sql_query)

 
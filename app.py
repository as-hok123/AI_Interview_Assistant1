import streamlit as st
from groq import Groq
st.set_config(page_title = "Placement Practice" , layout = "centered")
st.title("AI Placement Assistant")
st.caption("practice and prepare for your Interviews")
try:
client = Groq(api_Key =st.secrets("GROQ_API_KEY"))
except(keyError, FileNotFound):
st.error("API Key is missing. Add it in Advanced settings")
st.stop()
role = st.selectbox('Job Title',['Machine Learing Engineer','Senior Software Engineer','Data Analyst','Prompt Engineer','DevOps Engineer','other'])

import streamlit as st

st.title("AI Interview Assistant")

role = st.selectbox(
    "Job Title",
    ["Machine Learning Engineer", "Senior Engineer", "Software Engineer"]
)

st.write("Selected Job Role:", role)


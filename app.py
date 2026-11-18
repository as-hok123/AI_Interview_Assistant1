import streamlit as st
st.title("AI Interview Assistant")
role = st.selectbox(
    "Job Title",
    ["Machine Learning Engineer", "Senior Engineer", "Software Engineer"]
)
st.write("Selected Job Role:", role)
if role == "other":
    st.text_input('Enter you Job Title','xxxxxx')
    model = st.selectbox('model',['openai/gpt-oss-20b','Intermediate','Advanced"])
                                  level = st.selectbox('Difficulty',['Beginner','Intermediate','Advanced'])
                                  mode = st.radio('Activity',['ZGenerate Questions','Generate code Questions','Evaluate Answers','Improve Answers')


import streamlit as st from groq import Groq

st.set_page_config(page_title="AI Interview Assistant", page_icon="🫡", layout="centered")

st.title("🫡 AI Interview Assistant") st.caption("Your personal AI-powered interview preparation platform")

try: client = Groq(api_key=st.secrets["GROQ_API_KEY"]) except (KeyError, FileNotFoundError): st.error("Groq API key is missing. Configure it in Streamlit Secrets.") st.stop()

st.header("Interview Configuration")

role = st.selectbox("JOB TITLE", ["Software Engineer", "Senior Software Engineer", "Machine Learning Engineer", "Data Analyst", "Prompt Engineer", "DevOps Engineer", "Other"])

if role == "Other": custom_role = st.text_input("Enter your job title") if custom_role.strip(): role = custom_role.strip()

model = st.selectbox("SELECT AI MODEL", ["openai/gpt-oss-20b", "openai/gpt-oss-120b"])

difficulty = st.selectbox("DIFFICULTY LEVEL", ["Beginner", "Intermediate", "Advanced"])

mode = st.radio("ACTIVITY", ["Generate Questions", "Generate Code Questions", "Evaluate Answer", "Improve Answer"])

if mode in ["Generate Questions", "Generate Code Questions"]: count = st.slider("Number of Questions", 1, 10, 5)

if mode in ["Evaluate Answer", "Improve Answer"]: question = st.text_area("Enter Interview Question") answer = st.text_area("Enter Your Answer")

if st.button("🚀 Generate", use_container_width=True):

if role == "Other" and not custom_role.strip():
    st.warning("Please enter your job title.")

elif mode in ["Evaluate Answer", "Improve Answer"] and (not question.strip() or not answer.strip()):
    st.warning("Please enter both the question and answer.")

else:
    if mode == "Generate Questions":
        prompt = f"Generate {count} interview questions for {role} at {difficulty} level. Include technical, conceptual and practical questions."

    elif mode == "Generate Code Questions":
        prompt = f"Generate {count} coding interview questions for {role} at {difficulty} level. Include problem statements, input/output examples, constraints and Python examples."

    elif mode == "Evaluate Answer":
        prompt = f"Evaluate this interview answer for {role}. Question: {question}. Answer: {answer}. Provide a score out of 10, strengths, weaknesses, missing points and improvement suggestions."

    else:
        prompt = f"Improve this interview answer for {role}. Question: {question}. Original answer: {answer}. Provide a professional answer, important technical points and a short interview-ready version."

    try:
        with st.spinner("AI is generating your result..."):
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are an expert technical interviewer and professional career mentor."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_completion_tokens=3000
            )

            result = response.choices[0].message.content

        st.success("Generated successfully!")
        st.subheader("Your Interview Result")
        st.markdown(result)

    except Exception as e:
        st.error(f"Something went wrong: {e}")


st.divider() st.caption("AI Interview Assistant | Powered by Streamlit and Groq")
if role == "Other" and not custom_role.strip():
    st.warning("Please enter your job title.")

elif mode in ["Evaluate Answer", "Improve Answer"] and (not question.strip() or not answer.strip()):
    st.warning("Please enter both the question and answer.")

else:
    if mode == "Generate Questions":
        prompt = f"Generate {count} interview questions for {role} at {difficulty} level. Include technical, conceptual and practical questions."

    elif mode == "Generate Code Questions":
        prompt = f"Generate {count} coding interview questions for {role} at {difficulty} level. Include problem statements, input/output examples, constraints and Python examples."

    elif mode == "Evaluate Answer":
        prompt = f"Evaluate this interview answer for {role}. Question: {question}. Answer: {answer}. Provide a score out of 10, strengths, weaknesses, missing points and improvement suggestions."

    else:
        prompt = f"Improve this interview answer for {role}. Question: {question}. Original answer: {answer}. Provide a professional answer, important technical points and a short interview-ready version."

    try:
        with st.spinner("AI is generating your result..."):
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are an expert technical interviewer and professional career mentor."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_completion_tokens=3000
            )

            result = response.choices[0].message.content

        st.success("Generated successfully!")
        st.subheader("Your Interview Result")
        st.markdown(result)

    except Exception as e:
        st.error(f"Something went wrong: {e}")

import streamlit as st
from utils import extract_text_from_pdf, score_resume
from langchain.chat_models import AzureChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

st.title("Resume Ranker")

# Upload Job Description
jd_file = st.file_uploader("Upload Job Description (PDF)", type=["pdf"])

# Upload Resumes
resume_files = st.file_uploader("Upload up to 10 Resumes (PDF)", type=["pdf"], accept_multiple_files=True)

if jd_file and resume_files:
    st.info("Processing... Please wait.")

    jd_text = extract_text_from_pdf(jd_file)

    # Initialize AzureChatOpenAI
    llm = AzureChatOpenAI(
        openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        openai_api_base=os.getenv("AZURE_OPENAI_ENDPOINT"),
        deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
        openai_api_type="azure",
        openai_api_version="2023-03-15-preview",
        temperature=0.3
    )

    scores = []

    for file in resume_files:
        resume_text = extract_text_from_pdf(file)
        result = score_resume(llm, resume_text, jd_text)

        try:
            score_line = result.content.splitlines()[0]
            score = int(score_line.split(":")[1].strip())
            explanation = "\n".join(result.content.splitlines()[1:])
        except:
            score = 0
            explanation = "Error parsing LLM response."

        scores.append({
            "name": file.name,
            "score": score,
            "explanation": explanation
        })

    # Sort and display
    ranked = sorted(scores, key=lambda x: x["score"], reverse=True)

    st.subheader("Ranked Resumes")
    for i, item in enumerate(ranked, start=1):
        st.markdown(f"### {i}. {item['name']}")
        st.markdown(f"**Score**: {item['score']}")
        with st.expander("Explanation"):
            st.markdown(item['explanation'])

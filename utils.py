import os
import PyPDF2

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def score_resume(llm, resume_text, job_description):
    prompt = f"""
You are a professional recruiter. Compare the following resume to the job description and rate it from 0 to 100 with a short explanation.

Job Description:
{job_description}

Resume:
{resume_text}

Respond in the format:
Score: <score>
Explanation: <explanation>
"""
    response = llm.invoke(prompt)
    return response

# Resume-Ranker

Overview-<br>
The Resume Ranker is a web application that ranks resumes based on their relevance to a provided job description. Users can upload a job description (as text or PDF) and up to 10 resume PDFs. The application extracts content from the resumes, uses LangChain with Azure OpenAI to compare and score each resume against the job description, and displays a ranked list of resumes with their scores in a Streamlit interface. This tool is designed to assist recruiters or hiring managers in efficiently screening candidates.<br><br>

Tech Stack-<br>
LangChain: Framework for managing LLM interactions and document processing.<br>
Azure OpenAI: Provides the large language model (e.g., gpt-3.5-turbo or gpt-4) for scoring resumes.<br>
Streamlit: Python library for creating an interactive web interface.<br>
PyPDF2: Library for extracting text from PDF files.<br>
Python: Core programming language for the application.<br><br>

Prerequisites-<br>
Python 3.8 or higher<br>
Azure OpenAI account with access to an LLM model (e.g., gpt-3.5-turbo or gpt-4)<br>
Azure OpenAI API key, endpoint, and deployment name<br>
A job description (text or PDF) and up to 10 resume PDFs for testing<br>

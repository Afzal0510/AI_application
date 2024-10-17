import streamlit as st
import requests

# Streamlit UI
st.title("AI Chat with PDF Knowledge Base")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    st.write("Uploading PDF...")
    response = requests.post("http://localhost:8000/upload_pdf/", files={"file": uploaded_file})
    if response.status_code == 200:
        st.success("PDF uploaded successfully!")

question = st.text_input("Ask a question:")
if st.button("Submit"):
    response = requests.post("http://localhost:8000/ask_question/", json={"question": question})
    if response.status_code == 200:
        st.write("Answer: ", response.json()["answer"])




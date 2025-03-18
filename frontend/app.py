import streamlit as st
import requests

st.title("AI-Powered PDF Summarizer")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])
max_length = st.slider("Max Summary Length", 50, 500, 150)

if uploaded_file is not None:
    files = {"file": uploaded_file.getvalue()}
    response = requests.post(f"http://127.0.0.1:8000/summarize?model=bart", files=files)

    if response.status_code == 200:
        st.subheader("Summary:")
        st.write(response.json()["summary"])
    else:
        st.error("Error summarizing the document.")

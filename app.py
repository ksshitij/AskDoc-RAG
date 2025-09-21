import streamlit as st

st.title("AskDoc RAG (Prototype)")
st.write("Upload a document and try a simple retrieval pipeline.")

uploaded_file = st.file_uploader("Choose a PDF", type=["pdf"])
question = st.text_input("Ask a question")

if st.button("Search"):
    st.info("RAG pipeline not fully implemented yet – placeholder answer.")

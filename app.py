import streamlit as st
import os
import tempfile
from dotenv import load_dotenv

# --- IMPORTS FOR LANGCHAIN v0.1.x ---
# These imports are correct for the older, stable version
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain.chains import RetrievalQA
# --- END OF IMPORTS ---


# --- 1. LOAD API KEY ---
load_dotenv()
if not os.getenv("GOOGLE_API_KEY"):
    st.error("GOOGLE_API_KEY not found in .env file. Please add it and restart.")
    st.stop()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# --- 2. DEFINE THE RAG PROCESSING FUNCTION ---
@st.cache_resource
def get_qa_chain_from_pdf(uploaded_file):
    print(f"--- Processing {uploaded_file.name} ---")
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(uploaded_file.getvalue())
        temp_file_path = temp_file.name

    try:
        loader = PyPDFLoader(temp_file_path)
        docs = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        splits = text_splitter.split_documents(docs)

        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

        vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)
        
        retriever = vectorstore.as_retriever()

        # --- This is the OLD, STABLE way to create a RAG chain ---
        llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=retriever
        )
        # --------------------------------------------------------
        
        return qa_chain
    
    except Exception as e:
        st.error(f"Error processing PDF: {e}")
        return None
    finally:
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)

# --- 3. THE STREAMLIT USER INTERFACE ---
st.set_page_config(page_title="AskDoc RAG", page_icon="💬")
st.title("AskDoc RAG 💬")
st.write("Upload a PDF document and ask any question about its content.")

with st.sidebar:
    st.header("Upload Your Document")
    uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    # 1. Process the document
    if "qa_chain" not in st.session_state or st.session_state.file_name != uploaded_file.name:
        with st.spinner(f"Processing {uploaded_file.name}... This may take a moment."):
            st.session_state.qa_chain = get_qa_chain_from_pdf(uploaded_file)
            st.session_state.file_name = uploaded_file.name
            
            if st.session_state.qa_chain:
                st.success("Document processed! You can now ask questions.")
            else:
                st.error("Failed to process document. Please try again.")
    
    # 2. Handle user questions
    if "qa_chain" in st.session_state:
        user_question = st.text_input("Ask a question about your document:")
        
        if user_question:
            with st.spinner("Searching for the answer..."):
                # --- This is the OLD, STABLE way to get an answer ---
                response = st.session_state.qa_chain.run(user_question)
                st.write(response)

else:
    st.info("Please upload a PDF document in the sidebar to get started.")
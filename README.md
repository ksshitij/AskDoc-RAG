# AskDoc RAG 💬

**Chat with any PDF!** This is a web application built with Streamlit that lets you upload a PDF document and ask it questions. It uses the Google Gemini AI, LangChain, and a Chroma vector database to find contextually-aware answers from *within your document*.

This project is a powerful demonstration of a complete **Retrieval-Augmented Generation (RAG)** pipeline.

---

## 📸 In Action

Here's what it looks like. You can...

**1. Upload any PDF file:**
<img width="1919" height="949" alt="Screenshot 2025-10-30 130128" src="https://github.com/user-attachments/assets/2d232ce1-18fd-4f9a-815b-12b50d7518b3" />


**2. Ask a question about its content:**
<img width="1917" height="359" alt="Screenshot 2025-10-30 130431" src="https://github.com/user-attachments/assets/4641f738-aa3b-435b-a7b8-e0035744362e" />


**3. Get an AI-powered answer based *only* on the document's context:**


---

## ✨ Features

* **File Upload:** Securely upload any PDF document.
* **Document Processing:** Automatically splits the document into indexed, searchable chunks.
* **Vector Storage:** Uses **ChromaDB** to store the document's "memory" (embeddings).
* **RAG Pipeline:** Uses **LangChain** to connect the user's question, the document's memory, and the AI brain.
* **AI-Powered Answers:** Leverages **Google's Gemini-Pro** model to generate natural, accurate answers based on the retrieved context.
* **Simple UI:** A clean, easy-to-use web interface built with **Streamlit**.

---

## 🛠️ Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io/)
* **AI Framework:** [LangChain](https://www.langchain.com/)
* **LLM (Brain):** [Google Gemini Pro](https://ai.google.dev/)
* **Vector Database (Memory):** [ChromaDB](https://www.trychroma.com/)
* **PDF Loading:** `PyPDF`
* **Language:** Python 3.11

---

## 🚀 How to Run This Locally

Want to run this on your own machine? It's simple.

**1. Clone the Repository:**
```bash
git clone [https://github.com/ksshitij/AskDoc-RAG.git](https://github.com/ksshitij/AskDoc-RAG.git)
cd AskDoc-RAG

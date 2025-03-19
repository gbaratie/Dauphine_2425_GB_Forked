import streamlit as st
import requests

# Page title
st.title("Upload Files for RAG")

# Introduction
st.markdown(
    """
    Welcome to the file upload page for **RAG (Retrieval-Augmented Generation)**! 
    Here, you can upload your documents to use them in information retrieval and augmented generation processes.
    
    Make sure your files are in a compatible format (PDF, TXT, etc.) before uploading.
    """
)

# File upload section
st.subheader("📂 Upload Your Files")
st.markdown("Use the tool below to upload your files. These files will be analyzed and integrated into the RAG system.")

# File uploader
uploaded_files = st.file_uploader("Drag and drop your files here or click to select them", accept_multiple_files=True, type=["txt"])

if uploaded_files:
    st.success(f"{len(uploaded_files)} file(s) successfully uploaded!")
    for file in uploaded_files:
        st.write(f"📄 {file.name}")
        
        # Envoyer le fichier à l'API FastAPI
        files = {'file': (file.name, file, file.type)}
        response = requests.post("http://127.0.0.1:8000/files/upload-file", files=files)
        
        if response.status_code == 200:
            st.success(f"File {file.name} uploaded and processed successfully!")
        else:
            st.error(f"Failed to upload {file.name}. Error: {response.text}")

# Sidebar with Documentation Links
with st.sidebar:
    st.header("📚 Documentation")
    st.markdown(
        """
        This sidebar contains links to RAG-related resources:
        
        - [Cohere Embeddings Documentation](https://docs.cohere.com/docs/embeddings)
        - [Cohere API Reference - Embed](https://docs.cohere.com/reference/embed)
        - [Cohere API Reference - Chat](https://docs.cohere.com/reference/chat)
        
        Explore these resources to learn more about RAG and how to implement it!
        """
    )

st.markdown("For more examples and detailed explanations, check out the [Streamlit documentation](https://docs.streamlit.io). Happy coding!")
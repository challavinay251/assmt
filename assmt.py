import streamlit as st
import requests
import json

# Function to interact with OpenAI's RAG model
def query_rag_model(query, context):
    # Your OpenAI API key
    api_key = "YOUR_OPENAI_API_KEY"
    
    # API endpoint
    endpoint = "https://api.openai.com/v1/engines/rag-1/completions"

    # Request parameters
    data = {
        "prompt": query,
        "documents": [context],
        "max_tokens": 50
    }

    # Set headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # Send request to OpenAI API
    response = requests.post(endpoint, headers=headers, data=json.dumps(data))

    # Parse response
    if response.status_code == 200:
        return response.json()["choices"][0]["text"].strip()
    else:
        return "Error: Unable to retrieve response from OpenAI RAG model."

# Streamlit app layout
def main():
    st.title("PDF Chatbot with OpenAI RAG")
    
    # File upload
    st.header("Upload PDF File")
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        # Read PDF file
        pdf_text = uploaded_file.read()

        # Display PDF text
        st.header("PDF Content")
        st.write(pdf_text)

        # Chat interface
        st.header("Chat with PDF Content")
        query = st.text_input("Enter your question:")
        if st.button("Ask"):
            # Call OpenAI RAG model
            response = query_rag_model(query, pdf_text.decode("utf-8"))
            st.write("Bot:", response)

if __name__ == "__main__":
    main()

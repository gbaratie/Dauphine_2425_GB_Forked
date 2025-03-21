import sys
from dotenv import load_dotenv
import os

load_dotenv()

sys.path.append(os.getenv('PYTHONPATH'))

import streamlit as st
import requests

from rest.model.chat_request import ChatRequest



#Titles
st.title("💬 Chatbot")
st.caption("🚀 My First Chatbot using Cohere")



#Sidebar with description
with st.sidebar:
    st.markdown("""
                This page demonstrates how to create a memory-enabled chatbot using Cohere, showcasing
                the integration of advanced NLP capabilities in a user-friendly interface. Explore the 
                examples and learn how to build your own intelligent applications.     
                """)
    st.header("📚 Learn More")
    st.markdown("""Explore the examples and learn how to build your own intelligent applications.
                [Cohere API](https://docs.cohere.com/reference/chat)""")
            
st.markdown(
        """
        On this demonstration we will be able to send request to Cohere and have a chat with history 
        """
        )

#FastAPI created at 
api_url="http://127.0.0.1:8000/chat"

# Initialize the chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you my friend?"}]

# Display the chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# When a user submits a message
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display the user's message
    st.chat_message("user").write(prompt)

    # Prepare the payload for the API request
    request = ChatRequest(prompt=prompt)
    # Send the request to the API
    try:
        response = requests.post(api_url, json=request.to_dict())
        response.raise_for_status() # Will raise an exception for HTTP errors
        bot_response = response.json().get("response", "I didn't understand that.")
    except requests.exceptions.RequestException as e:
        bot_response = f"Error: {e}"
    
    # Display the bot's response
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    st.chat_message("assistant").write(bot_response)




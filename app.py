import streamlit as st
from src.chain import LLMchain

# Description of PolicyBot
policybot_description = """
PolicyBot is an AI assistant designed for car insurance inquiries. 
PolicyBot is based on the guidelines and information provided in [this document](https://assets.churchill.com/motor-docs/policy-booklet-0923.pdf).
"""

# Render the description in the sidebar
with st.sidebar:
    st.markdown(policybot_description, unsafe_allow_html=True)

# Main title 
# Main title with emoji
st.title("PolicyBot")
st.subheader(": For Your Car 🚗 Insurance Inquiries")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("How can I assist you with your car insurance today?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate and display assistant response with spinner
    with st.spinner("Generating response..."):
        response = LLMchain.invoke(prompt)
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

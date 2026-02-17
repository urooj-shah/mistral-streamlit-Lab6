import streamlit as st
from mistralai import Mistral
import os

st.title("💬 Customer Support Chatbot")

# API key from Streamlit secrets
client = Mistral(api_key=st.secrets["MISTRAL_API_KEY"])

user_input = st.text_input("Enter your query:")

if st.button("Send") and user_input:
    with st.spinner("Thinking..."):
        response = client.chat.complete(
            model="mistral-medium",
            messages=[
                {"role": "system", "content": "You are a professional customer support chatbot."},
                {"role": "user", "content": user_input}
            ]
        )
        st.success(response.choices[0].message.content)

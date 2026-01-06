import streamlit as st
from openai import OpenAI
import os


client = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv("API_KEY"))

st.title("LLM Chat")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Enter your message"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = client.chat.completions.create(
            model=os.getenv("MODEL"),
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                *st.session_state.messages
            ]
        )
        reply = response.choices[0].message.content
        st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})

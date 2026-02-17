import streamlit as st
from chain import build_chain

st.set_page_config(page_title="Local RAG Chatbot", layout="wide")

st.title("💬 Local RAG Chatbot (Ollama + FAISS)")

# Build chain once
if "chain" not in st.session_state:
    st.session_state.chain = build_chain()

chain = st.session_state.chain

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Chat input
user_input = st.chat_input("Ask something...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    response = chain.invoke({"question": user_input})

    answer = response["answer"]

    st.session_state.messages.append({"role": "assistant", "content": answer})
    st.chat_message("assistant").write(answer)
